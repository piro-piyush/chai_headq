from django.shortcuts import render, redirect
from django.contrib.auth import  logout 
from django.contrib.auth.decorators import login_required
from django.shortcuts import  render

def register(request):
    # registration logic
    return render(request, "accounts/register.html")

def login_view(request):
    # login logic
    return render(request, "accounts/login.html")

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("accounts:login")
    return render(request, "accounts/logout.html")

def password_reset(request):
    # reset logic
    return render(request, "accounts/password_reset.html")

def password_change(request):
    # change logic
    return render(request, "accounts/password_change.html")

@login_required
def profile(request):
    return render(request, "accounts/profile.html", {"user": request.user})

