from django.shortcuts import render
from first_app.models import PrimaryInfo
from first_app.forms import PrimaryForm
# Create your views here.
def index(request):
	form = PrimaryInfo
	return render(request, 'first_app/index.html', {'form':PrimaryInfo.objects.all})




def intake(request):
	form = PrimaryForm
	if request.method == "POST":
		form = PrimaryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
	return render(request, 'first_app/intake.html', {'form':form})