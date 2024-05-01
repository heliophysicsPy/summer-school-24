from datetime import datetime, timedelta

time_str_start = '2022-02-02T00:00:00Z'
time_str_end = '2022-02-11T00:00:00Z'
time = datetime.fromisoformat(time_str_start)

delta = timedelta(days=1)
for i in range(10):
  print(time)
  time += delta

# or time = [time + delta for i in range(10)]
print("---")

# https://pandas.pydata.org/docs/reference/api/pandas.date_range.html
import numpy as np
import pandas as pd
timestamp_range = pd.date_range(start=time_str_start, end=time_str_end)
for time in timestamp_range:
  print(time.to_datetime64().astype(np.int64))
  print(time.to_pydatetime())

# https://numpy.org/doc/stable/reference/arrays.datetime.html
time_o = np.array('2022-02-02T00:00:00',dtype='datetime64[D]')
times = np.arange(time_o, time_o + 10, dtype='datetime64[D]')
for time in times:
  print(time)

#print(time.astype(np.int64) - epoch.astype(np.int64))
#print(np.array([1,2],dtype='datetime64[D]'))
#print(np.array([1,2],dtype='datetime64[D]').astype(np.int64))

import spacepy.time as st
times = st.tickrange(time_str_start, time_str_end, deltadays=1, dtype=None)
for time in times:
  print(time.UTC[0])

#from sunpy.time import TimeRange
#time_range = TimeRange(time_str_start, time_str_end)
#print(time_range.get_dates())