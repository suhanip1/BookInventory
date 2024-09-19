from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
import csv
from .models import Inventory
from .serializers import InventorySerializer
from django.shortcuts import render
from rest_framework.permissions import AllowAny

def inventory_view(request):
    return render(request, 'inventory.html')

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def inventory_list_create(request):
    if request.method == 'GET':
        title = request.GET.get('title', None)
        author = request.GET.get('author', None)
        genre = request.GET.get('genre', None)
        publication_date = request.GET.get('publication_date', None)

        books = Inventory.objects.all()

        if title:
            books = books.filter(title__icontains=title)
        if author:
            books = books.filter(author__icontains=author)
        if genre:
            books = books.filter(genre__icontains=genre)
        if publication_date:
            books = books.filter(publication_date=publication_date)

        serializer = InventorySerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def inventory_delete(request, pk):
    try:
        book = Inventory.objects.get(pk=pk)
        book.delete()
        return Response({"message": "Book deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    except Inventory.DoesNotExist:
        return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def export_books_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    writer = csv.writer(response)
    writer.writerow(['Entry ID', 'Title', 'Author', 'Genre', 'Publication Date', 'ISBN'])

    books = Inventory.objects.all()

    for book in books:
        writer.writerow([book.entry_id, book.title, book.author, book.genre, book.publication_date, book.isbn])

    return response
