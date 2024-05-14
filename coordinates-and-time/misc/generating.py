from datetime import datetime, timedelta

time_str_start = '2022-02-01T00:00:00Z'
time_str_end = '2022-02-10T00:00:00Z'
time = datetime.fromisoformat(time_str_start)
print(f'Start: {time_str_start}')
print(f'End:   {time_str_end}')

print(40*"-" + "\ndatetime.timedelta\n" + 40*"-")
delta = timedelta(days=1)
for i in range(10):
  print(time)
  time += delta
# or time = [time + delta for i in range(10)]

print(40*"-" + "\npandas.date_range\n" + 40*"-")
# https://pandas.pydata.org/docs/reference/api/pandas.date_range.html
import numpy as np
import pandas as pd
timestamp_range = pd.date_range(start=time_str_start, end=time_str_end)
for time in timestamp_range:
  #print(time.to_datetime64().astype(np.int64))
  print(time.to_pydatetime())

# https://numpy.org/doc/stable/reference/arrays.datetime.html
print(40*"-" + "\nNumPy datetime64\n" + 40*"-")
time_o = np.array('2022-02-02T00:00:00', dtype='datetime64[D]')
times = np.arange(time_o, time_o + 10, dtype='datetime64[D]')
for time in times:
  print(time)

# https://spacepy.github.io/autosummary/spacepy.time.tickrange.html#spacepy.time.tickrange
print(40*"-" + "\nspacepy.time.tickrange\n" + 40*"-")
import spacepy.time
times = spacepy.time.tickrange(time_str_start, time_str_end, deltadays=1, dtype=None)
for time in times:
  print(time.UTC[0])

# https://docs.sunpy.org/en/stable/generated/api/sunpy.time.TimeRange.html
#from sunpy.time import TimeRange
#time_range = TimeRange(time_str_start, time_str_end)
#print(time_range.get_dates())