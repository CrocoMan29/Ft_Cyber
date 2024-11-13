from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse  # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib import messages # type: ignore
from .models import Users# type: ignore
# Create your views here.
def index(request):
	return render(request, 'index.html')

def register(request):
	if request.method == 'POST':
		username = request.POST.get("username")
		# firstname = request.POST.get['firstname']
		# lastname = request.POST.get['lastname']
		email = request.POST.get('email')
		password = request.POST.get('password')
		confirm_password = request.POST.get('confirm_password')
		if password == confirm_password:
			if User.objects.filter(email=email).exists():
				messages.info(request, 'email already exist!!')
				return redirect('register')
			elif User.objects.filter(username=username).exists():
				messages.info(request, 'username already exist!!')
				return redirect('register')
			else :
				user = User.objects.create_user(username=username, email=email, password=password)
				user.save();
				return redirect('login')
		else :
			messages.info(request, 'password not the same !!')
			return redirect('register')
	else :
		return render(request, 'register.html')

def log_in(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			messages.info(request, 'invalid user')
			return render(request, 'login.html')
	return render(request, 'login.html')

def log_out(request):
	logout(request)
	return redirect('index')

def counter(request):
	text = request.POST['text']
	c_text = len(text.split())
	return render(request, 'counter.html', {'counter': c_text})