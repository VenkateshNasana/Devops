from django.db import models
from django.conf import settings

class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    repository_url = models.URLField(blank=True, null=True)
    repository_provider = models.CharField(max_length=50, blank=True, null=True)
    default_branch = models.CharField(max_length=50, default='main')
    project_status = models.CharField(max_length=50, default='ACTIVE')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

class ProjectMember(models.Model):
    class ProjectRole(models.TextChoices):
        OWNER = 'OWNER', 'Owner'
        MAINTAINER = 'MAINTAINER', 'Maintainer'
        DEVELOPER = 'DEVELOPER', 'Developer'
        VIEWER = 'VIEWER', 'Viewer'

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ProjectRole.choices, default=ProjectRole.VIEWER)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Environment(models.Model):
    class EnvType(models.TextChoices):
        DEV = 'DEV', 'Development'
        TEST = 'TEST', 'Testing'
        QA = 'QA', 'QA'
        STAGING = 'STAGING', 'Staging'
        PROD = 'PROD', 'Production'

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=EnvType.choices, default=EnvType.DEV)
    url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=50, default='ACTIVE')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='environments')
    deployment_strategy = models.CharField(max_length=50, default='Rolling')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.name} - {self.name}"
