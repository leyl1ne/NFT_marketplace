from django import forms 
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder': 'Username'}),
            'email' : forms.EmailInput(attrs={'placeholder' : 'Email'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']
    

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name' : forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name' : forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email' : forms.TextInput(attrs={'placeholder': 'Email'}),
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']
        widgets = {
            'date_of_birth' : forms.TextInput(attrs={'placeholder': 'Date Of Birth'}),
        }