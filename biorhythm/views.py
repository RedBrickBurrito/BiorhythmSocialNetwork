from django.shortcuts import render, redirect

def HomePage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, 'biorhythm/home.html', {})
