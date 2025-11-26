from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import QuizSerializer 
from .models import Quiz
# Create your views here.

# get quiz
@api_view(['GET'])
def get_quiz(request):
    quiz_questions = Quiz.objects.all()
    serializer = QuizSerializer(quiz_questions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_quiz(request):
    is_many = isinstance(request.data, list)
    serializer = QuizSerializer(data =request.data, many = is_many)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# delete a quiz
@api_view(['DELETE'])
def delete_all_quizzes(request):
    Quiz.objects.all().delete()
    return Response({"message": "All quizzes deleted successfully"})

def delete_quiz(request, id):
    quiz = get_object_or_404(Quiz,id=id)
    quiz.delete()
    return Response({"message": "Quiz deleted successfully"})

@api_view(['PUT'])
def update_quiz(request, id):
    quiz = Quiz.objects.get(id=id)
    serializer = QuizSerializer(instance=quiz, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
