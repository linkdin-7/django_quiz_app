from . import views
from django.urls import include, path


urlpatterns = [
    path('quiz/create',views.QuizCreateAPIView.as_view()),
    path('quiz/list',views.ExamListAPIView.as_view()),
    path('quiz/<int:pk>/', views.take_quiz, name='take_quiz'),
    
]