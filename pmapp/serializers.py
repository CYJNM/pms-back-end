import re

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Server, Project, User
from django.contrib.auth.models import Group
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)


class GroupSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = ['id', 'name']


class ServerSerializer(BulkSerializerMixin, ModelSerializer):

    class Meta:
        model = Server
        fields = '__all__'
        list_serializer_class = BulkListSerializer


class UserSerializer(BulkSerializerMixin, ModelSerializer):
    password2 = serializers.CharField(write_only=True, label='确认密码')
    # group = GroupSerializer(many=True)
    # user_set = GroupSerializer(many=True)
    group = GroupSerializer(source='groups', many=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'mobile', 'group', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_mobile(self, value):
        """单独校验手机号"""
        if not re.match(r'1[3-9]\d{9}', value):
            raise serializers.ValidationError('手机格式错误')
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('两次密码不一致')
        # mobile = attrs['mobile']
        return attrs

    def create(self, validated_data):
        # 移除不需要的字段
        del validated_data['password2']

        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # 密码加密后赋值给user的password属性
        user.save()

        return user


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


