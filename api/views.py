from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from polls.models import Question
from api.serializers import QuestionSerializer
from api.serializers import ChoiceSerializer

class QuestionList(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer