from django import forms
from .models import MyGig


class GigForm(forms.ModelForm):

    title = forms.CharField(label="GIG TILE",widget = forms.Textarea(attrs={'class':'form-control','placeholder':'I will do something'}))
    search_tag = forms.CharField(label="SEARCH TAGS",widget = forms.TextInput(attrs={'class':'form-control'}))
    price= forms.FloatField(label = "Minimum Price", widget = forms.NumberInput(attrs={'class':'form-control'}))
    time = forms.IntegerField(label = "WORKING DAYS", widget = forms.NumberInput(attrs={'class':'form-control','placeholder':'No. of Days'}))
    gig_image = forms.ImageField(label="Upload Image")
    
	
    class Meta:
        model = MyGig
        exclude = ['user','s_name','c_name','description','first_gig','contact_no']    