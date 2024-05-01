from typing import Iterable
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from django.db.models import Model, QuerySet 


class BaseCache:
    cache_alias: str
    cache_time: int

    @classmethod
    def list(
        cls,
        data: Iterable[Model],
        filter: dict = {},
    ) -> Iterable[Model]:
        cache_name = cls.cache_alias + '_LIST' + str(sorted(filter.items()))

        if cached_data := cache.get(cache_name):
            return cached_data

        cache.set(cache_name, data, cls.cache_time)

        return data

    @classmethod
    def get(
        cls,
        id: int,
        queryset: QuerySet,
        filter: dict = {},
    ) -> Model:
        cache_name = cls.cache_alias + str(id)

        if instance := cache.get(cache_name):
            return instance

        instance = get_object_or_404(queryset, user_id=id, **filter)
        cache.set(cache_name, instance, cls.cache_time)

        return instance
    
    @classmethod
    def invalidate(cls, id: int) -> None:
        cache_name = cls.cache_alias + str(id)
        cache.delete(cache_name)