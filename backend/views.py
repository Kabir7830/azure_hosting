from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate,get_user_model
User = get_user_model()
from django.contrib import messages
# Create your views here.


def mainForm(request):
    if request.user.is_authenticated:
        return render(request,"mainForm.html")
    return redirect('login')

def register(request):
    
    if request.method == "POST":
        
        user = User.objects.create(
            first_name = request.POST.get('first_name'),
            email = request.POST.get('email'),
        )
        user.set_password(request.POST.get('password'))
        user.save()
        return redirect('login')
    return render(request,'signup.html')
        

def loginHandler(request):
    
    if request.method == "POST":
        user = authenticate(username = request.POST.get('email'),password=request.POST.get('password'))
        
        if user is not None:
            login(request,user)
            return redirect('homepage')
        messages.success(request,"Invalid Username or Password")
    return render(request,"login.html")


def logoutHandler(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            logout(request)
            return redirect('homepage')
        return redirect('login')
    return redirect(request.META.get('HTTP_REFERER'))
