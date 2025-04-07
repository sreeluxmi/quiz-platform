#django
from rest_framework import serializers

#local
from .models import Category


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = "__all__"