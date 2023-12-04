from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models.author import Author
from .serializers import AuthorSerializer
from .apis.authors import (
    get_authors_api,
    get_author_api,
    create_author_api,
    update_author_api,
    delete_author_api,
)
from .apis.categories import (
    get_categories_api,
    get_category_api,
    create_category_api,
    update_category_api,
    delete_category_api,
)


# ------------ authors ------------


@api_view(["GET"])
def get_authors(request):
    return get_authors_api(request)


@api_view(["GET"])
def get_author(request, pk):
    return get_author_api(request, pk)


@api_view(["POST"])
def create_author(request):
    return create_author_api(request)


@api_view(["PUT"])
def update_author(request, pk):
    return update_author_api(request, pk)


@api_view(["DELETE"])
def delete_author(request, pk):
    return delete_author_api(request, pk)


# ------------ categories ------------


@api_view(["GET"])
def get_categories(request):
    return get_categories_api(request)


@api_view(["GET"])
def get_category(request, pk):
    return get_category_api(request, pk)


@api_view(["POST"])
def create_category(request):
    return create_category_api(request)


@api_view(["PUT"])
def update_category(request, pk):
    return update_category_api(request, pk)


@api_view(["DELETE"])
def delete_category(request, pk):
    return delete_category_api(request, pk)
