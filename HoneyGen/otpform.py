from django import forms

class otpform(forms.Form):
	entered = forms.IntegerField()