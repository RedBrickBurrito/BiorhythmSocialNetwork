from django.db import models
from pandas import array
from user.models import CustomUser
from numpy import array, sin, pi
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class DailyBiorhythmChart(models.Model):
    user = CustomUser.objects.get(id=1)
    date_now = datetime.datetime.now().date().toordinal()

    date_bd = user.birthday.toordinal()


    dates = array(range((date_now-10),(date_now+10))) #range of 20 days






