from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import News, Category
from .forms import ContactForm


def news_list(request):
    news_list = News.published.all().order_by('-publish_time')
    categories = Category.objects.all()
    # news_list  = News.objects.filter(status = News.Status.Published)
    context = {
        'news_list': news_list,
        'categories':categories
    }

    return render(request, 'news/news_list.html', context=context)


def news_detail(request, news ):
    news = get_object_or_404(News, slug=news, status = News.Status.Published )

    context = {
        'news' : news
    }


    return render(request, 'news/news_detail.html', context = context)


# this is with using the funcktion
def homePageView(request):
    categories = Category.objects.all()
    news = News.published.all().order_by('-publish_time')[:15]
    sport_news = News.published.all().filter(category__name='Sport')
    main_news = News.published.all().order_by('-publish_time')[:1]
    latest_news = News.published.all().order_by('-publish_time')[1:5]
    jahon = News.published.all().filter(category__name='Jahon habarlari')

    context = {
        'news' :news,
        'categiories' : categories,
        'sport_news' : sport_news,
        'main_news' : main_news,
        'latest_news' : latest_news,
        'jahon': jahon,
    }

    return  render(request, 'news/index.html', context = context)

# it is the end of the function


# This is written with class
class HomePageView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categiories'] = Category.objects.all()
        context['news'] = News.published.all().order_by('-publish_time')[:15]
        context['sport_news'] =  News.published.all().filter(category__name='Sport')
        context['main_news'] = News.published.all().order_by('-publish_time')[:1]
        context['latest_news'] =  News.published.all().order_by('-publish_time')[1:5]
        context['uzb_news'] = News.published.all().filter(category__name='Uzbekiston')
        context['jahon'] = News.published.all().filter(category__name='Jahon habarlari').order_by('-publish_time')[:4]
        context['jamiyat'] = News.published.all().filter(category__name='Jamiyat')
        context['all_news'] = News.published.all()

        return context



class SportnewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = News.published.all().filter(category__name='Sport')
        return news


class UzbnewsView(ListView):
    model = News
    template_name = 'news/uzbekistanNews.html'
    context_object_name = 'uzb_news'

    def get_queryset(self):
        news = News.published.all().filter(category__name='Uzbekiston')
        return news

class JahonNewsView(ListView):
    model = News
    template_name = 'news/jahon.html'
    context_object_name = 'jahon'

    def get_queryset(self):
        news = News.published.all().filter(category__name='Jahon habarlari')
        return news

class LocalNewsView(ListView):
    model = News
    template_name = 'news/jamiyat.html'
    context_object_name = 'jamiyat'

    def get_queryset(self):
        news = News.published.all().filter(category__name='Jamiyat')
        return news


class AllNewsView(ListView):
    model = News
    template_name = 'news/all_news.html'
    context_object_name = 'all_news'

    def get_queryset(self):
        news = News.published.all()
        return news

def contactPageView(request):

    context = {}

    return render(request, 'news/Contact_us.html', context = context)

def blogPageView(request):

    context = {}

    return render(request, 'news/blog.html', context = context)

def singlePageView(request):

    context = {}

    return render(request, 'news/single.html', context=context)


def contactPageView(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('news:contact_thank_you')  # Redirect to the 'contact_thank_you' URL
        else:
            print(form.errors)  # Print errors for debugging

    context = {
        'form': form
    }
    return render(request, 'news/contact_us.html', context)


def contact_thank_you(request):
    return render(request, 'news/thank_you.html')