from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from account.models import AccountUser

# Create your models here.

class Machinery(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='staticfiles/machinery/images')
    name = models.TextField()
    description = models.TextField()
    current_market_value = models.FloatField()
    supplier = models.CharField(max_length=70)
    manufacturingcompany = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class RawMaterials(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='staticfiles/rawmaterials/images')
    name = models.TextField()
    description = models.TextField()
    current_market_value = models.FloatField()

    def __str__(self):
        return self.name


class Proces(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    description = models.TextField()
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE)
    machines_used = models.TextField()
    rawmaterials = models.ForeignKey(RawMaterials, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ManufacturingCompany(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name =models.CharField(max_length=70)
    target_market = models.CharField(max_length=30, choices=(('Local', 'Local'), ('Export', 'Export'), ('LocalnExport', 'LocalnExport')))
    category =models.CharField(max_length=30, choices=(('Industrial', 'Industrial'), ('Consumption', 'Consumption')))
    processe = models.CharField(max_length=70)
    products  = models.CharField(max_length=70)
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

class BrandCompany(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name =models.CharField(max_length=70)
    products  = models.CharField(max_length=70)
    target_market = models.CharField(max_length=30, choices=(('Local', 'Local'), ('Export', 'Export'), ('LocalnExport', 'LocalnExport')))
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

class FoodGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    brandcompany = models.ForeignKey(BrandCompany, on_delete=models.CASCADE)
    current_market_avg_price = models.FloatField()
    number_of_markets = models.IntegerField(default=0,)
    image = models.ImageField(upload_to='staticfiles/products/images')
    short_name =models.CharField(max_length=70)
    long_name =models.CharField(max_length=270)
    shortDescrip = models.CharField(max_length=270)
    category = models.ForeignKey(FoodGroup, on_delete=models.CASCADE)
    manufacturingcompany = models.ForeignKey(ManufacturingCompany, on_delete=models.CASCADE)

    def __str__(self):
        return self.short_name

class ProductComposition(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    composition = models.TextField()

    def __str__(self):
        return self.product.short_name

class loans(models.Model):
    id = models.AutoField(primary_key=True)
    loan_amount = models.IntegerField()
    funded_amount = models.IntegerField()
    term = models.CharField(max_length=25)
    int_rate = models.CharField(max_length=8)
    installment = models.FloatField()
    grade = models.CharField(max_length=2)
    sub_grade = models.CharField(max_length=2)
    emp_title = models.CharField(max_length=40, default='NA')
    emp_length = models.CharField(max_length=20)
    home_owner = models.CharField(max_length=40)
    annual_inc = models.FloatField()     
    verification_status = models.CharField(max_length=40)
    loan_status = models.CharField(max_length=40)
    purpose = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    zip = models.CharField(max_length=6)
    state = models.CharField(max_length=3)
    dti = models.FloatField()
    open_acc = models.IntegerField()
    revol_bal = models.IntegerField()
    revolv_util = models.CharField(max_length=10)
    total_acct = models.IntegerField()
    application_type = models.CharField(max_length=25)
    total_cur_bal = models.IntegerField()
    acc_open_past_24 = models.IntegerField()
    avg_cur_bal = models.IntegerField()
    bc_open_to_buy = models.IntegerField()
    tot_hi_cred = models.IntegerField()
    total_bal_ex_mort = models.IntegerField()
    total_bc_limit = models.IntegerField()
    total_il_high_cred = models.IntegerField()
