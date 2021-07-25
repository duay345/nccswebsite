from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from .models import info
from .models import Intro
from .models import mydoc
from .models import profile
from .models import skills
from .models import Aboutyou

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from .models import Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class AboutyouForm(forms.ModelForm):
    start = forms.CharField( widget= forms.TextInput
                           (attrs={'placeholder':'write somethiing about you.','style':'max-width: 24em'}))

    class Meta:
        model = Aboutyou
        fields = ('start',)


class infoForm(forms.ModelForm):  
    Email_address= forms.EmailField(required= True, widget= forms.TextInput
                           (attrs={'placeholder':'your_mail@example.com','style':'max-width: 12em'}))  
    Phone_number = PhoneNumberField()                 
    class Meta:
        model = info
        fields = ( 'Email_address','Phone_number','facebook','linkedin')


class IntroForm(forms.ModelForm):
     Applicants_name = forms.CharField( widget= forms.TextInput
                           (attrs={'placeholder':'Your Full Name','style':'max-width: 24em'}))
     CNIC = forms.CharField( widget= forms.TextInput
                           (attrs={'placeholder':'enter correct CNIC','style':'max-width: 24em'}))
     Father_name = forms.CharField( widget= forms.TextInput
                           (attrs={'placeholder':'enter real name','style':'max-width:24em'}))
     Mother_name = forms.CharField( widget= forms.TextInput
                           (attrs={'placeholder':'enter real name','style':'max-width: 24em'}))
     Gender = forms.ChoiceField(required=True, widget=forms.RadioSelect
                           (attrs={'class': 'Radio'}), choices=(('male','Male'),('female','Female'),))
     Marital_status = forms.ChoiceField(required=True, widget=forms.RadioSelect
                           (attrs={'class': 'Radio'}), choices=(('single','single'),('married','married'),('divorced','divorced'),))
     Domicile = forms.ChoiceField(required=True, widget=forms.RadioSelect
                           (attrs={'class': 'Radio'}), choices=(('sindh','Sindh'),('other','Other'),))
     #Gender = forms.CharField( widget= forms.TextInput
                           #(attrs={'placeholder':'write other if not male /female','style':'max-width: 24em'}))
     #Marital_status = forms.CharField( widget= forms.TextInput
                           #(attrs={'placeholder':'enter valid entity','style':'max-width: 24em'}))
     #Domicile = forms.CharField( widget= forms.TextInput
                           #(attrs={'placeholder':'enter valid entity','style':'max-width: 24em'}))
     Address = forms.CharField( widget= forms.TextInput
                           (attrs={'placeholder':'enter valid entity','style':'max-width: 24em'}))
     Employment = forms.CharField( widget= forms.TextInput
                           (attrs={'placeholder':'enter valid entity','style':'max-width: 24em'}))
     Nationality = forms.CharField( widget= forms.TextInput
                           (attrs={'placeholder':'enter valid entity','style':'max-width: 24em'}))
     Religion= forms.CharField( widget= forms.TextInput
                           (attrs={'placeholder':'enter valid entity','style':'max-width: 24em'}))
     Country = forms.CharField( widget= forms.TextInput
                           (attrs={'placeholder':'enter valid entity','style':'max-width: 24em'}))
     City = forms.CharField( widget= forms.TextInput
                           (attrs={'placeholder':'enter valid entity','style':'max-width: 24em'}))
     class Meta:
        model = Intro
        fields = ('Applicants_name', 'CNIC','Father_name','Mother_name','Gender','Marital_status',
        'Domicile','Address','Employment','Nationality','Religion', 'Country', 'City')
         



class mydocForm(forms.ModelForm):
    name = forms.CharField( widget= forms.TextInput(attrs={'placeholder':'Your Full Name','style':'max-width: 12em'}))   
    
    class Meta:
        model = mydoc
        fields = ('name','cv', 'picture', 'certificate','degree')

class profileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ('profilepic',)

class skillsForm(forms.ModelForm):
    
    Additional_skills = forms.CharField(required=False,   widget= forms.TextInput
                           (attrs={'placeholder':'if you have another skill excpet above mentioned skills '}))
    
    class Meta:
        model = skills
        fields = ('Interpersonal_skills','Intrapersonal_skills','Hands_on_programming_languages','Additional_skills')
        



