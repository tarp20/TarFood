from django import forms

from django.contrib.auth.models import User
from TarFoodApp.models import Restaurant,Meal

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name','email')

class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100,required=True)
    class Meta:
        model = User
        fields = ('first_name','last_name','email')


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name','phone','adress','logo')

class MealForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model=Meal
        exlude = ("restaurant")





