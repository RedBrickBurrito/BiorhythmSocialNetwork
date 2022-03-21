from django.db import models
from user.models import CustomUser


class Event(models.Model):
    title = models.CharField(max_length=100, default=None)
    birthday = models.DateField(null=True, blank=False)
    customUser = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
