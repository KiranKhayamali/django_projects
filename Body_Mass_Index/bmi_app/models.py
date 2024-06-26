from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BMIHistory(models.Model):
    user = User.ForeignKey(User, on_delete = models.CASCADE)
    bmi = models.FloatField()
    date = models.DateTimeField(auto_now_add = True)

def __str__(self):
    return (f'{self.user.username} - {self.date}')
