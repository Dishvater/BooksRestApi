from django.db import models


# from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=512, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=256)
    authors = models.ManyToManyField(Author, null=True, blank=True)
    published_date = models.CharField(max_length=10, null=True)
    categories = models.ManyToManyField(Category, null=True, blank=True)
    average_rating = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    ratings_count = models.IntegerField(null=True, blank=True)
    thumbnail = models.CharField(max_length=256, null=True)
    bookid = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.title
