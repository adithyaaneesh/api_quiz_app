from django.db import models

# Create your models here.
class Quiz(models.Model):
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=100, null=False, blank=True)
    option2 = models.CharField(max_length=100, null=False, blank=True)
    option3 = models.CharField(max_length=100, null=False, blank=True)
    option4 = models.CharField(max_length=100, null=False, blank=True)
    answer = models.CharField(max_length=100, null=False, blank=True)