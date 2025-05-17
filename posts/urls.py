# posts/urls.py
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, UserViewSet


router = SimpleRouter()
router.register('users', UserViewSet, basename='users') # new
router.register('', PostViewSet, basename='posts') #new

urlpatterns = router.urls