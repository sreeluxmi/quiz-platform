#django
from django.shortcuts import get_object_or_404
from rest_framework import serializers

#local
from .models import User
from quiz.models import Quiz, Question, Option, Submission, Answer



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'is_admin')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class AnswerSubmitSerializer(serializers.Serializer):
    question = serializers.IntegerField()
    selected_option = serializers.IntegerField()



class SubmissionCreateSerializer(serializers.ModelSerializer):
    answers = AnswerSubmitSerializer(many=True)

    class Meta:
        model = Submission
        fields = ['quiz', 'answers']

    def validate(self, data):
        quiz = get_object_or_404(Quiz, id=data['quiz'].id if isinstance(data['quiz'], Quiz) else data['quiz'], is_active=True)
        print("quiz inside vlaidate-------------------", quiz)
        for ans in data['answers']:
            question = get_object_or_404(Question, id=ans['question'], quiz=quiz, is_active=True)
            option = get_object_or_404(Option, id=ans['selected_option'], question=question)
        return data

    def create(self, validated_data):
        user = self.context['request'].user
        quiz = validated_data['quiz']
        answers_data = validated_data.pop('answers')
        score = 0

        submission = Submission.objects.create(user=user, quiz=quiz, score=0)

        for ans in answers_data:
            question = Question.objects.get(id=ans['question'])
            option = Option.objects.get(id=ans['selected_option'])

            if option.is_correct:
                score += 1

            Answer.objects.create(
                submission=submission,
                question=question,
                selected_option=option.id
            )

        submission.score = score
        submission.save()
        return submission

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "quiz": instance.quiz.id,
            "score": instance.score,
            "submitted_at": instance.submitted_at,
        }

    
class SubmissionHistorySerializer(serializers.ModelSerializer):
    quiz_title = serializers.CharField(source='quiz.title', read_only=True)

    class Meta:
        model = Submission
        fields = ['id', 'quiz_title', 'score', 'submitted_at']
