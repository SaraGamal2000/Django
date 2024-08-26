from django import forms
from .models import Track
class Newtrainee(forms.Form):
    id = forms.IntegerField(required=True)
    name = forms.CharField(max_length=200,required=True)
    id_track = forms.ModelChoiceField(queryset=Track.objects.all(), required=True)
    image = forms.ImageField(required=True)
    