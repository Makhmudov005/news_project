from django.urls import path
from .views import news_list, news_detail, homePageView, contactPageView, blogPageView, singlePageView, HomePageView, \
    UzbnewsView, JahonNewsView, LocalNewsView, SportnewsView, AllNewsView
from django.views.generic import TemplateView

app_name = 'news'

urlpatterns = [
    path('news/', news_list, name='all_news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('', HomePageView.as_view(), name='home_page'),
    path('contact-us/', contactPageView, name='contact_page'),
    path('blog/', blogPageView, name='blog_page'),
    path('single/', singlePageView, name='single_page'),
    path('thank-you/', TemplateView.as_view(template_name='news/thank_you.html'), name='contact_thank_you'),
    path('uzbnews/', UzbnewsView.as_view(), name='uzb_news_page'),
    path('foreign/', JahonNewsView.as_view(), name='foreign_news_page'),
    path('localnews/', LocalNewsView.as_view(), name='local_news_page'),
    path('sportnews/', SportnewsView.as_view(), name='sport_news_page'),
    path('all/', AllNewsView.as_view(), name='all_news_list')
]
