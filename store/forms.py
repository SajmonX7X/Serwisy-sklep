from dataclasses import field
from .models import Customer
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    #@transaction.atomic
    #def data_save(self):
        #user=super().save(commit=False)
        #user.save()
        #customer=Customer.objects.create(user=user)
        #customer.name=self.cleaned_data.get('username')
        #customer.email=self.cleaned_data.get('email')
        #customer.save()
        #return user
