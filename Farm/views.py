from django.shortcuts import render
from .models import Farm, FarmProduce
from investmanager import logic as log
from investmanager.models import Product, ManufacturingCompany, BrandCompany, ProductComposition, loans
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.db.models import Q
from account.models import AccountUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    user_id = request.user.id
    extra_context = ''
    title = ''
    fp = ''
    user = AccountUser.objects.get(user_id=user_id)
    account_user = Farm.objects.get(farmer_id = request.user.id)
    farm_produce = account_user.farm_produce
    cdata = loans.objects.all()
    testdata = 'Farms MArket Stocks'
    chart_data = log.grade_avg(cdata)

    extra_context = extra_context or {'chart_data': chart_data, "testdata": testdata, "user":user, "farm_produce":farm_produce}
    return render(request, 'farmer/home.html', extra_context )


def contacts(request):
    user_id = request.user.id
    extra_context = ''
    title = ''
    fp = ''
    user = AccountUser.objects.get(user_id=user_id)
    
    cdata = loans.objects.all()
    testdata = 'New Clients'
    chart_data = log.grade_avg(cdata)

    extra_context = extra_context or {'chart_data': chart_data, "testdata": testdata, "user":user}
    return render(request, 'farmer/contacts.html', extra_context )

def recommends(request):
    user_id = request.user.id
    extra_context = ''
    title = ''
    fp = ''
    user = AccountUser.objects.get(user_id=user_id)
    
    cdata = loans.objects.all()
    testdata = 'New Clients'
    chart_data = log.grade_avg(cdata)

    extra_context = extra_context or {'chart_data': chart_data, "testdata": testdata, "user":user}
    return render(request, 'farmer/recommends.html', extra_context )

def market_data(request):
    user_id = request.user.id
    extra_context = ''
    title = ''
    fp = ''
    user = AccountUser.objects.get(user_id=user_id)
    
    cdata = loans.objects.all()
    testdata = 'New Clients'
    chart_data = log.grade_avg(cdata)

    extra_context = extra_context or {'chart_data': chart_data, "testdata": testdata, "user":user}
    return render(request, 'farmer/market_data.html', extra_context )

def file_manager(request):
    
    extra_context = ''
    title = ''
    fp = ''
    user_id = request.user.id
    user = AccountUser.objects.get(user_id=user_id)
    
    cdata = loans.objects.all()
    testdata = 'New Clients'
    chart_data = log.grade_avg(cdata)

    extra_context = extra_context or {'chart_data': chart_data, "testdata": testdata, "user":user}
    return render(request, 'farmer/file_manager.html', extra_context )

def investors(request):
    user = request.user
    print(user.id)
    extra_context = ''
    title = ''
    fp = ''
    user_id = request.user.id
    user = AccountUser.objects.get(user_id=user_id)
    
    
    cdata = loans.objects.all()
    testdata = 'New Clients'
    chart_data = log.grade_avg(cdata)

    extra_context = extra_context or {'chart_data': chart_data, "testdata": testdata , "user":user}
    return render(request, 'farmer/investors.html', extra_context )

@login_required(login_url='/accounts/login/')
def farmer(request, user_id):
    extra_context = ''
    title = ''
    fp = ''
    user = AccountUser.objects.get(user_id=user_id)
    
    cdata = loans.objects.all()
    testdata = 'New Clients'
    chart_data = log.grade_avg(cdata)

    extra_context = extra_context or {'chart_data': chart_data, "testdata": testdata, "user":user}
    return render(request, 'farmer/home.html', extra_context )

    

def buyers(request):
    extra_context = ''
    chart_data = ''
    testdata = ''
    prddata = ''
    user = ''
    fp = ''
    user_id = request.user.id
    user = AccountUser.objects.get(user_id=user_id)

    # FIND POTENTIAL BUYERS BY QUERYING PRODUCE PROCESSORS
        # get farmer produce
    print('user id is:: ', request.user.id)

    account_user = Farm.objects.get(farmer_id = request.user.id)
    farm_produce = account_user.farm_produce
    fdata = Farm.objects.all()
    # fproduce = fdata.farm_produce
    for item in fdata:
        fp = item.farm_produce
        # print(fp)
    prd = ProductComposition.objects.filter(Q(composition__icontains=fp))
    for item in prd:

        prd = item.product
    
    prddata = Product.objects.filter(short_name__icontains=prd)   
    total_buyers = len(prddata)

    extra_context = extra_context or {"prddata": prddata, "total_buyers": total_buyers, "testdata": testdata, "user":user, "farm_produce": farm_produce}
    return render(request, 'farmer/buyers.html', extra_context)