from django.shortcuts import render, redirect
from biorhythm.views import HomePage
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy(HomePage)