from django import forms
from .models import Language, MyProfile,gender_list
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from languages.fields import LanguageField

class ProfileForm(forms.ModelForm):

    full_name = forms.CharField(label="Full Name",widget = forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(label="Description",widget = forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your description.'}))
    country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={"class": "form-control"}))
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=gender_list)
    contact_no = forms.CharField(label="Contact No.",disabled = False ,widget = forms.TextInput(attrs={'class':'form-control',}))
    skills = forms.CharField(label="Skills",disabled = False ,widget = forms.TextInput(attrs={'class':'form-control'}))
    languages = LanguageField().formfield(widget=CountrySelectWidget(attrs={"class": "form-control"}))
    facebook = forms.URLField(label="Facebook",disabled = False ,widget = forms.URLInput(attrs={'class':'form-control'}))
    github = forms.URLField(label="Github",disabled = False ,widget = forms.URLInput(attrs={'class':'form-control'}))

    class Meta:
    	model = MyProfile
    	exclude = ['google','profile_image','user','profile_set']


class ChangeProfilePicture(forms.ModelForm):

    profile_image = forms.ImageField(label="Upload Image")


    class Meta:
        model = MyProfile
        exclude = ['full_name','country','description','gender','contact_no','skills','languages','facebook','github','google','user','profile_set']