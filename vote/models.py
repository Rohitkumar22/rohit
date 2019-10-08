from django.db import models
from django.utils import timezone
# Create your models here.
class Food(models.Model):
    Question_txt=models.CharField(max_length=200)
    pub_dates=models.DateTimeField('Date publish',default=timezone.now)
    def __str__(self):
        return (self.Question_txt)

class Choice(models.Model):
    key=models.ForeignKey(Food,on_delete=models.CASCADE)
    choice_txt=models.CharField(max_length=20)
    count=models.IntegerField(default=0)
    def __str__(self):
        return (self.choice_txt)

class Price(models.Model):
    key=models.ForeignKey(Food,on_delete=models.CASCADE)
    rupees=models.IntegerField(default=0)
    dollar=models.IntegerField(default=0)
    def __str__(self):
        return (self.rupees)
