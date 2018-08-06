from django.forms import ModelForm
from .models import *


class MomentForm(ModelForm):
    class Meta:
        model = UserKind
        fields = '__all__'