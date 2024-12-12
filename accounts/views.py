from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import CreateUserForm
from .models import ExtendedUserData

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    
    if request.method == "POST":
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Username or Password is Incorrect')
    
    return render(request, 'accounts/login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')

            created_user_obj = User.objects.get(username=user)
            new_extended_data = ExtendedUserData(user=created_user_obj,
                                                 profile_pic=None,
                                                 headliner=None,
                                                 bio=None,
                                                 location=None,
                                                 )
            new_extended_data.save()
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('login')
