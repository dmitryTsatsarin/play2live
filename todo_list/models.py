from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    is_checked = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
