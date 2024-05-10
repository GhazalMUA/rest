from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveSmallIntegerField()
    email=models.EmailField()
    
    def __str__(self):
        return self.name
    
    

class Cardio(models.Model):
    sport_name=models.CharField(max_length=100)
    callory_burning=models.SmallIntegerField()
    coach=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.sport_name    
    
    
class Question(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE , related_name='questions')
    slug=models.SlugField(max_length=200)
    
    def __str__(self):
        return f'{self.user} - {self.title[:20]}'
    
    
class Answer(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE , related_name='answers')
    body=models.TextField(max_length=300)
    created=models.DateTimeField(auto_now_add=True)
    question=models.ForeignKey(Question , on_delete=models.CASCADE , related_name='answers')
    
    def __str__(self):
        return f'{self.user} - {self.question.title}'