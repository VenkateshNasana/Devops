from django.db import models
from projects.models import Environment

class Server(models.Model):
    hostname = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE, related_name='servers')
    operating_system = models.CharField(max_length=100)
    cpu = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    disk = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default='RUNNING')
    provider = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hostname} ({self.ip_address})"

class Container(models.Model):
    class ContainerStatus(models.TextChoices):
        RUNNING = 'RUNNING', 'Running'
        STOPPED = 'STOPPED', 'Stopped'
        FAILED = 'FAILED', 'Failed'
        RESTARTING = 'RESTARTING', 'Restarting'
        UNKNOWN = 'UNKNOWN', 'Unknown'

    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    tag = models.CharField(max_length=100, default='latest')
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE, related_name='containers')
    status = models.CharField(max_length=20, choices=ContainerStatus.choices, default=ContainerStatus.UNKNOWN)
    port = models.IntegerField(blank=True, null=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='hosted_containers', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}:{self.tag}"
