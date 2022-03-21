from distutils.log import debug
from django.shortcuts import get_object_or_404, render, redirect
from pandas import array
import matplotlib.dates as mdates
from biorhythm.forms import CreateEventForm
from user.models import CustomUser
from .models import Event
from numpy import array, sin, pi
from datetime import date, timedelta
import matplotlib.pyplot as plt
import base64
import io
import urllib
import base64
from django.shortcuts import render
from datetime import date
from pylab import *
from user.models import CustomUser
from .utils import getBiorhythmLevels, getTop3Users, getUserEvent
from . import forms

birthdayForEvent = datetime.date.today()


def getCurrentUser(request):
    # If there is a user logged in, get its info
    if request.user.id:
        return CustomUser.objects.get(id=request.user.id)

    # Load default user with id 1
    return CustomUser.objects.get(id=1)


def getCurrentEvent(request):
    if request.user.id:
        return Event.objects.get(id=request.user.id)


def DailyBiorhythmChart(user):
    t1 = date.today().toordinal()

    dates = array(range((t1-1), (t1+9)))  # range of 10 days

    # Calculate biorhythm levels
    y = getBiorhythmLevels(user, dates)

    # append labels dates to each point in the chart
    label = []
    for p in dates:
        label.append(date.fromordinal(p))

    fig = figure(facecolor='#ffffff')
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

    ax.set_facecolor('#ffffff')

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
    user = getCurrentUser(request)
    context = {
        'data': DailyBiorhythmChart(user),
        'levels': getCurrentBiorhythmLevels(),
    }
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request, 'biorhythm/home.html', context)


def Top3(request):
    all_users = CustomUser.objects.all()
    user = getCurrentUser(request)
    context = {
        'top3': getTop3Users(user, all_users),
    }
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, 'biorhythm/top3.html', context)


def CreateEvent(request):
    if(request.method == 'POST'):
        form = CreateEventForm(request.POST)
        if(form.is_valid()):
            instance = form.save(commit=False)
            instance.customUser = request.user
            instance.save()
            return redirect('result-event')
    else:
        form = CreateEventForm()
    context = {
        'form': form
    }
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, 'biorhythm/createEvent.html', context)


def ResultEvent(request):
    print('Result Event')
    print(birthdayForEvent)
    all_users = CustomUser.objects.all()
    user = getCurrentUser(request)
    events = Event.objects.all()
    dates = Event.objects.filter().values_list('date', flat=True)
    dates_list = list(dates)

    context = {
        'events': events,
        'resultOfEvent': getUserEvent(user, all_users, dates_list),

    }
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, 'biorhythm/resultEvent.html', context)


def DeleteEvent(request, event_id):  # PROBLEMAS
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect("result-event")


def EditEvent(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = CreateEventForm(request.POST or None, instance=event)
    if(form.is_valid()):
        form.save()
        return redirect("result-event")

    context = {
        "object": event,
        "form": form
    }
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request, "biorhythm/editEvent.html", context)
