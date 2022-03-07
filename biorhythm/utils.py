from pandas import array
from numpy import array, sin, pi
from datetime import date

def getBiorhythmLevels(user, date_range = []):
    date_bd = user.birthday
    t0 = date_bd.toordinal()
    y = None

    # Calculate biorhythm levels
    if len(date_range) > 0:
        y = (sin(2*pi*(date_range-t0)/23),   # Physical
        sin(2*pi*(date_range-t0)/28),   # Emotional
        sin(2*pi*(date_range-t0)/33))   # Intellectual
    else:
        t0 = date_bd.toordinal()
        t1 = date.today().toordinal()

        y = (sin(2*pi*(t1-t0)/23),   # Physical
            sin(2*pi*(t1-t0)/28),   # Emotional
            sin(2*pi*(t1-t0)/33))   # Intellectual
    
    return y
