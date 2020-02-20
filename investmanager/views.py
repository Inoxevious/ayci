from django.shortcuts import render
from Farm.models import Farm, FarmProduce
from investmanager.models import Product, ManufacturingCompany, BrandCompany, ProductComposition
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.db.models import Q
from account.models import AccountUser
from . import imports as imp
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def investmanager(request, user_id):
    extra_context = ''
    title = ''
    user = AccountUser.objects.get(user_id=user_id)
    print(user.user.username)

    pdata = Product.objects.filter(short_name__icontains='maize')
    fdata = Farm.objects.all()
    # fproduce = fdata.farm_produce
    for item in fdata:
        fp = item.farm_produce
        print(fp)
    prd = ProductComposition.objects.filter(Q(composition__icontains=fp))
    for item in prd:

        prd = item.product
    
    prddata = Product.objects.filter(short_name__icontains=prd)
        

    cdata = loans.objects.all()
    testdata = 'New Clients'
    chart_data = log.grade_avg(cdata)

    extra_context = extra_context or {'chart_data': chart_data, "testdata": testdata, "user":user}
    return render(request, 'farmer/home.html', extra_context )

def importer(request):
    opfile = ''
    imp.get_data(opfile)
    return render(request, 'test.html')