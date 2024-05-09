import spacepy.time 
time_string = '2000-03-20T12:06:40Z'
time =  spacepy.time.Ticktock(time_string, 'ISO')
# SpacePy refers to the following as "systems". AstroPy has some as "formats" and
# others as "scales".
systems = ['CDF', 'ISO', 'UTC', 'TAI', 'GPS', 'UNX', 'JD', 'MJD', 'RDT', 'GPS', 'APT']
print(f"\nTime: {time_string}\n")
print(f"System   Value")
print(f"------------------------------------------")
for system in systems:
  print(f'{system}  {time.convert(system)}')
