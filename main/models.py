from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

# Create your models here.

#Definição do modelo MenuPrincipal
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

class ManipulaUsuario(BaseUserManager):
    def create_user(self, username, nome, perfil, password):
        user = self.model(
            username=username,
            nome=nome,
            perfil=perfil
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, username, nome, perfil, password):
        user = self.create_user(
            username,
            nome=nome,
            perfil=perfil,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Login', max_length=11, unique=True)
    nome = models.CharField('Nome', max_length=255)
    perfil = models.CharField('Perfil', max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = ManipulaUsuario()

    REQUIRED_FIELDS = ['nome', 'perfil']
    USERNAME_FIELD = 'username'
    
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    def __str__(self):
        return self.nome