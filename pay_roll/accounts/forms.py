from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Create_Business



User = get_user_model()

class Create_Account_Form(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    phone = forms.CharField(max_length=254, help_text='Enter a valid Phone No.')
    is_business = forms.BooleanField(required=False)
    is_accountant = forms.BooleanField(required=False)
    


    class Meta:
        model = User
        fields = [
            
             
            'username',
            'first_name', 
            'last_name', 
            'email',
            'phone',
            'password1', 
            'password2', 
            'is_business',
            'is_accountant',
            
            ]


class CreateForm(forms.ModelForm):

	class Meta:
		model = Create_Business
		fields = '__all__'	