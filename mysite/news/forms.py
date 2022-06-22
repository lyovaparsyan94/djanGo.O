from django import forms
from .models import Category, News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя',
                               help_text='Имя пользователя должно состоять максимум из 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'username': forms.EmailField(attrs={'class': 'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }


#         плохо получается настраивать поля поэтому закомментируем и будем настраивать в самом классе UserRegisterForm

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

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title
