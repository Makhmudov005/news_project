from django.db import models
from django.urls import reverse
from django.utils import timezone

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class News(models.Model):

    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now = True)
    status  = models.CharField(max_length=2,
                               choices=Status.choices,
                               default=Status.Draft
                               )

    objects = models.Manager() #default manager
    published = PublishedManager()

    class Meta:
         ordering  = ('-publish_time',)
       #bu kod orqali teskari tartiblashda chiqarib beradi masalan ohirgi
        # yangilik qoshilganda uni birinchi bolib korsatadi


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:news_detail_page', args=[self.slug])


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email

