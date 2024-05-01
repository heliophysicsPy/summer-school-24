from astropy.time import Time
# https://docs.astropy.org/en/stable/time/index.html

def logger_init():
  # Print to stdout and main.log
  import os
  import logging
  # TODO: Get base filename from __file__ in case this script name changes.
  if os.path.exists("main.log"):
    os.remove("main.log")
  handlers = [logging.FileHandler("main.log"), logging.StreamHandler()]
  format = '%(message)s'
  logging.basicConfig(level=logging.INFO, handlers=handlers, format=format)
  return logging.getLogger(__name__).info

log = logger_init()

time_string = '2000-01-01T00:00Z'
time_string = '2000-03-20T12:06:40Z'
#time_string = '2000-01-01T00:00:00Z'
time_object = Time(time_string, precision=9)

if False:
  # Basic usage
  t = t.tt   # https://docs.astropy.org/en/stable/time/index.html#id6
  val = t.jd # https://docs.astropy.org/en/stable/time/#time-format
  print(val)

# Print all formats and scales for t
log(f"\nTime: {time_object}\n")
maxlen = max([len(f) for f in list(Time.FORMATS.keys())])
log(f"Format        Scale Value")
log(f"------------------------------------------")
for FORMAT in [*list(Time.FORMATS.keys()),'jd1','jd2']:
  for SCALE in Time.SCALES:
    if SCALE == 'local': continue
    # Set scale. time_object = getattr(time_object, SCALE) is equivalent to doing
    #    time_object = time_object.SCALE
    # where SCALE is one of scales listed at
    # https://docs.astropy.org/en/stable/time/index.html#id6
    time_object = getattr(time_object, SCALE)

    # Set format. getattr(t, FORMAT) is equivalent to doing
    #    t = Time(time_string)
    #    val = t.format
    # where FORMAT is one of the formats listed at
    # https://docs.astropy.org/en/stable/time/#time-format
    val = getattr(time_object, FORMAT)

    log(f"{FORMAT:13} {SCALE:5} {val}") # https://docs.astropy.org/en/stable/time/#id6
