from django import forms

from .models import Recommendation

class RecommendationPostingForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ('location_idea', )

        widgets = {
            'location_idea': forms.Textarea(attrs={'class': 'form-control'}),
        }