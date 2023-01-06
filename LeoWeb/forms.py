from django import forms

from .models import EmailModel,ContentModel

class EmailForms(forms.ModelForm):
    class Meta:
        model=EmailModel
        fields='__all__'
        # labels={
        #     'email':'Email' 
        # }