from django.http import Http404
from django.db import models

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from minesweeper.models import Player
from minesweeper.permissions import IsOwnerOrReadOnly
from minesweeper.serializers import PlayersSerializer
from minesweeper.cache import CashedPlayer
from minesweeper.filters import PlayersFilter


class PlayersView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """
    * list, retrive, update, partial update
    * On update and partial update change Player stats
    """
    queryset = Player.objects.all().filter(user__is_active=True).select_related("user")
    serializer_class = PlayersSerializer
    permission_classes = IsOwnerOrReadOnly,
    filterset_class = PlayersFilter

    def list(self, request: Request, *args, **kwargs) -> Response:
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        cached_data = CashedPlayer.list(
            serializer.data,
            request.query_params
        )

        return Response(cached_data)

    def get_object(self, *args, **kwargs) -> models.Model:
        """
        * Using User id in URL (not Player id)
        * Caching
        """
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        try:            
            pk = int(filter_kwargs.pop('pk'))
        except:
            raise Http404()

        instanse = CashedPlayer.get(
            id=pk, 
            queryset=queryset, 
            filter=filter_kwargs
        )

        self.check_object_permissions(self.request, instanse)
        return instanse

    def get_me(self) -> models.Model:
        return CashedPlayer.get(
            self.request.user.id,
            self.get_queryset()
        )

    @action(
        methods=["get", "put", "patch"],
        detail=False,
        permission_classes=(IsAuthenticated,),
        url_name="player-me",
        url_path="me",
    )
    def me(self, request, *args, **kwargs):
        self.get_object = self.get_me

        match request.method:
            case "GET":
                return self.retrieve(request, *args, **kwargs)
            case "PUT":
                return self.update(request, *args, **kwargs)
            case "PATCH":
                return self.partial_update(request, *args, **kwargs)
