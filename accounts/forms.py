from accounts.models import Support
from datetime import datetime,date
from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import  UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import SelectDateWidget, Textarea
from blog.models import HappeningNow, Post, Profile, Withdrawal,Category

class DateInput(forms.DateInput):
    input_type = 'date'
 
    
class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(
        max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(
        max_length=254, required=True, help_text='Required. Inform a valid email address.')
    
    phone_no = forms.CharField(max_length=20,required=True,help_text='Required.')
    account_name = forms.CharField(max_length=50,required=True,help_text='Required.')
    bank_name = forms.CharField(max_length=50,required=True,help_text='Required.')
    bank_account = forms.CharField(max_length=50,required=True,help_text='Required.')
    country = forms.CharField()
    state = forms.CharField()
    city = forms.CharField()
    profile_picture = forms.ImageField(required=False)
    dob = forms.DateField(widget=DateInput())
    referred_by = forms.CharField(required=False)
    
    NO_BENEFIT_USER = 1
    READ_COMMENT_USER = 2
    REPORTER = 3
    USER_TYPE_CHOICES = [
        (NO_BENEFIT_USER, 'No Benefit User'),
        (READ_COMMENT_USER, 'Read/Comment User '),
        (REPORTER, 'Reporter'),
    ]
    
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES,required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2','phone_no','dob',
                  'account_name','bank_name','bank_account',
                  'country','state','city','profile_picture','referred_by')
       
    def clean_dob(self):
        dob_data = self.cleaned_data['dob']
        age = (date.today() - dob_data).days/365
        if age < 18:
            raise forms.ValidationError('Must be at least 18 years old to register')
        return dob_data
        
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email already used")
        return data

      

class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name',
                  'email')
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_no','dob',
                  'account_name','bank_name','bank_account',
                  'country','state','city','profile_picture'
                  )

class PostForm(forms.ModelForm):       
    class Meta:
        model = Post
        fields = ('user','category','title','body','featured_image')
        

class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = ('user','amount')

class YouTubeForm(forms.Form):
    title = forms.CharField(required=True)
    description = forms.CharField(required=True)
    tags = forms.CharField(required=True)
    video = forms.FileField(required=True)

class VideoForm(forms.ModelForm):
    title = forms.CharField(required=True)
    description = forms.Textarea()
    video = forms.FileField(required=True)
    
    class Meta:
        model = HappeningNow
        fields = ('user','title','description','video')

class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = '__all__'