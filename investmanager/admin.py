from django.contrib import admin
from .models import Machinery, RawMaterials, Proces, ManufacturingCompany, FoodGroup, BrandCompany, Product, ProductComposition
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("short_name", "brandcompany", "manufacturingcompany", "current_market_avg_price")

    def changelist_view(self, request, extra_context=None):
        data = Product.objects.all()

        extra_context = extra_context or {"data": data}

         # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)



admin.site.register(Machinery) 
admin.site.register(RawMaterials) 
admin.site.register(Proces)
admin.site.register(ManufacturingCompany) 
admin.site.register(FoodGroup) 
admin.site.register(BrandCompany) 
# admin.site.register(Product) 
admin.site.register(ProductComposition)
