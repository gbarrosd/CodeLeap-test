from rest_framework.routers import SimpleRouter, DefaultRouter
from post.api.views import (
    CareersViewSet,
)

router = DefaultRouter(trailing_slash=False)

router.register(r"careers", CareersViewSet, basename='careers')