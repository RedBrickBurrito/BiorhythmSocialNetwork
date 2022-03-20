import matplotlib.dates as mdates
import pandas as pd
import matplotlib.pyplot as plt
import base64
import io
import urllib, base64
from django.shortcuts import render
from datetime import date
from pylab import *
from user.models import CustomUser
from .utils import getBiorhythmLevels, getTop3Users

def getCurrentUser(request):
    # If there is a user logged in, get its info
    if request.user.id:
        return CustomUser.objects.get(id = request.user.id)

    # Load default user with id 1
    return CustomUser.objects.get(id = 1)


def DailyBiorhythmChart(user):
    t1 = date.today().toordinal()

    dates = array(range((t1-1),(t1+9))) #range of 10 days

    # Calculate biorhythm levels
    y = getBiorhythmLevels(user, dates)
    
    # append labels dates to each point in the chart
    label = []
    for p in dates:
        label.append(date.fromordinal(p))


    fig = figure()
    ax = fig.gca()

    plot(label, y[0], label, y[1], label, y[2])
    legend(['Physical', 'Emotional', 'Intellectual'])

    # plot horizontal line for zero 
    plt.axhline(y=0.0, color='black', linestyle=':')
    # plot vertical line indicating todays date
    xloc = mdates.DayLocator()

    # set x ticks spacing and rotation
    ax.xaxis.set_tick_params(rotation=90)
    ax.xaxis.set_major_locator(xloc)

    # formatting the dates on the x axis
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%m/%d'))

    ax.grid(True, linewidth=0.25)

    # save the chart in a buffer, to pass as a string
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return uri

def HomePage(request, *args, **kwargs):
    all_users = CustomUser.objects.all()
    user = getCurrentUser(request)
    context = {
        'data': DailyBiorhythmChart(user),
        'levels': getBiorhythmLevels(user),
    }
    return render(request, 'biorhythm/home.html', context)

def Top3(request):
    all_users = CustomUser.objects.all()
    user = getCurrentUser(request)
    context = {
        'top3': getTop3Users(user, all_users),
    }
    return render(request, 'biorhythm/top3.html', context)
