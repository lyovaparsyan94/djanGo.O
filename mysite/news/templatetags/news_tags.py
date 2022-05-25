from django import template
# создаем простые теги
from news.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    """объект создается ради избегания кода, в противном случае в в .views нужно было писать news = News.objects.all()
    после этого в news.html данную функцию импортируем как свой тег и переименовываем с помощью 'as categories', т.е сокращается кол-во строк кода """
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='Hello', arg2='Word'):
    categories = Category.objects.all()
    return {'categories': categories, 'arg1':arg1, 'arg2':arg2}