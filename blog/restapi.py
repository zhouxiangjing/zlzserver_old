from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from blog.restapi_serializers import *
from django.http import JsonResponse
import time


class CommentViewSet(ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# class AuthView(APIView):
#
#     def post(self, request, *args, **kwargs):
#         ret = {'code':1000, 'msg':None}
#         try:
#             usr = request.data.get('username')
#             pas = request.data.get('password')
#             print(usr)
#             obj = models.User.objects.filter(username=usr,password=pas).first()
#             print(obj)
#             print(type(obj))
#             print(obj.username)
#             print(obj.password)
#             if not obj:
#                 ret['code'] = '1001'
#                 ret['msg'] = '用户名或者密码错误'
#                 return JsonResponse(ret)
#             # 里为了简单，应该是进行加密，再加上其他参数
#             token = str(time.time()) + usr
#             print(token)
#             models.userToken.objects.update_or_create(username=obj, defaults={'token': token})
#             ret['msg'] = '登录成功'
#         except Exception as e:
#             ret['code'] = 1002
#             ret['msg'] = '请求异常'
#
#         return JsonResponse(ret)