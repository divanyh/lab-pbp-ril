from django.db import models

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete = models.CASCADE,
    )
    date = models.CharField(max_length=30)
    title = models.CharField(max_length=255)
    description = models.TextField()