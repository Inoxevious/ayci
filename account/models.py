from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Role(models.Model):
    name = models.CharField(max_length=70)
    user_group = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=200)
    official_language = models.TextField()
    flag = models.ImageField(upload_to='static/images/countries/flags')
    longi = models.TextField(blank=True)
    lat = models.TextField(blank=True)   

# Create your models here.
class AccountUser(models.Model):
    role = models.CharField(null=True ,blank=True, max_length=70)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    writer = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    country = models.CharField(null=True ,blank=True, max_length=70)
    address =models.TextField(null=True ,blank=True )
    date_birth =models.DateField(null=True ,blank=True )
    phone =models.CharField(null=True ,blank=True, max_length=70)
    email =models.CharField(null=True ,blank=True, max_length=70)
    id_number =models.CharField(null=True ,blank=True, max_length=20)
    gender =models.CharField(null=True ,blank=True, max_length=20,  choices=(('Male', 'Male'), ('Female', 'Female')))
    education_level =models.CharField(null=True ,blank=True, max_length=70, choices=(('Graduate', 'Graduated'), ('Not_Graduate', 'Not_Graduate')))
    marital_status =models.CharField(null=True ,blank=True, max_length=20,  choices=(('Yes', 'Yes'), ('No', 'No')))
    number_dependants =models.IntegerField(null=True ,blank=True )
    total_worth =models.IntegerField(null=True ,blank=True )
    profile_pic = models.ImageField(null=True ,blank=True, upload_to='staticfiles/images')
    

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        AccountUser.objects.create(user=instance)
    instance.accountuser.save()