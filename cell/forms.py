from django import forms

from .models import SimCard

class ActivateForm(forms.ModelForm):

    class Meta:
        model = SimCard
        fields = ('phone','offerid',)
        

class GetBalance(forms.ModelForm):

    class Meta:
        model = SimCard
        fields = ('phone',)