import django.forms as forms
from .models import CustomUser


class SignupForm(forms.ModelForm):
    email = forms.EmailField(max_length=50, help_text="Required. Please enter valid email address")
    homepage = forms.URLField(required=False, help_text="Optional")
    age = forms.IntegerField(required=False, help_text="Optional")
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("email", 'username', 'display_name', 'age', 'homepage', 'password')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)





