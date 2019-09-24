from django.db import models
import time
import uuid
# Create your models here.


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class Devices(models.Model):

    id = models.CharField(primary_key=True, default=next_id, max_length=50)
    name = models.CharField(max_length=50)
    addr = models.CharField(max_length=50)
    mac = models.CharField(max_length=50)
    create_at = models.FloatField(default=time.time())
    updated_at = models.FloatField(default=time.time())

    def __str__(self):
        return self.name.strip()