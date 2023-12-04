from django.db import models
from django.contrib.auth.models import User
from .item import Item
from uuid import uuid4


class Review(models.Model):
    RATING_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    text = models.CharField(max_length=255, default="this is a title")
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=3,
    )

    # ---- relations ----
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return self.text  # representation on the DB

    class Meta:
        ordering = ["text"]
