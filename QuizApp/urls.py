from django.urls import path
from . import views
urlpatterns = [
    path('api/get_quiz',views.get_quiz),
]