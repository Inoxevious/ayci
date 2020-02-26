from django.contrib import admin
from . models import MenuItem, Menu, SubItem , SubMenu
# Register your models here.

admin.site.register(MenuItem)
admin.site.register(Menu)

admin.site.register(SubItem)
