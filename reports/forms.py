from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['category', 'description', 'photo', 'address', 'location_lat', 'location_lng']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe the issue...'}),
            'address': forms.TextInput(attrs={'placeholder': 'Street address or nearest landmark'}),
        }