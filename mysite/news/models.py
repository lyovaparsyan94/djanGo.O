from django.db import models
from django.urls import reverse, reverse_lazy


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория') #related_name='get_news'#) #PROTECT-защита от удаления,
    views = models.IntegerField(default=0)
    # null=True чтобы с пустым полем можно было работать
    # "verbose_name позволяет, чтобы в админке данные поля назывались так, как удобно админу
    # 'Category' указывается строкой, так как она модель, которая создана после класса News, в противном случае ссылку
    # тоже можно разместить
    # related_name нужен чтобы переназначить sql set при обращениии к связанной модели"

    def get_absolute_url(self):
        return reverse_lazy('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = "Новости"
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')
    # db_index ставиться True для более быстрого поиска для этого поля

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"
        ordering = ['title']
