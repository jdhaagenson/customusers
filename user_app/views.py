# Create your views here.
from .models import CustomUser
from .forms import SignupForm, LoginForm
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


@login_required
def main(request):
    pass


def signup_form(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create_user(
                username=data.get('username'),
                password=data.get('password'),
                age=data.get('age'),
                display_name=data.get('display_name'),
                homepage=data.get('homepage')
            )
            user.save()
            if request.user.is_staff:
                return HttpResponseRedirect(request.GET.get('next'), reverse('homepage'))
    form = SignupForm()
    return render(request, 'signupform.html', {'form': form})


def login_form(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get('password'))