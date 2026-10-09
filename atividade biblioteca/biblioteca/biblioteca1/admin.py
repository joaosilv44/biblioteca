from django.contrib import admin
from .models import Book, Author, Category

class BookInLine(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "year", "available")
    search_fields = ("title", "author__name")
    list_filter = ("available", "categories")
    filter_horizontal = ("categories",)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInLine]

admin.site.register(Category)