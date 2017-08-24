# models.py
from django.db import models


class IpInfo(models.Model):
    ipaddr = models.CharField(max_length=20)
    mac = models.CharField(max_length=30)
    username = models.CharField(max_length=20)