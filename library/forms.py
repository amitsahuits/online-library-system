from django import forms
from django.contrib.auth.models import User
from .models import CustomUser,Book
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields = ['email']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','desc']
        labels = {'title':'Title', 'desc':'Description'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                    'desc':forms.Textarea(attrs={'class':'form-control'})
        }