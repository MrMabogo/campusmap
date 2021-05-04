from django import forms
from django.core.exceptions import ValidationError
from .models import Recommendation

class RecommendationPostingForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ('location_name', 'address', 'longitude', 'latitude', 'details')

        widgets = {
            'location_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 
                'placeholder': '0 Rotunda Alley, Charlottesville, VA'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'})
        }
    
    def clean(self):
        super().clean()

        addr = self.cleaned_data.get(('address'))
        addr = addr.split(',')
        lng = self.cleaned_data.get(('longitude'))
        lat = self.cleaned_data.get(('latitude'))

        if not lng and not lat and not addr:
            raise ValidationError(
                    'You must enter an address or a pair of coordinates'
                )
        
        if not lng and not lat and len(addr) < 3:
            raise ValidationError(
                    '''Incorrect address format. 
                    Try [number] [street], Charlottesville, VA'''
                )
        