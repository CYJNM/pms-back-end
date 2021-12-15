from django_filters import rest_framework
from ..models import Server, User


def filter_by_ids(queryset, name, value):
    values = value.split(',')
    return queryset.filter(id__in=values)


class ServerFilter(rest_framework.FilterSet):
    server_name = rest_framework.CharFilter(field_name='server_name', lookup_expr='icontains')
    server_belong = rest_framework.CharFilter(field_name='server_belong', lookup_expr='icontains')
    server_type = rest_framework.CharFilter(field_name='server_type', lookup_expr='icontains')
    id = rest_framework.NumberFilter(field_name='id', lookup_expr='icontains')
    ids = rest_framework.CharFilter(method=filter_by_ids)

    class Meta:
        model = Server
        fields = ['server_name', 'server_belong', 'server_type', 'id', 'ids']


class UserFilter(rest_framework.FilterSet):
    username = rest_framework.CharFilter(field_name='username', lookup_expr='icontains')
    mobile = rest_framework.NumberFilter(field_name='mobile', lookup_expr='icontains')
    id = rest_framework.NumberFilter(field_name='id', lookup_expr='icontains')
    ids = rest_framework.CharFilter(method=filter_by_ids)

    class Meta:
        model = User
        fields = ['username', 'mobile', 'id', 'ids']
