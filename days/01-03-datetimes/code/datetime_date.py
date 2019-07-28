#! /usr/bin/env python3

from datetime import datetime
from datetime import date

datetime.today()

today = datetime.today()
# 2019-07-28 17:37:51.904041

type(today)
#<class 'datetime.datetime'>


todaydate = date.today()

todaydate
#datetime.date(2019, 7, 28)

type(todaydate)
#<class 'datetime.date'>

todaydate.month
#7

todaydate.year
#2019

todaydate.day
#28


christmas = date(2019, 7, 28)
christmas
#datetime.date(2019, 12, 25)

if christmas is not todaydate:
    print("Sorry there are still " + str((christmas - todaydate).days) + " until Christmas!")
else:
    print("Yay it's Christmas!")
