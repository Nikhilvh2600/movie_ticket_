from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from .utils import get_otp
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from movies.models import Movies
# Create your views here.
def registerview(request):
    fm = RegisterForm()
    context = {
        'RegisterForm' : fm }
    if request.method == 'POST':
        user = RegisterForm(request.POST)
        if user.is_valid():
            user.save()
            username = user.cleaned_data['username']
            email = user.cleaned_data['email']
            send_mail(
                'Registration successfull',
                f'{username} you have created account in movie ticket booking application' ,
                'anthonyalex543@gmail.com',
                [email],
                fail_silently=True
            )
            return redirect('signin')
    return render(request,'accounts/register.html',context)
            
def LoginView(request):
    context = {
            'LoginForm' : LoginForm()
    }
    if request.method == 'POST':
        fm = LoginForm(data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                if user.is_authenticated:
                    login(request,user)   
                    messages.success(request,f'logged in as {username}')
                    return redirect('home')
    return render(request, 'accounts/login.html', context)

def logoutview(request):
    logout(request)
    messages.error(request,'you have been logged out')
    return redirect('signin')


# @login_required(login_url='/accounts/signin/')
# def home(request):
#     context = {
#         'movies' : Movies.objects.all()
#     }
#     return render(request,'accounts/home.html',context)