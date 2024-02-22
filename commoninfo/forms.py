from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    username = forms.CharField(label='username', max_length=20, required=True)
    email = forms.EmailField(label='email', required=True)
    first_name = forms.CharField(label='First Name', max_length=200, required=True)
    last_name = forms.CharField(label='Last Name', max_length=200)
    day_of_birth = forms.DateField(label='Day of birth', widget=forms.DateInput())
    password = forms.CharField(label='password', max_length=30, required=True, widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm Password', required=True, widget=forms.PasswordInput())

    class Meta:
        model = Patient
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'day_of_birth']
        
class FetchForm(forms.Form):
    id = forms.IntegerField(label="UniqueID", required=True)