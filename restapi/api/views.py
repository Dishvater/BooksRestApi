from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, filters, generics

from .filters import DynamicSearchFilter
from .models import Book
from .serializers import BooksSerializer, BooksPublishedDateSerializer


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
    filter_fields = ("published_date", "bookid")
    ordering_fields = ("published_date",)
    search_fields = ("authors__name", "published_date")
    #
    # def book_by_id(self, bookid):
    #     queryset = Book.object.get(bookid=bookid)
    #     return queryset


#
# class BookByIdViewSet(viewsets.ModelViewSet):
#     serializer_class = BooksSerializer
#
#     def get_queryset(self):
#         queryset = Book.objects.filter(bookid=bookid)
#         return Book.objects.filter(bookid=bookid)


class QuestionsAPIView(generics.ListCreateAPIView):
    filter_backends = (DynamicSearchFilter,)
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
