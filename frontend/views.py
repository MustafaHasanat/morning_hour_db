from django.views.generic import TemplateView, ListView
from tables.models.category import Category


class HomeView(TemplateView):
    template_name = "home.html"


class TablesView(TemplateView):
    template_name = "tables.html"


class CategoriesView(TemplateView):
    template_name = "tables/categories.html"


class CategoriesListView(ListView):
    model = Category
    template_name = "tables/categories.html"
    context_object_name = "categories_list"