from django.contrib.auth.models import User
from rest_framework import viewsets, serializers

from polls.models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer

class QuestionViewSet(viewsets.ModelViewSet):
	serializer_class = QuestionSerializer
	queryset = Question.objects.all()


class ChoiceViewSet(viewsets.ModelViewSet):
	serializer_class = ChoiceSerializer
	queryset = Question.objects.all()