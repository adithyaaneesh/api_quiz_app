from django.db import models

# Create your models here.
class Quiz(models.Model):
    question = models.CharField(max_length=255)
    
class Option(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
