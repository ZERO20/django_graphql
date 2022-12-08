from django.contrib import admin

from .models import Category, Movie


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
