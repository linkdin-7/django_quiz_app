# Importing Required Libraries
from .models import Exam,QuizSection,Topic,Question,Answer
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

'''
Creating a Answer for Each question serializer
'''
class AnswerSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Answer
        fields = ['text']

'''Creating a Question serializer'''
class QuestionSerializer(WritableNestedModelSerializer):
    answers = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = ['text','ques_image','op1','op2','op3','op4','answers']


'''Creating a Topic serializer'''
class TopicSerializer(WritableNestedModelSerializer):
    questions = QuestionSerializer(many = True)
    class Meta:
        model = Topic
        fields = ['topic_name','questions']

'''Creating a Section'''
class QuizSectionSerializer(WritableNestedModelSerializer):
    sec_topic = TopicSerializer(many = True)
    class Meta:
        model = QuizSection
        fields=['owner','section','sec_topic']

''' Creating a Exam with section Serializer '''
class ExamSerializer(WritableNestedModelSerializer):
    quizzes = QuizSectionSerializer(many = True)
    class Meta:
        model = Exam
        fields = [
            'name','quizzes'
        ]

''' Creating a List of topics Serializer '''
class TopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['topic_name',]

'''Creating a Section List Serailizer'''
class QuizSectionListSerializer(serializers.ModelSerializer):
    sec_topic = TopicListSerializer(many = True)
    class Meta:
        model = QuizSection
        fields=['section','sec_topic']

''' Creating a Exam List of section and topics Serializer '''
class ExamListSerializer(serializers.ModelSerializer):
    quizzes = QuizSectionListSerializer(read_only = True,many = True)
    class Meta:
        model = Exam
        fields = [
            'name','quizzes'
        ]





