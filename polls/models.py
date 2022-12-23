import datetime # standard python datetime

from django.db import models
from django.utils import timezone # django shit

# CharField, DataTimeField are classes inheritedfrom Field
# there is no new in python, we simply do 
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# database uses the machine-friendly field name as column name
# pub_date has a human-friendly name passed as first argument

# max_length is required in CharField
# IntegerField argument named default is optional

# ———> from the models django creates database schemas (CREATE TABLE), and creates a database access api to access Question and Choice

# Each question has a set of choices
# in the shell we can do 
# q = Question.objects.get(pk=1)
# q.choice_set.all()
# q.choice_set.create(choice_text='Not much', votes=0)
# q.choice_set.create(choice_text='The sky', votes=0)
# q.choice_set.create(choice_text='Just hacking again', votes=0)
# q.choice_set.all()
# <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
# q.choice_set.count()
# 3


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    # __str__ methods useful in the CLI (python manage.py shell)
    # and in django’s admin
    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text