from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    nome = forms.CharField(max_length=255, required=True)
    perfil = forms.CharField(max_length=50, required=True)
    username = forms.CharField(max_length=11, required=True)

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('nome', 'perfil', 'username', 'password1', 'password2')
