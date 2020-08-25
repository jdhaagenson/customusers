# Create your views here.
from .models import CustomUser
from .forms import SignupForm, LoginForm
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from custom_user.settings import AUTH_USER_MODEL


@login_required
def main(request):
    return render(request, 'main.html', {'auth_user_model': AUTH_USER_MODEL, 'user': request.user})


def signup_form(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        # breakpoint()
        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create_user(
                email=data.get('email'),
                username=data.get('username'),
                password=data.get('password'),
                age=data.get('age'),
                display_name=data.get('display_name'),
                homepage=data.get('homepage')
            )
            return HttpResponseRedirect(request.GET.get('next', reverse('loginpage')))
    form = SignupForm()
    return render(request, 'generic_form.html', {'form': form})


def login_form(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(
                request,
                username=username,
                password=raw_password
            )
            # breakpoint()
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage')))
    form = LoginForm()
    return render(request, "generic_form.html", {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))


