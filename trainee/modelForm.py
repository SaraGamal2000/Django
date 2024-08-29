from django import forms
from .models import Trainee


class TraineeModelForm(forms.ModelForm):
    class Meta:
        model = Trainee  # Correct the model to Trainee
        fields = ['id', 'name', 'id_track', 'image']  # Ensure these fields exist in the Trainee model
        widgets = {
            'image': forms.ClearableFileInput(),  # For handling file uploads
        }