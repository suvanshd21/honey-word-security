from django.shortcuts import render
from django.http import HttpResponse
from .forms import IndexForm
from .otpform import otpform
from .HoneyWordGenerator import *
from .HoneyWordChecker import *

def index1(request):
	form = IndexForm()
	return render(request, 'index1.html', {'form':form})

def signup(request):
	form = IndexForm(request.POST)
	if form.is_valid():
		username=form.cleaned_data['username']
		password=form.cleaned_data['password']
		store_sweet_string(username,password)
		return HttpResponse("<h3 style='text-align:center;'>Thank you for signing up!</h3>")

def index2(request):
	form = IndexForm()
	return render(request, 'index2.html', {'form':form})

def login(request):
	form = IndexForm(request.POST)
	if form.is_valid():
		username=form.cleaned_data['username']
		password=form.cleaned_data['password']
		authenicity=honey_checker(username,password)
		print(authenicity)
		if authenicity == "Correct":
			return render(request,'cab booking form.html')
		else:
			return HttpResponse("<h3 style='text-align:center;'>Invalid Attempt.</h3>")

original = 0
def generate_otp(request):
	global original
	original=random.randint(100001,999999)
	print(original)
	form = otpform()
	return render(request,'enter_otp.html',{'form':form})

def verify(request):
	global original
	form = otpform(request.POST)
	if form.is_valid():
		entered=form.cleaned_data['entered']
		print(entered,' ',original)
		if entered == original:
			print("Approved")
			return HttpResponse("<h3 style='text-align:center;'>Booking Approved!</h3>")
		else:
			print("Denied")
			return HttpResponse("<h3 style='text-align:center;'>Booking Denied.</h3>")
