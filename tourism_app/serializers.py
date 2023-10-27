import io
from django.contrib.auth.models import User
from .models import Tourist, MountainPass, MountainCoords, Image, MountainLevel
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'password')


class TouristSerializer(serializers.ModelSerializer):
    person = UserSerializer()
    class Meta:
        model = Tourist
        fields = ('phone', 'otc', 'person')


# class WomanCategorySerializer(serializers.ModelSerializer):
#     category = CategorySerializer(many=True, read_only=True)
#     # category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#     class Meta:
#         model = Woman
#         fields = ('title', 'content', 'category')

#     def create(self, validated_data):
#         category_data = validated_data.pop('category')
#         category = Category.objects.create(**category_data)
#         woman = Woman.objects.create(category=category, **validated_data)
#         return woman


# class MountainPassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MountainPass
#         fields = '__all__'
