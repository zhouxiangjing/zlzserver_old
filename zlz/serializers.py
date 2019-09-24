from rest_framework import serializers
from .models import Devices


class DevicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Devices  # 指定的模型类
        fields = ['name', 'addr', 'mac']