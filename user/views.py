from django.shortcuts import redirect, render
from user.models import CustomUser

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView

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
            password = form.clean_password2()
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

    context["form"] = form 
    return render(request, "user/signup.html", context)
