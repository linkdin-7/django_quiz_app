from identity.models import User
from django.db import models

class Exam(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name


class QuizSection(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_quizzes')
    section = models.CharField(max_length=255)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return self.section

class Topic(models.Model):
    topic_name = models.CharField(max_length=255)
    section = models.ForeignKey(QuizSection, on_delete=models.CASCADE, related_name='sec_topic')

    def __str__(self):
        return self.topic_name

class Question(models.Model):

    def upload_image(self,filename):
        '''
        Generate a file path 
        for the image 
         '''
        ext = filename.split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join(f'items/{self.text}',filename)

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)
    ques_image = models.ImageField(upload_to=upload_image,blank=True,null=True)
    op1 = models.CharField(max_length=40, null =True)
    op2 = models.CharField(max_length=40, null =True)
    op3 = models.CharField(max_length=40, null =True)
    op4 = models.CharField(max_length=40, null =True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quiz = models.ManyToManyField(Question)

    def get_unanswered_questions(self, quiz):
        answered_questions = self.quiz_answers \
            .filter(answer__question__quiz=quiz) \
            .values_list('answer__question__pk', flat=True)
        questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
        return questions

    def __str__(self):
        return self.user.username


class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_answers')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')
