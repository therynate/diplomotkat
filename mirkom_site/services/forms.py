from django import forms
from .models import ServiceRequest

class SellForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['title', 'description', 'photo']

class RepairForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['title', 'description', 'photo']

class CustomPCForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['description']