from django.contrib import admin
from  . import  models 
from searchableselect.widgets import SearchableSelect
from django import forms

# Register your models here.

class BusinessForm(forms.ModelForm):
    class Meta:
        model = models.Business
        exclude = ()
        widgets = {
            'business':SearchableSelect(model='processor.Business', search_field='name', limit=10 )

        }
class BusinessAdmin(admin.ModelAdmin):
    form = BusinessForm


admin.site.register(models.CapitalInvestmentRequirementsItem) 
admin.site.register(models.GeneralCostsItem) 
admin.site.register(models.DirectCostsItem) 
admin.site.register(models.ProjectProductCostPriceStructureItem) 
admin.site.register(models.Business, BusinessAdmin)
admin.site.register(models.Ministry) 
admin.site.register(models.Sector) 
admin.site.register(models.CapitalInvestmentRequirements) 
admin.site.register(models.GeneralCosts) 
admin.site.register(models.GovernmentFacilitiesIncentives) 
admin.site.register(models.DirectCosts) 
admin.site.register(models.ProductionOperatingCosts) 
admin.site.register(models.ProjectProductCostPriceStructure) 
admin.site.register(models.MarketAnalysis) 
admin.site.register(models.SourceEquipmentMaterials)

