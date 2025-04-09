from django import forms
from .models import Document
from .models import Profile

class DocForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'location', 'skills']
