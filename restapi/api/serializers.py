from rest_framework import serializers
from .models import Book, Author, Category


# class MyPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
#
#     def to_representation(self, value):
#         return str(value)


class AuthorsSerializer(serializers.ModelSerializer):
    """
    Serializing all the authors
    """

    class Meta:
        model = Author
        fields = (
            "id",
            "name"
        )


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializing all the Categories
    """

    class Meta:
        model = Category
        fields = (
            "name",
        )


class BooksSerializer(serializers.ModelSerializer):
    # authors = MyPrimaryKeyRelatedField(many=True, queryset=Author.objects.all())
    # categories = MyPrimaryKeyRelatedField(queryset=Category.objects.all())
    authors = serializers.StringRelatedField(many=True, read_only=True)
    categories = serializers.StringRelatedField(read_only=True)

    # thumbnail = serializers.HyperlinkedRelatedField(read_only=True, view_name='thumbnail')

    class Meta:
        model = Book
        fields = (
            "pk",
            "title",
            "authors",
            "published_date",
            "categories",
            "average_rating",
            "ratings_count",
            "thumbnail",
            "bookid",
        )
        depth = 1


class BooksPublishedDateSerializer(serializers.Serializer):
    from_date = serializers.DateField()
    to_date = serializers.DateField()
