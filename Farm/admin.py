from django.contrib import admin
from .models import Farm, FarmProduce
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.db.models import Q
# Register your models here.

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
     list_display = ("farmer", "farm_produce", "category", "location")

     def changelist_view(self, request, extra_context=None):
        fp = ''
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
        testdata = 'test data'
        chart_data = log.grade_avg(cdata)
        extra_context = extra_context or {"chart_data": chart_data, "testdata": testdata, "fdata": fdata, "prddata": prddata}

         # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(FarmProduce)