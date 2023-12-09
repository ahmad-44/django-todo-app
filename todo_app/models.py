from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    is_Task_Completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __init__(self, title: str, desc: str, user_id: User, is_Task_Completed=False):
    #     self.title = title
    #     self.desc = desc
    #     self.user_id = user_id
    #     self.is_Task_Completed = is_Task_Completed
