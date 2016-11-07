# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

class DocumentForm(forms.Form):
    
    docfile = forms.FileField(
        label='Subir una fotografia'
    )
    

