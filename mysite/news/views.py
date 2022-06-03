from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    """определяем модель, из которой наследуем модель"""
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = "news"
    allow_empty = False

    # extra_context = {'title': 'Главная'} #это в случае статичных данных, если динамичные данные будут -> def get_context_data

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):  # для фильтрации, не нужно больше писать фильтры или news = News.objects.all()
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = "news"
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class ViewNews(DeleteView):
    model = News
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'
    # template_name = 'news/news_confirm_delete.html'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
#     на самом деле здесь Джанго ждет функцию, которую мы создали в models def get_absolute_url(self): или
#     success_url = reverse_lazy('home') делает редирект на домашнюю стр(но мы будем использовать(get_absolute_url)



# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})


# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {"news_item": news_item})


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             """после подключения наследования в формс.ру используем удобный метод news = form.save()"""
#             # print(form.cleaned_data)
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
#Мы закомментировали эту функцию потому что всего 3 строки class CreateNews могут полностью заменить эту функцию

