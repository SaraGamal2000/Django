from django import forms

class NewAccount(forms.Form):
    id = forms.IntegerField(required=True)
    fname = forms.CharField(max_length=200,required=True)
    lname = forms.CharField(max_length=200,required=True)
    email = forms.EmailField(max_length=254,required=True)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput,required=True)
    image = forms.ImageField(required=True)
    
#    /required=False
# upload_to='media/'