from django import forms
from .models import ScrapingProcess

class ScrapingProcessForm(forms.Form):
    class Meta:
        model = ScrapingProcess
        fields = '__all__'
