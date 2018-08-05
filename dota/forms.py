from django.forms import ModelForm
from .models import *

class Moment(ModelForm):
    class Meta:
        model = MomentModel
        fields = '__all__'