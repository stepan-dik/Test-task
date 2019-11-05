from django.contrib.auth import login, authenticate
from register.forms import SignUpForm
from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            firstname= form.cleaned_data.get('firstname')
            lastname= form.cleaned_data.get('lastname')
            username= form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            ads = form.cleaned_data.get('ads')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form': form, 'title': 'Sign up', "terms": "terms"}
    return render(request, 'signup.html', context)

def dynamic_lookup_view(request):
    obj = User.objects.get(request.username)
    context = {
    "object":obj

    }
    return render(request, "", context)