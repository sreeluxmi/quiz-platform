#django
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

#local
from quiz.models import Quiz, Submission
from quiz.serializers import QuizSerializer
from ..serializers import SubmissionCreateSerializer, SubmissionHistorySerializer


class ActiveQuizListView(generics.ListAPIView):
    queryset = Quiz.objects.filter(is_active=True)
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]


# Attempt a quiz by submitting answers
class SubmissionCreateView(generics.CreateAPIView):
    serializer_class = SubmissionCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}
    

class SubmissionHistoryView(generics.ListAPIView):
    serializer_class = SubmissionHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Submission.objects.filter(user=self.request.user).order_by('-submitted_at')