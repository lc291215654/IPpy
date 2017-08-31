# models.py
from django.db import models


class IpInfo(models.Model):
    ipaddr = models.CharField(max_length=20)
    mac = models.CharField(max_length=40)
    username = models.CharField(max_length=30)
    hostname = models.CharField(max_length=50)
    describe = models.CharField(max_length=300)
    create_at = models.DateTimeField()
    flag = models.IntegerField()