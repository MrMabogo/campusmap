from django import forms

from .models import Recommendation

class RecommendationPostingForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ('location_name', 'address', 'longitude', 'latitude', 'details')

        widgets = {
            'location_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'})
        }