from django import forms
from .models import Proposal

class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ['cover_letter', 'proposed_price', 'estimated_days']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Introduce yourself and explain why you are the best fit...'}),
            'proposed_price': forms.NumberInput(attrs={'placeholder': 'Your price in KSh'}),
            'estimated_days': forms.NumberInput(attrs={'placeholder': 'Days to complete'}),
        }
