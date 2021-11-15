from django_filters import rest_framework
from ..models import Server


class ServerFilter(rest_framework.FilterSet):
    server_name = rest_framework.CharFilter(field_name='server_name', lookup_expr='icontains')
    server_belong = rest_framework.CharFilter(field_name='server_belong', lookup_expr='icontains')
    server_type = rest_framework.CharFilter(field_name='server_type', lookup_expr='icontains')

    class Meta:
        model = Server
        fields = ['server_name',]
