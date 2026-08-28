from django.contrib import admin
from .models import Deployment

@admin.register(Deployment)
class DeploymentAdmin(admin.ModelAdmin):
    list_display = ('project', 'environment', 'version', 'strategy', 'status', 'started_at')
    list_filter = ('status', 'strategy', 'environment')
    search_fields = ('version', 'commit_sha')
