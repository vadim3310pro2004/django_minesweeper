import django_filters.rest_framework as filters
from django.db.models import QuerySet


class PlayersFilter(filters.FilterSet):
    top_players = filters.CharFilter(
        label="top players", 
        method="filter_top_players"
    )

    def filter_top_players(
        self, 
        queryset: QuerySet, 
        value, 
        filter,
    ):
        if filter == '_':
            filter = None
        elif isinstance(filter, int):
            if (filter < 1):
                return queryset
        else:
            return queryset

        filtred_queryset = (
            queryset
            .order_by("averange_resoult")
        )

        try:
            return filtred_queryset[:filter]
        except:
            return filtred_queryset     

    class Meta:
        fields = '__all__'
