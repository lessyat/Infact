from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FactSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Fact
        fields = '__all__'
