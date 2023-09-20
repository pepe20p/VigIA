from django.contrib import admin

# Register your models here.
from main.models import MenuPrincipal


class MenuPrincipalAdmin(admin.ModelAdmin):
    #Definindo os campos que serão exibidos
    list_display = ('item_menu', 'ordem_menu', 'url_menu') 

admin.site.register(MenuPrincipal, MenuPrincipalAdmin)