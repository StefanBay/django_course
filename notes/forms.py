from logging import NOTSET
from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
            model = Notes
            fields = ('title', 'text')
            widget = {
                'title': forms.TextInput(attrs={'class':'form-control my-5'}),
                'text' : forms.Textarea(attrs={"class":"form-control mb-5"})
            }
            labels ={
                'text':'Write your thoughts here:'
            }
    
    def clean_title(self):
        """the method valdiates the input, so that only titles containing "django" are allowed"""
        title = self.cleaned_data['title'] #cleaned_data = returned fields from the form
        if 'django' not in title.lower():
            raise forms.ValidationError("Only notes about Django are accepted!")
        return title
