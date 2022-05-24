from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    # """атрибут name позволяет задать для Джанго соответств. имя  c помощью тега url для маршрута, для динамичности
    # если например название category поменять на cat, достаточно лишь в name указать новое имя"""

]