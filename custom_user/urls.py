"""custom_user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from user_app.views import login_form, logout_user, signup_form, main
from django.urls import path

urlpatterns = [
    path('', main, name='homepage'),
    path('loginpage/', login_form, name='loginpage'),
    path('logout/', logout_user, name='logout_user'),
    path('signup/', signup_form),
    path('admin/', admin.site.urls),
]
