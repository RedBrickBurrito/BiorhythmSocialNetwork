from django.shortcuts import render, redirect
from .models import DailyBiorhythmChart

def HomePage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, 'biorhythm/home.html', {})

def BiorhythmChart(request):
    biorhythmchart = DailyBiorhythmChart
    context = {
        'chart': biorhythmchart,
    }
    return render(request, 'biorhythm/home.html', context)