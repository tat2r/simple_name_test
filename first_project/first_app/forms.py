from django import forms
from first_app.models import PrimaryInfo

class PrimaryForm(forms.ModelForm):
	class Meta():
		model = PrimaryInfo
		fields = '__all__'