from django import forms
from Contact .models import News_letter

class Newsletter(forms.ModelForm):
    class Meta:
        model=News_letter
        fields='__all__'