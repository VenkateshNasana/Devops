from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TeamViewSet, ProjectMemberViewSet, EnvironmentViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'members', ProjectMemberViewSet, basename='projectmember')
router.register(r'environments', EnvironmentViewSet, basename='environment')

urlpatterns = [
    path('', include(router.urls)),
]
