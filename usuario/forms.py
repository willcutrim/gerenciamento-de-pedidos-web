from django.contrib.auth.models import User
from django import forms

from usuario.models import AvatarUser

class CadastroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class AvatarUserForm(forms.ModelForm):
    class Meta:
        model = AvatarUser
        fields = ['avatar']