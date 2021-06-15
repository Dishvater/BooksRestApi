from django.contrib import admin
from .models import Author, Category, Book


# Register your models here.

# class BookInLine(admin.TabularInline):
#     model = Book
#     extra = 1
#
#
# class CathegoryListAdmin(admin.ModelAdmin):
#     inlines = (BookInLine,)


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
