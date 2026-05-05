from django import forms
from .models import comments

class commentforms(forms.ModelForm):
    class Meta():
        model = comments
        fields = ["user_name", "user_email","user_comments"]
        labels= {"user_name": "Your Name", "user_email":"Your Email", "user_comments":"Comments"}
