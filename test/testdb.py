import django
import os
import rest_framework
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zlzserver.settings")
django.setup()

from blog.models import *
from blog.restapi_serializers import *

# from zlz.models import *
# from zlz.serializers import DevicesSerializers

# queryset = Devices.objects.latest('id')
# print(queryset)
# serializers = DevicesSerializers(queryset)
# print(serializers.data)

user = User.objects.filter(phone='15236023900').first()

val2 = UserSerializer(user).data

nn = 0