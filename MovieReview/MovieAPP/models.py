from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie:allmovbycat', args=[self.slug])

    def __str__(self):
        return self.name

class Movies(models.Model):
    Movie_Title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    Description = models.TextField(blank=True)
    Poster = models.ImageField(upload_to='product', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Actors = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Release_date = models.DateField(default=timezone.now)
    youtube_link = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Movie_Title)
        super(Movies, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie:allproddetail', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ('Movie_Title',)
        verbose_name = 'Movies'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.Movie_Title