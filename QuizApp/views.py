from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import QuizSerializer 
from .models import Quiz, Option
# Create your views here.

# get quiz
@api_view(['GET'])
def get_quiz(request):
    quiz_questions = Quiz.objects.all()
    serializer = QuizSerializer(quiz_questions, many=True)
    return Response(serializer.data)

