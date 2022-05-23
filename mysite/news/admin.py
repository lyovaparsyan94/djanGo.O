from django.contrib import admin

# пока модель не будет импортирована, она не отобразится в админке.
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    "в данном атрибуте класса указывается те параметры, которые будут отображаться в админке, но для этого их" \
    "нужно зарегистрировать в admin.site.register(News). Порядок важен! "

    list_display_links = ('id', 'title')
    "список полей, который должны юыть с ссылками на модели(новости)"

    search_fields = ('title', 'content')
    "Добавляет поле для поиска, аргументы для того, чтобы указать по каким полям выпонлять поиск, регистры нужно обработать"

    list_editable = ('is_published',)
    "позволяет в админке редактировать категорию, ЗАпятая важна после кортежа"

    list_filter = ('is_published', 'category')
    "позволяет в админке фильтровать по указанному полю"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)  # кортеж из одного элемента, нужно поставить запятую чтобы укзаать, что это не строка


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
