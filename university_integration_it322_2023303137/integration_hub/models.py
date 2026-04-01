from django.db import models

class IntegrationLog(models.Model):
    source_system = models.CharField(max_length=100)
    target_system = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
