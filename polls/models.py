import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Fretboard(models.Model):

    # User specifies the particular major scale they would like.
    scale = models.CharField(max_length=3)

    # User specifies the tuning of each string on their guitar.
    #Largest diameter string is string 1. A traditionally tunded guitar would be as follows 1=E, 2=A, 3=D, 4=G, 5=B, 6=E

    string1 = models.CharField(max_length=3)
    string2 = models.CharField(max_length=3)
    string3 = models.CharField(max_length=3)
    string4 = models.CharField(max_length=3)
    string5 = models.CharField(max_length=3)
    string6 = models.CharField(max_length=3)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text