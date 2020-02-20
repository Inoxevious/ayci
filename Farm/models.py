from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class FarmProduce(models.Model):
    id = models.AutoField(primary_key=True)
    short_name =models.CharField(max_length=70)
    long_name =models.CharField(max_length=270)
    shortDescrip = models.CharField(max_length=270)
    current_market_avg_price = models.FloatField(default=0)
    number_of_markets = models.IntegerField(default=0)
    image = models.ImageField(upload_to='staticfiles/products/images')
    category =models.CharField(max_length=30, choices=(('Industrial', 'Industrial'), ('Consumption', 'Consumption')))


    def __str__(self):
        return self.short_name

class Farm(models.Model):
    id = models.AutoField(primary_key=True)
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    name =models.CharField(max_length=70)
    farm_produce  = models.ForeignKey(FarmProduce, on_delete=models.CASCADE)
    target_market = models.CharField(max_length=30, choices=(('Local', 'Local'), ('Export', 'Export'), ('LocalnExport', 'LocalnExport')))
    category =models.CharField(max_length=30, choices=(('Industrial', 'Industrial'), ('Consumption', 'Consumption')))
    processes = models.TextField()
    production_output = models.CharField(max_length =70)
    growth_size =models.CharField(max_length=70)
    address =models.TextField()
    location =models.CharField(max_length=30, choices=(('Rural', 'Rural'), ('Semiurban', 'Semiurban'), ('Urban', 'Urban')))
    number_employees =models.IntegerField()
    assets_total =models.IntegerField()
    prev_year_closing_balance =models.IntegerField()
    business_size =models.CharField(max_length =70)
    business_logo =models.ImageField(upload_to='staticfiles/business/logo')
    business_site_images =models.ImageField(upload_to='staticfiles/images')

    def __str__(self):
        return self.name
