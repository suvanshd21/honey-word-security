from django import forms

class IndexForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': "input100","type":"text"}))
	password = forms.CharField(widget=forms.TextInput(attrs={'class': "input100","type":"password"}))