from django.db import models


class IpStorage(models.Model):
    ip = models.CharField(max_length = 30)
    created = models.DateTimeField(auto_now_add = True)
    user_agent = models.CharField(max_length = 200, null=True)