from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название:', widget=forms.TextInput(
        attrs={'class': 'form-control'}))  # label= то же самое что и verbose_name
    content = forms.CharField(label='Текст', required=False,
                              widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    is_published = forms.BooleanField(label='Опубликовано', initial=True)  # initial= значение по умолчанию
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
                                      empty_label='Выберите категорию',
                                      widget=forms.Select(attrs={'class': "form-control"}))
