from django.db import models
from projects.models import Project
from django.conf import settings

class Pipeline(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='pipelines')
    repository_url = models.URLField(blank=True, null=True)
    branch = models.CharField(max_length=100, default='main')
    configuration = models.JSONField(default=dict)
    status = models.CharField(max_length=50, default='ACTIVE')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.project.name} - {self.name}"

class PipelineExecution(models.Model):
    class ExecutionStatus(models.TextChoices):
        QUEUED = 'QUEUED', 'Queued'
        RUNNING = 'RUNNING', 'Running'
        SUCCESS = 'SUCCESS', 'Success'
        FAILED = 'FAILED', 'Failed'
        CANCELLED = 'CANCELLED', 'Cancelled'

    pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE, related_name='executions')
    status = models.CharField(max_length=20, choices=ExecutionStatus.choices, default=ExecutionStatus.QUEUED)
    logs = models.TextField(blank=True)
    duration_seconds = models.IntegerField(default=0)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.pipeline.name} - #{self.id} ({self.status})"
