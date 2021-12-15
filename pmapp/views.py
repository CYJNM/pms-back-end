from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .utils.JsonResponse import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from .utils.filters import ServerFilter, UserFilter
from rest_framework import filters
from rest_framework_bulk import BulkModelViewSet

from .serializers import *


# Create your views here.

# 用户登录登出视图
class UserView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        # queryset = User.objects.all()
        # s = UserSerializer(instance=queryset, many=True)
        token = request.headers.get('Authorization')
        # token_msg = authentication.JSONWebTokenAuthentication().get_jwt_value(token)
        # print(token_msg)
        return Response({"code": 200, "data": {"roles": ["admin"], "introduction": "I am a super administrator",
                                                 "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
                                                 "name": "Super Admin"}})

    @staticmethod
    def post(request):
        return Response({
            "code": 200,
            "data": 'success'
        })


class GroupView(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        user_count = len(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return JsonResponse(code=200, msg="请求成功", total=user_count, data=serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # super().ser
        return JsonResponse(code=200, msg="请求成功", data=response.data)

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return JsonResponse(code=status.HTTP_200_OK, msg="请求成功")

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return JsonResponse(code=status.HTTP_200_OK, msg="请求成功")


# 用户视图api
class UsersView(BulkModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_class = UserFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        user_count = len(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return JsonResponse(code=200, msg="请求成功", total=user_count, data=serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # super().ser
        return JsonResponse(code=200, msg="请求成功", data=response.data)

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return JsonResponse(code=status.HTTP_200_OK, msg="请求成功")

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return JsonResponse(code=status.HTTP_200_OK, msg="请求成功")

    def bulk_destroy(self, request, *args, **kwargs):
        super().bulk_destroy(request, *args, **kwargs)
        return JsonResponse(code=status.HTTP_200_OK, msg='请求成功')


# 服务器视图api
class ServerView(BulkModelViewSet):
    queryset = Server.objects.all().order_by('id')
    serializer_class = ServerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['server_name', 'server_type', 'server_belong', 'id']
    filter_class = ServerFilter
    # 搜索
    # search_fields = ('id',)
    # 排序
    # ordering_fields = ('id',)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        server_count = len(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return JsonResponse(code=status.HTTP_200_OK, msg="请求成功", total=server_count, data=serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # super().ser
        return JsonResponse(code=status.HTTP_201_CREATED, msg="请求成功", data=response.data)

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return JsonResponse(code=status.HTTP_200_OK, msg="请求成功")

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return JsonResponse(code=status.HTTP_200_OK, msg="请求成功")

    def bulk_destroy(self, request, *args, **kwargs):
        super().bulk_destroy(request, *args, **kwargs)
        return JsonResponse(code=status.HTTP_200_OK, msg='请求成功')

