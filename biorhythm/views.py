from django.shortcuts import render
from pandas import array
import pandas as pd
from user.models import CustomUser
from numpy import array, sin, pi
from datetime import date, timedelta
import matplotlib.pyplot as plt
import base64
import io
from pylab import *
import urllib, base64
import matplotlib.dates as mdates

def DailyBiorhythmChart():
    user = CustomUser.objects.get(id=1)

    date_bd = user.birthday

    t0 = date_bd.toordinal()
    t1 = date.today().toordinal()

    dates = array(range((t1-1),(t1+9))) #range of 10 days

    # Calculate biorhythm levels
    y = (sin(2*pi*(dates-t0)/23),   # Physical
        sin(2*pi*(dates-t0)/28),   # Emotional
        sin(2*pi*(dates-t0)/33))   # Intellectual
    
    # append labels dates to each point in the chart
    label = []
    for p in dates:
        label.append(date.fromordinal(p))


    fig = figure(facecolor='#E5E5E5')
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

    ax.set_facecolor('#E5E5E5')

    # save the chart in a buffer, to pass as a string
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return uri

def getCurrentBiorhythmLevels():
    user = CustomUser.objects.get(id=1)

    date_bd = user.birthday

    t0 = date_bd.toordinal()
    t1 = (date.today() - timedelta(days=1)).toordinal()

    # Calculate biorhythm levels
    y = (sin(2*pi*(t1-t0)/23),   # Physical
        sin(2*pi*(t1-t0)/28),   # Emotional
        sin(2*pi*(t1-t0)/33))   # Intellectual
    
    return y

def HomePage(request, *args, **kwargs):
    context = {
        'data': DailyBiorhythmChart(),
        'levels': getCurrentBiorhythmLevels(),
    }
    return render(request, 'biorhythm/home.html', context)
