from django.contrib import admin

# Register your models here.
from main.models import MenuPrincipal
from main.models import CustomUser


class MenuPrincipalAdmin(admin.ModelAdmin):
    #Definindo os campos que serão exibidos
    list_display = ('item_menu', 'ordem_menu', 'url_menu') 

admin.site.register(MenuPrincipal, MenuPrincipalAdmin)

class CustomUserAdmin(admin.ModelAdmin):
    #Definindo os campos que serão exibidos
    list_display = ('username', 'nome', 'perfil', 'is_active', 'is_staff') 

admin.site.register(CustomUser, CustomUserAdmin)