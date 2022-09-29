from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )
    date_created = models.DateField(default = date.today)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)