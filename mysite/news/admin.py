from django.contrib import admin

# пока модель не будет импортирована, она не отобразится в админке.
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    # "в данном атрибуте класса указывается те параметры, которые будут отображаться в админке, но для этого их" \
    # "нужно зарегистрировать в admin.site.register(News). Порядок важен! "

    list_display_links = ('id', 'title')
    # "список полей, который должны юыть с ссылками на модели(новости)"

    search_fields = ('title', 'content')
    # "Добавляет поле для поиска, аргументы для того, чтобы указать по каким полям выпонлять поиск, регистры нужно обработать"

    list_editable = ('is_published',)
    # "позволяет в админке редактировать категорию, ЗАпятая важна после кортежа"

    list_filter = ('is_published', 'category')
    # "позволяет в админке фильтровать по указанному полю"

    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', "views", 'created_at', "updated_at")
    # """список полей для нашей категорий, далее в следующем атрибуте указываем, какие поля являются НЕредкатируемыми"""

    readonly_fields = ("get_photo", "views", 'created_at', "updated_at",)
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return "-"

    get_photo.short_description = 'Миниатюра'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)  # кортеж из одного элемента, нужно поставить запятую чтобы укзаать, что это не строка


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
