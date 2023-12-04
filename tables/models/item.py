from django.db import models
from .category import Category
from .author import Author
from uuid import uuid4


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255, default="this is a title")
    description = models.TextField(default="this is a description")
    primary_color = models.TextField(default="#000")
    old_price = models.PositiveIntegerField(default=0)
    current_price = models.PositiveIntegerField(default=0)
    is_best_selling = models.BooleanField(default=False)
    image = models.ImageField(upload_to="items/")

    # screenshots = models.ForeignKey(
    #     Screenshots, on_delete=models.CASCADE, related_name="items"
    # )

    # ---- relations ----
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="items"
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return self.title  # representation on the DB

    class Meta:
        ordering = ["title"]
