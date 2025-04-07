from django.urls import path, include
from rest_framework.routers import DefaultRouter

#local
from .api.quiz import CategoryViewSet, QuizViewSet, QuestionViewSet


router = DefaultRouter()
router.register('categories', CategoryViewSet, basename="categories")
router.register('quizzes', QuizViewSet, basename="quizzes")
router.register('questions', QuestionViewSet, basename="questions")

urlpatterns = [
    path('api/', include(router.urls)),
]