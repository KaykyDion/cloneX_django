from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Title", max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updatedAt = models.DateTimeField(auto_now=True, null=False, blank=False)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.DO_NOTHING, default=1)
    likes = models.ManyToManyField(User, related_name="post_like", blank=True)

    def like_amount(self):
        return self.likes.count()

    class Meta:
        ordering = ["-created_at"]