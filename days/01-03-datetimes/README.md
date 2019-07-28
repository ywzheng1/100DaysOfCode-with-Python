## Days 1 to 3

### Concept: datetime and date
Begin by importing datetime and date.
```
from datetime import datetime
from datetime import date

datetime.today()
datetime.datetime(2019, 7, 28, 13,38, 52, 133483)

date.today()
datetime.date(2019, 7, 28)

christmas = date(2019, 12, 25)
str((christams - todaydate).days)
```

----

### Concept: datetime timedelta
Begin by importing timedelta and set the timedelta length.
```
from datetime import timedelta

t = timedelta(days=4, hours=10)

t.Days
t.seconds
t.hous #fails

t.seconds / 60 / 60
#10.0

eta = timedelta(hours=6)
today = datetime.today()
eta = str(today + eta)
# 2019-07-28 23:48:47.412450
```
timedelta **only** works in days and seconds. Seconds' max is 24 hours a day.

It's possible to add/subtract timedeltas from datetimes.
