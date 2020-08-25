import django.forms as forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text="Required. Please enter valid email address")

    class Meta:
        model = CustomUser
        fields = ("email", 'username', 'password', 'display_name', 'age', 'homepage')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)





