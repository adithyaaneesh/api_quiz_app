from django.urls import path
from . import views
urlpatterns = [
    path('api/get_quiz',views.get_quiz),
    path('api/create_quiz',views.create_quiz),
    path('api/delete-all/', views.delete_all_quizzes),
    path('api/delete/<int:id>',views.delete_quiz),
    path('api/update/<int:id>', views.update_quiz),

]