from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import ProfileUpdate
# Create your views here.
def index(request):
	return render(request,'users/index.html')

def contact(request):
	return render(request,'users/contact.html')

def profile(request):

	if request.method=='POST':
		puform=ProfileUpdate(request.POST,request.FILES,instance=request.user.profile)
		if puform.is_valid():
			puform.save()
			return redirect('/posts')
	else:
		puform=ProfileUpdate(request.POST,request.FILES,instance=request.user.profile)
	
	return render(request,'users/profile.html',{'pform':puform})



def register(request):
	form=UserCreationForm()
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		print('insiderform')
		print(form.is_valid())
		if form.is_valid():
			form.save()
			# username=form.cleaned_data.get('username')
			# password=form.cleaned_data.get('password')
			messages.success(request,'User have been created Successfully')
			return redirect('/posts')
	else:
		form=UserCreationForm()
	return render(request,'users/register.html',{'form':form})




def index(request):
	return red
 

    
