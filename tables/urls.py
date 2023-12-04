from django.urls import path
from .views import (
    get_authors,
    get_author,
    create_author,
    update_author,
    delete_author,
    get_categories,
    get_category,
    create_category,
    update_category,
    delete_category,
)

urlpatterns = [
    # authors
    path("get-authors", get_authors, name="get-authors"),
    path("get-author/<uuid:pk>", get_author, name="get-author"),
    path("create-author", create_author, name="create-author"),
    path("update-author/<uuid:pk>", update_author, name="update-author"),
    path("delete-author/<uuid:pk>", delete_author, name="delete-author"),
    # categories
    path("get-categories", get_categories, name="get-categories"),
    path("get-category/<uuid:pk>", get_category, name="get-category"),
    path("create-category", create_category, name="create-category"),
    path("update-category/<uuid:pk>", update_category, name="update-category"),
    path("delete-category/<uuid:pk>", delete_category, name="delete-category"),
]
