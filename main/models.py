from django.db import models

# Create your models here.
class MenuPrincipal(models.Model):
    '''Classe para definição dos itens do menu principal'''
    item_menu = models.CharField('Item do menu', max_length=50)
    ordem_menu = models.IntegerField('Ordem no Menu', default=0)
    url_menu = models.CharField('URL', max_length=500)
    
    class Meta:
        ordering = ['ordem_menu']
    
    
    def __str__(self):
        """String que representa o objeto modelo."""
        return f'{self.item_menu}'