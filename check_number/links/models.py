from django.db import models


class Link(models.Model):
    number = models.CharField(max_length=15)
    found = models.BooleanField(default=True)
