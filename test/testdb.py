import django
import os
import rest_framework
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zlzserver.settings")
django.setup()

from blog.models import *

# from zlz.models import *
# from zlz.serializers import DevicesSerializers

# queryset = Devices.objects.latest('id')
# print(queryset)
# serializers = DevicesSerializers(queryset)
# print(serializers.data)

z = timezone.now()

d1 = timezone.datetime.fromtimestamp(timezone.datetime.now().timestamp() - 60)
d2 = timezone.datetime.now()
sms_code = SmsCode.objects.filter(phone='15236023900', updated__range=(d1, d2)).first()

nn = 0