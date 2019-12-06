import uuid
import time
import random
import string
import json
import configparser
from django.conf import settings

from aliyunsdkcore.client import AcsClient
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest

conf = configparser.ConfigParser()
conf.read(settings.CONF_FILE, encoding="utf-8")
remote_host = conf.get("remote_host", "host")

REGION = conf.get("sms", "region")
ACCESS_KEY_ID = conf.get("sms", "access_key_id")
ACCESS_KEY_SECRET = conf.get("sms", "access_key_secret")
SMS_SIGN_NAME = conf.get("sms", "sign_name")
SMS_TEMPLATE_CODE = conf.get("sms", "template_code")

sms_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)


def ran_str(num):
    return ''.join(random.sample(string.ascii_letters + string.digits, num))


def ran_number(num):
    return ''.join(random.sample(string.digits, num))


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


def get_name():
    return 'un_' + ran_str(8)


def send_sms(phone_numbers, code):
    sms_params = "{\"code\":\"" + code + "\"}"
    smsRequest = SendSmsRequest.SendSmsRequest()
    smsRequest.set_TemplateCode(SMS_TEMPLATE_CODE)
    smsRequest.set_TemplateParam(sms_params)
    smsRequest.set_OutId(uuid.uuid1())
    smsRequest.set_SignName(SMS_SIGN_NAME)
    smsRequest.set_PhoneNumbers(phone_numbers)
    smsResponse = sms_client.do_action_with_exception(smsRequest)
    smsResponse = str(smsResponse, encoding='utf-8')
    smsResponse = json.loads(smsResponse)
    return smsResponse['Code']
