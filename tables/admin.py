from django.contrib import admin
from .models.item import Item
from .models.category import Category
from .models.author import Author
from .models.review import Review
from .models.notification import Notification
from .models.order import Order


@admin.register(Item)
class AdminItem(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "description",
        "primary_color",
        "old_price",
        "current_price",
        "is_best_selling",
        "image",
        "category",
        "author",
    ]
    search_fields = ("title",)


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "description",
        "image",
    ]
    search_fields = ("title",)


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "avatar",
    ]
    search_fields = ("name",)


@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    list_display = [
        "id",
        "text",
        "rating",
    ]
    search_fields = ("text",)


@admin.register(Notification)
class AdminNotification(admin.ModelAdmin):
    list_display = [
        "id",
        "content",
        "is_read",
        "created_at",
    ]
    search_fields = ("content",)


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = [
        "id",
        "total_amount",
        "created_at",
    ]
    search_fields = ("total_amount",)
