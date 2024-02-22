from rest_framework import permissions, viewsets, mixins, filters, status, response, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from post.api.mixins import GetSerializerClassMixin

from post.api.serializers import (
    PostListSerializer,
    PostCreateSerializer,
    PostPatchSerializer,
)
from post.models import (
    Post,
)

class CareersViewSet(
    GetSerializerClassMixin,
    viewsets.ModelViewSet
):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    serializer_action_classes = {
        "partial_update": PostPatchSerializer,
        "create": PostCreateSerializer,
    }
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = {
        "created_datetime": ['gte', 'lte'], 
    }
    search_fields = ["title", "content", "username"]