from django.db import models
from projects.models import Project, Environment
from django.conf import settings

class HealthCheck(models.Model):
    class Status(models.TextChoices):
        HEALTHY = 'HEALTHY', 'Healthy'
        DEGRADED = 'DEGRADED', 'Degraded'
        DOWN = 'DOWN', 'Down'
        UNKNOWN = 'UNKNOWN', 'Unknown'

    target_url = models.URLField()
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.UNKNOWN)
    response_time_ms = models.IntegerField(null=True, blank=True)
    status_code = models.IntegerField(null=True, blank=True)
    error_message = models.TextField(blank=True)
    checked_at = models.DateTimeField(auto_now_add=True)

class Incident(models.Model):
    class Severity(models.TextChoices):
        LOW = 'LOW', 'Low'
        MEDIUM = 'MEDIUM', 'Medium'
        HIGH = 'HIGH', 'High'
        CRITICAL = 'CRITICAL', 'Critical'

    class Status(models.TextChoices):
        OPEN = 'OPEN', 'Open'
        INVESTIGATING = 'INVESTIGATING', 'Investigating'
        MITIGATED = 'MITIGATED', 'Mitigated'
        RESOLVED = 'RESOLVED', 'Resolved'

    title = models.CharField(max_length=255)
    description = models.TextField()
    severity = models.CharField(max_length=20, choices=Severity.choices, default=Severity.MEDIUM)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='incidents')
    environment = models.ForeignKey(Environment, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
