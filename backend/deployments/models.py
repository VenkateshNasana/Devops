from django.db import models
from projects.models import Project, Environment
from django.conf import settings

class Deployment(models.Model):
    class DeploymentStrategy(models.TextChoices):
        ROLLING = 'ROLLING', 'Rolling'
        BLUE_GREEN = 'BLUE_GREEN', 'Blue-Green'
        CANARY = 'CANARY', 'Canary'
        RECREATE = 'RECREATE', 'Recreate'

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='deployments')
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    version = models.CharField(max_length=50)
    commit_sha = models.CharField(max_length=40)
    strategy = models.CharField(max_length=20, choices=DeploymentStrategy.choices, default=DeploymentStrategy.ROLLING)
    status = models.CharField(max_length=20, default='PENDING')
    deployed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    logs = models.TextField(blank=True)

    def __str__(self):
        return f"{self.project.name} - {self.version} to {self.environment.name}"
