from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from identity.permission import ActionBasedPermissions
from examquiz import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics,authentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .models import Exam,QuizSection,Topic,Question
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
# Create your views here.

'''
Create Quiz Api For Admin
'''
class QuizCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,ActionBasedPermissions)
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Exam.objects.all()
    serializer_class = serializers.ExamSerializer

'''
Create Api For getting Exam Wise Section and Topic Name 
'''
class ExamListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Exam.objects.all()
    serializer_class = serializers.ExamListSerializer



''' Student Quiz Take'''
@csrf_exempt
def take_quiz(self,request, pk):
    print(self.request.user)
    quiz = get_object_or_404(Topic, pk=pk)
    student = request.user

    total_questions = quiz.questions.count()
    unanswered_questions = student.get_unanswered_questions(quiz)
    total_unanswered_questions = unanswered_questions.count()
    progress = 100 - round(((total_unanswered_questions - 1) / total_questions) * 100)
    question = unanswered_questions.first()

    if request.method == 'POST':
                student_answer.student = student
                student_answer.save()
                if student.get_unanswered_questions(quiz).exists():
                    return redirect('students:take_quiz', pk)
                else:
                    correct_answers = student.quiz_answers.filter(answer__question__quiz=quiz, answer__is_correct=True).count()
                    score = round((correct_answers / total_questions) * 100.0, 2)
                    TakenQuiz.objects.create(student=student, quiz=quiz, score=score)
                    if score < 50.0:
                        messages.warning(request, 'Better luck next time! Your score for the quiz %s was %s.' % (quiz.name, score))
                    else:
                        messages.success(request, 'Congratulations! You completed the quiz %s with success! You scored %s points.' % (quiz.name, score))
                    return redirect('students:quiz_list')
    else:
        form = TakeQuizForm(question=question)

    return Response ({
        'quiz': quiz,
        'question': question,
        'form': form,
        'progress': progress
    })