import django
import os
import rest_framework

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zlzserver.settings")
django.setup()


from zlz.models import Devices
from zlz.serializers import DevicesSerializers

queryset = Devices.objects.latest('id')

print(queryset)

serializers = DevicesSerializers(queryset)

print(serializers.data)
