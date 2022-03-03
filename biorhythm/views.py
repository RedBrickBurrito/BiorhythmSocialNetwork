from django.shortcuts import render
from .models import DailyBiorhythmChart

def HomePage(request, *args, **kwargs):
    return render(request, 'biorhythm/home.html', {})

def BiorhythmChart(request):
    biorhythmchart = DailyBiorhythmChart
    context = {
        'chart': biorhythmchart,
    }
    return render(request, 'biorhythm/home.html', context)