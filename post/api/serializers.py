from rest_framework import serializers
from django.db import transaction
from rest_framework import response, status
from post.models import (
    Post,
)

class PostListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ("id", "username", "created_datetime", "title", "content")
        depth = 1

class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("username", "title", "content")

class PostPatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("title", "content")