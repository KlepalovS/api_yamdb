from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Настройка модели User в админке."""

    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'role',
        'bio',
    )
    search_fields = ('username', 'role',)
    list_filter = ('username',)
    empty_value_display = '-пусто-'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройка модели Category в админке."""

    list_display = ('pk', 'name', 'slug')
    search_fields = ('name', 'slug',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Настройка модели Genre в админке."""

    list_display = ('pk', 'name', 'slug')
    search_fields = ('name', 'slug',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    """Настройка модели Title в админке."""

    list_display = (
        'pk',
        'name',
        'year',
        'description',
        'category'
    )
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Настройка модели Review в админке."""

    list_display = ('pk', 'title', 'text', 'author', 'score', 'pub_date')
    search_fields = ('author', 'title', 'score')
    list_filter = ('pub_date', 'author', 'title')
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Настройка модели Comment в админке."""

    list_display = ('pk', 'author', 'text', 'review', 'pub_date')
    search_fields = ('author', 'title',)
    list_filter = ('pub_date', 'author',)
    empty_value_display = '-пусто-'
