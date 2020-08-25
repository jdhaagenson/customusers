import django.forms as forms


class SignupForm(forms.Form):
    display_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    Email = forms.EmailField(required=False)
    Age = forms.IntegerField(required=False)
    Homepage = forms.URLField(required=False)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)





