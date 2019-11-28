from django import forms
from .models import Host,Visitor
from django.utils import timezone

class VisitorForm(forms.ModelForm):
	
	class Meta:
		model = Visitor
		fields = ('visitor_name', 'email','phone','checkout')

class HostForm(forms.Form):
	host_name = forms.CharField(label='host_name', max_length=200)
	email = forms.EmailField()
	phone = forms.CharField(max_length=12)

class HostloginForm(forms.Form):
	host_name = forms.CharField(label='host_name', max_length=200)


class TimeForm(forms.ModelForm):
	class Meta:
		model = Visitor
		fields = ('checkout',)
