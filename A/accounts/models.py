from django.db import models

# Create your models here.
class Cardio(models.Model):
    sport_name=models.CharField(max_length=100)
    callory_burning=models.SmallIntegerField()
    coach=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.sport_name