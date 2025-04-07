from django.urls import path

#local
from .apis.auth import RegistrationView
from .apis.quiz import ActiveQuizListView, SubmissionCreateView, SubmissionHistoryView



urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('quizzes/active/', ActiveQuizListView.as_view(), name='active-quizzes'),
    path('quizzes/submit/', SubmissionCreateView.as_view(), name='submit-quiz'),
    path('submissions/history/', SubmissionHistoryView.as_view(), name='submission-history'),
]
