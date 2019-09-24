from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import CursorPagination

from django.http import JsonResponse
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

import time
import datetime
from .models import Devices
from .serializers import DevicesSerializers


class DevicesAPIView(APIView):

    authentication_classes = [BasicAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request):

        devices = Devices.objects.filter(updated_at__gt=time.time()-7)

        page = CursorPagination()
        page.ordering = 'name'
        page_list = page.paginate_queryset(devices, request, view=self)
        ser = DevicesSerializers(instance=page_list, many=True)

        return page.get_paginated_response(ser.data)

    def post(self, request):

        name = self.request.data.get('name')
        addr = self.request.data.get('addr')
        mac = self.request.data.get('mac')

        devices, created = Devices.objects.update_or_create(name = name,
                                                        defaults = {
                                                            'addr': addr,
                                                            'mac': mac,
                                                            'updated_at': time.time()
                                                        })


        return Response({'code': 0, 'msg': '更新成功'})





# class DevicesViewSet(APIView):
#
#     queryset = Devices.objects.all()
#     serializer_class = DevicesSerializers
#     authentication_classes = (SessionAuthentication,)
#     permission_classes = (IsAuthenticated,)
#
#     def perform_create(self, serializer):
#         my_model, created = Devices.objects.update_or_create(name=self.request.data['name'],
#                                                              defaults={
#                                                                  'addr': self.request.data['addr'],
#                                                                  'mac': self.request.data['mac'],
#                                                                  'updated_at': time.time()
#                                                              })
