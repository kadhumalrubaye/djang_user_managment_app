from django import forms

class UserRegisteration(forms.Form):

    first_name = forms.CharField(required=True,widget=forms.TextInput (attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput (attrs={'class':'form-control'}))
    age = forms.CharField(required=True,widget=forms.TextInput (attrs={'class':'form-control'}))
    date_birth = forms.CharField(required=True,widget=forms.TextInput (attrs={'class':'form-control'}))

class UserDegreeForm(forms.Form):
    degree=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))