from django import forms
from .models import contact

class contactforms(forms.ModelForm):
    class Meta():
        model = contact
        fields = ["user_name", "user_email","message"]
        labels= {"user_name": "Name", "user_email":"Email", "message":"Message"}
