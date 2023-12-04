from rest_framework.response import Response
from rest_framework import status
from ..models.author import Author
from ..serializers import AuthorSerializer


def get_authors_api(request):
    queryset = Author.objects.all()
    serializer = AuthorSerializer(queryset, many=True)

    return Response(serializer.data)


def get_author_api(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response({"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = AuthorSerializer(author)
    return Response(serializer.data)


def create_author_api(request):
    serializer = AuthorSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update_author_api(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response({"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = AuthorSerializer(author, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_author_api(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response({"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)

    author.delete()
    return Response(
        {"message": "Author deleted successfully"}, status=status.HTTP_204_NO_CONTENT
    )
