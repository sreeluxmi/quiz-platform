#django
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

#local
from ..serializers import CategorySerializer, QuizSerializer, QuestionSerializer
from users.permissions import IsAdmin
from ..models import Category, Quiz, Question


class CategoryViewSet(viewsets.ModelViewSet):
    print("-------------------------------------------------")
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated()]


    @action(detail=True, methods=['patch'], url_path='toggle-active')
    def toggle_active(self, request, pk=None):
        quiz = self.get_object()

        is_active = request.data.get('is_active')
        if is_active is not None:
            quiz.is_active = is_active
        else:
            quiz.is_active = not quiz.is_active

        quiz.save()
        return Response({
            "id": quiz.id,
            "title": quiz.title,
            "is_active": quiz.is_active
        }, status=status.HTTP_200_OK)


#creating question with options
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all() 
    serializer_class = QuestionSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated()]
    
    @action(detail=True, methods=['patch'], url_path='toggle-active')
    def toggle_active(self, request, pk=None):
        question = self.get_object()
        
        is_active = request.data.get('is_active')
        if is_active is not None:
            question.is_active = is_active
        else:
            question.is_active = not question.is_active
        
        question.save()
        return Response({'id': question.id, 'is_active': question.is_active}, status=status.HTTP_200_OK)