from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from account.models import AccountUser
# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d",blank = True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20,blank = True)
    is_member = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default = datetime.now,blank = True)
    def __str__(self):
        return self.user.username


class Article(models.Model):
    author  = models.ForeignKey(AccountUser,on_delete = models.DO_NOTHING)
    title = models.CharField(max_length = 200)
    summary = models.TextField(blank=True)
    description = models.TextField(blank=True)
    category =models.CharField(max_length=30, choices=(  ('Communication', 'Communication'),('Business', 'Business'), ('Civil', 'Civil') , ('Policies', 'Policies'), ('Climate', 'Climate')))
    photo_main = models.ImageField(upload_to = 'articles/photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to = 'articles/photos/%Y/%m/%d/',blank =True)
    photo_2 = models.ImageField(upload_to = 'articles/photos/%Y/%m/%d/',blank =True)
    photo_3 = models.ImageField(upload_to = 'articles/photos/%Y/%m/%d/',blank =True)
    photo_4 = models.ImageField(upload_to = 'articles/photos/%Y/%m/%d/',blank =True)
    photo_5 = models.ImageField(upload_to = 'articles/photos/%Y/%m/%d/',blank =True)
    photo_6 = models.ImageField(upload_to = 'articles/photos/%Y/%m/%d/',blank =True)
    is_published = models.BooleanField(default=False)
    pub_date = models.DateField(default = datetime.now,blank = True)
    def __str__(self):
        return self.title

class Gallery(models.Model):
    author  = models.ForeignKey(Author,on_delete = models.DO_NOTHING)
    title = models.CharField(max_length = 200)
    description = models.TextField(blank=True)
    category =models.CharField(max_length=30, choices=( ('video', 'video'), ('banner', 'banner'),('thumbs', 'thumbs'), ('events', 'events') , ('ads', 'ads'), ('products', 'products')))
    photo_main = models.ImageField(upload_to = 'articles/photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to = 'articles/photos/%Y/%m/%d/',blank =True)
    photo_2 = models.ImageField(upload_to = 'articles/photos/%Y/%m/%d/',blank =True)
    photo_3 = models.ImageField(upload_to = 'articles/photos/%Y/%m/%d/',blank =True)
    photo_4 = models.ImageField(upload_to = 'articles/photos/%Y/%m/%d/',blank =True)
    photo_5 = models.ImageField(upload_to = 'articles/photos/%Y/%m/%d/',blank =True)
    photo_6 = models.ImageField(upload_to = 'articles/photos/%Y/%m/%d/',blank =True)
    video = models.FileField(upload_to = 'articles/videos/%Y/%m/%d/',blank =True)
    is_published = models.BooleanField(default=False)
    pub_date = models.DateField(default = datetime.now,blank = True)
    def __str__(self):
        return self.title   

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.DO_NOTHING)
    commentor_name = models.CharField(max_length=256, blank=True, null=True)
    commentor_email = models.CharField(max_length=256, blank=True, null=True)
    comment = models.TextField(blank=True)
    is_member = models.BooleanField(default=False)
    comment_date = models.DateTimeField(default = datetime.now,blank = True)
    pub_date = models.DateField(default = datetime.now,blank = True)
    likes = models.IntegerField(default=0)
    diss = models.IntegerField(default=0)
    def __str__(self):
        return self.comment