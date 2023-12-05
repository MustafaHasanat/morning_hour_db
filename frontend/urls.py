from django.urls import path
from .views import HomeView, TablesView, CategoriesListView

urlpatterns = [
    path("", HomeView.as_view(), name="home.html"),
    path("tables/", TablesView.as_view(), name="tables.html"),
    path("categories/", CategoriesListView.as_view(), name="tables/categories.html"),
]
