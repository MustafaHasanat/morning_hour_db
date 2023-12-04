from django.db import models
from django.contrib.auth.models import User
from .item import Item
from uuid import uuid4


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # ---- relations ----
    users = models.ManyToManyField(User, related_name='orders')
    items = models.ManyToManyField(Item, related_name='orders')

    def __str__(self):
        return self.text  # representation on the DB

    class Meta:
        ordering = ["total_amount"]
