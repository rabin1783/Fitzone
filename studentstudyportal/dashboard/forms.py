
from django.forms import widgets
from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm



class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','description',]

class DateInput(forms.DateInput):
    input_type = 'date'


class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100,label="Enter Your Search :")

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','is_finished']
        
class ConversionForm(forms.Form):
    CHOICES = [('mass','Mass'),]
    measurement = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect)




class ConversionMassForm(forms.Form):
    CHOICES = [('pound','Pound'),('kilogram','Kilogram')]
    input = forms.CharField(required=False,label=False, widget=forms.TextInput(
        attrs= {'type':'number','placeholder':'Enter the Number'}
    ))
    measure1 = forms.CharField(
        label='',widget=forms.Select(choices = CHOICES)
    )
    measure2 = forms.CharField(
        label='',widget=forms.Select(choices = CHOICES)
    )

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','email']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        #to generate form with all fields/attributes form
        #fields = "__all__"

        #to generate form with limited /custom field
        fields = ('email','password')

        model = AppUser 

class CreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ('first_name','middle_name','last_name',\
                'email','contact','dob','password','address')

        model = AppUser


from .models import Step


class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ('title', 'description', 'cover')

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        #to generate form with all fields/attributes form
        #fields = "__all__"

        #to generate form with limited /custom field
        fields = ('email','password')

        model = AppUser

class AdminLoginForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        #to generate form with all fields/attributes form
        #fields = "__all__"

        #to generate form with limited /custom field
        fields = ('email','password1')

        model = AppUser 
class AdminRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ('first_name','middle_name','last_name',\
                'email','contact','dob','password1','address')

        model = AppUser 
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ('first_name','middle_name','last_name',\
                'email','contact','dob','password','address')

        model = AppUser 

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due':DateInput()}

        fields = ['title','description','is_finished']
