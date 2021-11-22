from rest_framework.serializers import ModelSerializer
from .models import Server, Project
from django.contrib.auth.models import User
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)


class ServerSerializer(BulkSerializerMixin, ModelSerializer):

    class Meta:
        model = Server
        fields = '__all__'
        list_serializer_class = BulkListSerializer


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'id')


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

