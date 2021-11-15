from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .utils.JsonResponse import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from .utils.filters import ServerFilter
from rest_framework import filters

from .serializers import *


# Create your views here.


# 用户视图api
class UserView(APIView):

    def get(self, request):
        # queryset = User.objects.all()
        # s = UserSerializer(instance=queryset, many=True)
        token = request.headers.get('Authorization')
        # token_msg = authentication.JSONWebTokenAuthentication().get_jwt_value(token)
        # print(token_msg)
        return Response({"code": 200, "data": {"roles": ["admin"], "introduction": "I am a super administrator",
                                                 "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
                                                 "name": "Super Admin"}})

    def post(self, request):
        return Response({
            "code": 200,
            "data": 'success'
        })
#

# 服务器视图api
class ServerView(ModelViewSet):
    queryset = Server.objects.all().order_by('id')
    serializer_class = ServerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['server_name', 'server_type', 'server_belong']
    filter_class = ServerFilter
    # 搜索
    search_fields = ('title', 'description', 'content')
    # 排序
    ordering_fields = ('id',)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        server_count = len(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return JsonResponse(code=200, msg="请求成功", total=server_count, data=serializer.data)
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


# 项目立项
def pro_start(request):
    response = render(request, 'pmapp/prostart.html', context=None)
    return response


# 项目上线
def pro_live(request):
    response = render(request, 'pmapp/prolive.html', context=None)
    return response


# 项目收款
def pro_payment(request):
    response = render(request, 'pmapp/propayment.html', context=None)
    return response


# 项目续保
def pro_renewal(request):
    response = render(request, 'pmapp/prorenewal.html', context=None)
    return response


# 项目下线
def pro_offline(request):
    response = render(request, 'pmapp/prooffline.html', context=None)
    return response


# 项目详情
def pro_details(request):
    response = render(request, 'pmapp/prodetails.html', context=None)
    return response
