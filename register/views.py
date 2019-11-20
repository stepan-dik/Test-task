from django.contrib.auth import login, authenticate
from register.forms import SignUpForm
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def signup_view(request):
    print(request)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            messages.success(request, f'account created for {username}')
            user = authenticate(username=username, password=raw_password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('reg-profile')
    else:
        form = SignUpForm()
    context = {'form': form, 'title': 'Sign up', "terms": "terms"}
    return render(request, 'signup.html', context)

def home_view(request):
    if request.user.is_authenticated:
        try:
            return redirect('reg-profile')
        except:
            return redirect('reg-g-profile')
    else:
        return redirect('signup')

def signin_view(request):
    pass

def dynamic_lookup_view(request, username=None):
    print(request)
    if request.user.is_authenticated:
        context = {"object":request.user,
                   "title": f"{request.user}'s account"
                    }
        return render(request, 'users/user.html', context)
    else:
        return redirect('signup')

def logout_view(request):
    logout(request)
    return redirect('home')

def p_view(request):
    return render(request, 'privacy.html', {})

def t_view(request):
    return render(request, 'terms.html', {})