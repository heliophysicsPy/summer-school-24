**Time and Space Transformations**

_Wednesday, May 22nd, 9:05-9:55 and 10:05-10:55 Mountain Time_

Target audience: Students with limited experience with

* manipulation and transformation of time representations and
* transforming data between Heliophysics coordinate systems

Examples are given using native Python libraries and PyHC packages.

# Time Transformations

_9:05-9:55 Mountain Time_

## Parsing

### Known Time String Format

The most common task is to parse an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time string into a Python `datetime` object. (`datetime` can also parse non--ISO 8601 time strings).

If you know the format of the time string and it has millisecond precision or less, a reliable approach it to use [`datetime.strptime`](https://docs.python.org/3/library/datetime.html). For example,

```python
import datetime 
dt = datetime.datetime.strptime("2008-09-03T20:56:35.450686Z", "%Y-%m-%dT%H:%M:%S.%fZ")
print(dt)
dt = datetime.datetime.strptime("2008-09-03T20:56:35.450Z", "%Y-%m-%dT%H:%M:%S.%fZ")
print(dt)
dt = datetime.datetime.strptime("2008-09-03T20:56:35Z", "%Y-%m-%dT%H:%M:%SZ")
print(dt)
dt = datetime.datetime.strptime("2008-09-03T20:56:35.Z", "%Y-%m-%dT%H:%M:%S.Z")
print(dt)

dt = datetime.datetime.strptime("2008-002T20:56:35.450686Z", "%Y-%jT%H:%M:%S.%fZ")
print(dt)
```

For precisions higher than millisecond, [NumPy's datetime64](https://numpy.org/doc/stable/reference/arrays.datetime.html) can be used.

### Unknown Time String Format

[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is a complex standard. If you have to parse a time string and don't know its format beyond "ISO 8601", you are likely to run into issues because not all packages fully implement the standard. For example, Pandas does not parse `2001-001T00Z`.

Parsers in the PyHC community:

* https://spacepy.github.io/_modules/spacepy/time.html#Ticktock
* https://docs.sunpy.org/en/stable/how_to/parse_time.html
* https://docs.astropy.org/en/stable/api/astropy.time.Time.html#astropy.time.Time

And some code samples:

* https://github.com/spacepy/spacepy/blob/main/spacepy/time.py#L1931
* https://github.com/hapi-server/client-python/blob/master/hapiclient/hapitime.py#L166

References
* https://stackoverflow.com/questions/127803/how-do-i-parse-an-iso-8601-formatted-date-and-time
* https://wiki.python.org/moin/WorkingWithTime
* comprehensive list of Python packages that deal with ISO 8601 at https://github.com/closeio/ciso8601

## Generating

A common task is to generate a list of timestamps that can be used, for plotting.

## Transforming

## Plotting

* Matplotlib time axes
* AstroPy time_support
* spacepy/plot/utils.py
* [hapiplot](https://github.com/hapi-server/plot-python/blob/main/hapiplot/plot/datetick.py)
* [pytplot](https://pypi.org/project/pytplot-mpl-temp/)
* [geospacelab](https://github.com/JouleCai/geospacelab)

## Problems

### Parsing

### Generating

### Transforming

### Plotting

# Space Transformations

_10:05-10:55 Mountain Time_

## Overview

Three main approaches:

1. Custom library: SpacePy, SunPy, etc. More often used by scientists.
2. SPICE: Not covered; more often used by instrument teams. Should mention that there are often training opportunities with NAIF.
3. Web site, e.g.
   * [LAMBDA](https://lambda.gsfc.nasa.gov/toolbox/converters.html)
   * [TREPS](https://treps.irap.omp.eu/)
   * [Geomagnetic Coordinate Calculator](https://geomag.bgs.ac.uk/data_service/models_compass/coord_calc.html)
   * [AACGM-v2 Coordinate Transformations](https://sdnet.thayer.dartmouth.edu/aacgm/aacgm_calc.php)
   * [NOAA Magnetic Field Calculators](https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml)
   * [Kyoto Geographic <=> Geomagnetic (IGRF)](https://wdc.kugi.kyoto-u.ac.jp/igrf/gggm/)

## Review of coordinate transforms

Give examples of doing transforms with at least two packages.

## Problems

1. Computing dipole tilt. Problem involving plotting over the course of a year. Discussion of interpretation.

2. Transforming a unit vector from GSE to GSM and plotting over the course of a year. Discussion of interpretation.

3. Conversion from helioprojective (100 arcsec in x, 100 arcsec in y) to heliographic (lat long) (stonyhurst or carrington)
