from django import forms
from .models import ScrapingProcess

class ScrapingProcessForm(forms.ModelForm):
    
    file_source = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'onchange': 'this.form.submit();'}))
    website_lists = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'http://example.com'}))

    class Meta:
        model = ScrapingProcess
        fields = ('file_source', 'website_lists',)