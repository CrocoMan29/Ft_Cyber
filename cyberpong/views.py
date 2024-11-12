from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse  # type: ignore
from django.contrib.auth import authenticate # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib import messages # type: ignore
# Create your views here.
def index(request):
	return render(request, 'index.html')

def register(request):
	if request.method == 'POST':
		username = request.POST.get("username")
		firstname = request.POST.get['firstname']
		lastname = request.POST.get['lastname']
		email = request.POST.get['email']
		password = request.POST.get['password']
		confirm_password = request.POST.get['confirm_password']
		if password == confirm_password:
			if User.objects.filter(email=email).exists():
				messages.info(request, 'email already exist!!')
				return redirect('register')
	return render(request, 'register.html')

def counter(request):
	text = request.POST['text']
	c_text = len(text.split())
	return render(request, 'counter.html', {'counter': c_text})