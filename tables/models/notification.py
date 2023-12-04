from django.db import models
from django.contrib.auth.models import User
from .item import Item
from uuid import uuid4


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    content = models.CharField(max_length=255, default="this is a title")
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # ---- relations ----
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )

    def __str__(self):
        return self.text  # representation on the DB

    class Meta:
        ordering = ["content"]
