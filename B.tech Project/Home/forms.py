from django import forms
from django.forms import ModelForm
from Home.models import StaffInfo,StudentInfo,AlumniInfo
from django.forms.models import inlineformset_factory
from django.contrib.admin.widgets import *

class AlumniInfo_form(ModelForm):
    Password=forms.CharField(max_length=150,widget=forms.PasswordInput)
    Enter_Password_Again=forms.CharField(max_length=150,widget=forms.PasswordInput)
    class Meta:
        model = AlumniInfo
        fields='__all__'
    def __init__(self,*args,**kwargs):
        super(AlumniInfo_form,self).__init__(*args,**kwargs)
        self.fields['First_Name'].widget=forms.TextInput(attrs={'class':'check','placeholder':'Enter First Name'})
        self.fields['Last_Name'].widget=forms.TextInput(attrs={'placeholder':'Enter Last Name'})
        self.fields['Date_of_Birth'].widget=forms.TextInput(attrs={'type':'date'})
        self.fields['Email_Id'].widget=forms.TextInput(attrs={'value':'@itbhu.ac.in'})
        self.fields['First_Name'].required = "True"

class StaffInfo_form(ModelForm):
    Password=forms.CharField(max_length=150,widget=forms.PasswordInput)
    Enter_Password_Again=forms.CharField(max_length=150,widget=forms.PasswordInput)
    class Meta:
        model = StaffInfo
        fields='__all__'
    def __init__(self,*args,**kwargs):
        super(StaffInfo_form,self).__init__(*args,**kwargs)
        self.fields['First_Name'].widget=forms.TextInput(attrs={'class':'check','placeholder':'Enter First Name'})
        self.fields['Last_Name'].widget=forms.TextInput(attrs={'placeholder':'Enter Last Name'})
        self.fields['Date_of_Birth'].widget=forms.TextInput(attrs={'type':'date'})
        self.fields['Email_Id'].widget=forms.TextInput(attrs={'value':'@itbhu.ac.in'})
        
class StudentInfo_form(ModelForm):
    Password=forms.CharField(max_length=150,widget=forms.PasswordInput)
    Enter_Password_Again=forms.CharField(max_length=150,widget=forms.PasswordInput)
    class Meta:
        model = StudentInfo
        fields='__all__'
    def __init__(self,*args,**kwargs):
        super(StudentInfo_form,self).__init__(*args,**kwargs)
        #self.fields['First_Name'].widget=forms.TextInput(attrs={'class':'check','placeholder':'Enter First Name'})
        #self.fields['Last_Name'].widget=forms.TextInput(attrs={'placeholder':'Enter Last Name'})
        self.fields['Date_of_Birth'].widget=forms.TextInput(attrs={'type':'date'})
        self.fields['Email_Id'].widget=forms.TextInput(attrs={'value':'@itbhu.ac.in'})
