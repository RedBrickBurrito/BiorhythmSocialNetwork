from django.shortcuts import redirect, render
from user.models import CustomUser
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.hashers import make_password


class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")

def SignUpPage(request):
    context = {}
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = make_password(form.clean_password2())
            birthday = form.cleaned_data.get("birthday")
            image = form.cleaned_data.get("image")
            obj = CustomUser.objects.create(
                email = email,
                password = password, 
                birthday = birthday,
                image = image
            )
            obj.save()
            return redirect('/login/')
    else:
        form = CustomUserCreationForm()

    context["signup_form"] = form 
    return render(request, "user/signup.html", context)
