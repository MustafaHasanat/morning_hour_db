from django.db import models
from uuid import uuid4


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, default="this is a name")
    avatar = models.ImageField(upload_to="authors/")
    brief = models.CharField(max_length=255, default="this is a brief")

    # ---- relations ----

    def __str__(self):
        return self.name  # representation on the DB

    class Meta:
        ordering = ["name"]
