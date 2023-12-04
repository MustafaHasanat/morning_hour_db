from django.db import models
from uuid import uuid4


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255, default="this is a title")
    description = models.TextField(default="this is a description")
    image = models.ImageField(upload_to="categories/")


    def __str__(self):
        return self.title  # representation on the DB

    class Meta:
        ordering = ["title"]
