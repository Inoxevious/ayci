from django.db import models
from articles.models import Article


# Create your models here.
class SubItem(models.Model):

    name = models.CharField(max_length=256)
    article = models.ForeignKey(Article, on_delete = models.DO_NOTHING)
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    sub_items = models.ManyToManyField(SubItem)
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to = 'articles/photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    sub_menu = models.ManyToManyField(MenuItem)
    def __str__(self):
        return self.name
    
class SubMenu(models.Model):
    menu   = models.ForeignKey(Menu, on_delete = models.DO_NOTHING)
    name = models.CharField(max_length=265)

    def __str__(self):
        return self.name


    


