from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from Farm.models import Farm, FarmProduce
from investmanager import logic as log
from investmanager.models import Product, ManufacturingCompany, BrandCompany, ProductComposition, loans
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.db.models import Q
from account.models import AccountUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models
from django.views.generic import DetailView, TemplateView

class RecommendationsView(TemplateView):
     model = models.CapitalInvestmentRequirements
     template_name = 'processor/recommends.html'

     def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['business'] = models.Business.objects.all()
        user_id = self.request.user.id
        extra_context = ''
        title = ''
        fp = ''
        items = ''
        user = AccountUser.objects.get(user_id=user_id)
        business = models.Business.objects.all()
        cp = models.CapitalInvestmentRequirements.objects.all()
        businessdata = dict()
        for a in business:
            print('-----------------------------------------------')
            # print(a.name)

            cpr = models.CapitalInvestmentRequirements.objects.get(id=a.id)
            # cpr = models.CapitalInvestmentRequirements.objects.all()
            sums = 0.0
            context['items'] = cpr.name.all()  
            items = context['items']
           
            sums = float()
            item_sum = list()

            for i in items:
                
                print('name: ',i.name, "++++",i.qty, "++++", i.at, "total:" , i.qty*i.at )
                sums = float(sums) + float(i.qty*i.at)
                 
            


            print('sums is ', sums)
                # tot_sums = sum(item_sum.append(sums))
                # print('total sums:: ',tot_sums)

                # context['sums'] = sums
                # print('first element is:', sums[0])
                
        return context

def home(request):
    user_id = request.user.id
    extra_context = ''
    title = ''
    fp = ''
    user = AccountUser.objects.get(user_id=user_id)
    account_user = ManufacturingCompany.objects.get(user_id = request.user.id)
    products = account_user.products
    cdata = loans.objects.all()
    testdata = 'Farms MArket Stocks'
    chart_data = log.grade_avg(cdata)


    extra_context = extra_context or {'chart_data': chart_data, "testdata": testdata, "user":user, "products":products}
    return render(request, 'processor/home.html', extra_context )


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
    return render(request, 'processor/contacts.html', extra_context )

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
    return render(request, 'processor/market_data.html', extra_context )

def file_manager(request):
    user_id = request.user.id
    extra_context = ''
    title = ''
    fp = ''
    user = AccountUser.objects.get(user_id=user_id)
    
    cdata = loans.objects.all()
    testdata = 'New Clients'
    chart_data = log.grade_avg(cdata)

    extra_context = extra_context or {'chart_data': chart_data, "testdata": testdata, "user":user}
    return render(request, 'processor/file_manager.html', extra_context )

def investors(request):
    user = request.user
    print(user.id)
    extra_context = ''
    title = ''
    fp = ''
    
    
    cdata = loans.objects.all()
    testdata = 'New Clients'
    chart_data = log.grade_avg(cdata)

    extra_context = extra_context or {'chart_data': chart_data, "testdata": testdata}
    return render(request, 'processor/investors.html', extra_context )

@login_required(login_url='/accounts/login/')
def processor(request, user_id):
    extra_context = ''
    title = ''
    fp = ''
    user = AccountUser.objects.get(user_id=user_id)
    
    cdata = loans.objects.all()
    testdata = 'New Clients'
    chart_data = log.grade_avg(cdata)

    extra_context = extra_context or {'chart_data': chart_data, "testdata": testdata, "user":user}
    return render(request, 'processor/home.html', extra_context )

    

def buyers(request):
    extra_context = ''
    chart_data = ''
    testdata = ''
    prddata = []
    user = ''
    fp = ''
    user_id = request.user.id
    user = AccountUser.objects.get(user_id=user_id)

    # FIND POTENTIAL BUYERS BY QUERYING PRODUCE PROCESSORS
        # get farmer produce
    print('user id is:: ', request.user.id)

    account_user = ManufacturingCompany.objects.get(user_id = request.user.id)
    products = account_user.products
    

    a = ProductComposition.objects.all()
    for i in a:
        prod = {'id': i.id, ' name': i.product, 'comp': i.composition}
        # print(prod)
        # print('id', i.id, ' name', i.product, 'comp', i.composition)

        prod_id = prod['id']
        prod_comp = prod['comp']
    

    

    prd = ProductComposition.objects.filter(Q(product__exact= prod_id))
    for item in prd:
        prd = item.composition
        print(prd)
    rp = str(prd)
    print(rp)

    prd = Farm.objects.filter(Q(farm_produce__exact=prod_id))
    

    
    total_farmers = len(prd)

    extra_context = extra_context or {"total_farmers": total_farmers, "prd": prd ,"testdata": testdata, "user":user, "products": products}
    return render(request, 'processor/buyers.html', extra_context)