from django.forms import ModelForm
from .models import *
from django import forms


class MomentForm(ModelForm):
    class Meta:
        model = UserKind
        fields = '__all__'



# class TestForm(forms.Form):
#     name = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'class':'form-control'}))
