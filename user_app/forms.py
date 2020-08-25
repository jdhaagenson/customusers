import django.forms as forms


class SignupForm(forms.Form):
    display_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    age = forms.IntegerField(required=False)
    homepage = forms.URLField(required=False)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)





