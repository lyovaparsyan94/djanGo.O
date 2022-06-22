from django.urls import path
from django.contrib.auth.mixins import LoginRequiredMixin
from .views import *

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('news/add_news/', add_news, name='add_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
    # """атрибут name позволяет задать для Джанго соответств. имя  c помощью тега url для маршрута, для динамичности
    # если например название category поменять на cat, достаточно лишь в name указать новое имя
    # это имя используется также в построение get_absolute_url в Категориях"""
    path('test/', test, name='test')

]
