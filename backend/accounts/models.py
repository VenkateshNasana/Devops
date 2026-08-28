from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    DEVOPS_ENGINEER = 'DEVOPS_ENGINEER', 'DevOps Engineer'
    DEVELOPER = 'DEVELOPER', 'Developer'
    PROJECT_MANAGER = 'PROJECT_MANAGER', 'Project Manager'
    VIEWER = 'VIEWER', 'Viewer'

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.VIEWER)
    avatar = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=20, default='ACTIVE')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
