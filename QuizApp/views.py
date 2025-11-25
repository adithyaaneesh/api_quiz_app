from django.shortcuts import get_object_or_404
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


@api_view(['POST'])
def create_quiz(request):
    quizzes = request.data
    
    if not isinstance(quizzes, list):
        return Response({"error": "Input must be a list of quizzes"})

    for quiz_data in quizzes:
        question = quiz_data.get("question")
        options = quiz_data.get("options", [])

        if not question:
            return Response({"error": "Question Required"})

        quiz = Quiz.objects.create(question=question)

        for opt in options:
            Option.objects.create(
                quiz=quiz,
                text=opt.get("text", ""),
                is_correct=opt.get("is_correct", False)
            )

    return Response({"message": "All quizzes created successfully"})


# delete a quiz
@api_view(['DELETE'])
def delete_all_quizzes(request):
    Quiz.objects.all().delete()
    return Response({"message": "All quizzes deleted successfully"})