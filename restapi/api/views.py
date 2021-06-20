from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from requests import Response
from rest_framework import viewsets, status, filters, generics
from rest_framework.views import APIView

from .filters import DynamicSearchFilter
from .models import Book, Author
from .serializers import BooksSerializer, BooksPublishedDateSerializer, AuthorsSerializer, ExternalDataSerializer


# Create your views here.

class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('published_date'):
            return ['published_date']
        elif request.query_params.get('author'):
            return ['authors__name']
        return super(CustomSearchFilter, self).get_search_fields(view, request)


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Book.objects.all()
    lookup_field = "bookid"
    filter_backends = (filters.OrderingFilter, CustomSearchFilter)
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ["author__name"]
    filter_fields = ("published_date", "bookid", "title")
    ordering_fields = ("published_date",)
    search_fields = ("author__name", "published_date", "^title")


class QuestionsAPIView(generics.ListCreateAPIView):
    filter_backends = (DynamicSearchFilter,)
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
