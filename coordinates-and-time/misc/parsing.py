import datetime
import pandas
import ciso8601

times = ['2001-01-01T00Z','2001-001T00Z']

for time in times:
  print(36*'-')
  print(f'Input: {time}')
  print(36*'-')
  try:
    dt = pandas.to_datetime(time)
    print(f'pandas.to_datetime:      {dt}')
  except:
    print(f'pandas.to_datetime:      failed')
    dt = None

  try:
    dt = datetime.datetime.fromisoformat(time)
    print(f'datetime.fromisoformat:  {dt}')
  except:
    print(f'datetime.fromisoformat   failed')
    dt = None

  try:
    dt = ciso8601.parse_datetime(time)
    print(f'ciso8601.parse_datetime: {dt}')
  except:
    print(f'ciso8601.parse_datetime  failed')
    dt = None
