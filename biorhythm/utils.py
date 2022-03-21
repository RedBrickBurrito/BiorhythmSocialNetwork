from pandas import array
from numpy import array, sin, cos, pi
from datetime import date


def getBiorhythmLevels(user, date_range=[]):
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


def getBiorhythmCompat(birthday1, birthday2):
    t = birthday1.toordinal() - birthday2.toordinal()
    p_compat = cos((pi * t) / 23)
    e_compat = cos((pi * t) / 28)
    i_compat = cos((pi * t) / 33)
    mean = (p_compat + e_compat + i_compat) / 3

    return {
        "p_compat": round(p_compat, 4),
        "e_compat": round(e_compat, 4),
        "i_compat": round(i_compat, 4),
        "mean": round(mean * 100, 2)
    }


def getTop3Users(current_user, all_users):
    compat_info = []
    for user in all_users:
        if current_user == user:
            continue
        compat_info.append({"user": user, "compatibility": getBiorhythmCompat(
            current_user.birthday, user.birthday)})

    compat_info = sorted(compat_info, key=lambda x: x['compatibility']['mean'])
    compat_info.reverse()

    return compat_info[:3]


def getUserEvent(current_user, all_users, birthday):
    compat_info = []
    for user in all_users:
        if current_user == user:
            continue
        for date in birthday:
            compat_info.append(
                {"user": user, "compatibility": getBiorhythmCompat(date, user.birthday)})

    compat_info = sorted(compat_info, key=lambda x: x['compatibility']['mean'])
    compat_info.reverse()

    return compat_info[:1]
