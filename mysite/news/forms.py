from django import forms
from .models import Category, News


# class NewsForm(forms.Form):
# в целях избежания дублирования кода данный споосб определения атрибутов класса неэффективен
# title = forms.CharField(max_length=150, label='Название:', widget=forms.TextInput(
#     attrs={'class': 'form-control'}))  # label= то же самое что и verbose_name
# content = forms.CharField(label='Текст', required=False,
#                           widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
# is_published = forms.BooleanField(label='Опубликовано', initial=True)  # initial= значение по умолчанию
# category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
#                                   empty_label='Выберите категорию',
#                                   widget=forms.Select(attrs={'class': "form-control"}))

class NewsForm(forms.ModelForm):
    class Meta:
        """ Указываем модель от которой наследируется форма, и пола которые нужно отображать, эффективнее чем пример выше"""
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }
