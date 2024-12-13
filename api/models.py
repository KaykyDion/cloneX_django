from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Title", max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updatedAt = models.DateTimeField(auto_now=True, null=False, blank=False)

    class Meta:
        ordering = ["-created_at"]