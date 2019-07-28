from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)

type(t)
# <class 'datetime.timedelta'>

t.days
# 4

t.seconds
# 36000 (10 hours) - max is 1 day

t.seconds / 60 / 60
# 10.0 (hours)

t.seconds / 3600
# 10.0 (hours)


eta = timedelta(hours=6)

today = datetime.today()

eta = str(today + eta)
print(eta)
# 2019-07-28 23:48:47.412450
