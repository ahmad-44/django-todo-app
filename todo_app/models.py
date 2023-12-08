from django.db import models
from django.contrib.auth.models import User, UserManager


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    is_Task_Completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
