from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    """members = models.IntegerField(default=0)"""
    """Lo de arriba se puede borrar"""
    created_at = models.DateTimeField(auto_now_add=True)