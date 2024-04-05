**Time and Space Transformations**

_Wednesday, May 22nd, 9:05-9:55 Mountain Time_

Target audience: Students with limited experience with

* manipulation and transformation of time representations and
* transforming data between Heliophysics coordinate systems

Examples are given using native Python libraries and PyHC packages.

# Time Transformations

## Overview

### Parsing

* UTC, datetime, and pytz
* SpacePy Ticktock
* SunPy

## Transforming

### Plotting

* Matplotlib time axes
  * astropy time_support
  * spacepy/plot/utils.py
  * [hapiplot](https://github.com/hapi-server/plot-python/blob/main/hapiplot/plot/datetick.py)
  * [pytplot](https://pypi.org/project/pytplot-mpl-temp/)
  * [geospacelab](https://github.com/JouleCai/geospacelab)

## Problems

### Parsing

### Transforming

### Plotting

# Space Transformations

## Overview

Three main approaches:

1. Custom library: SpacePy, SunPy, etc. More often used by scientists.
2. SPICE: Not covered; more often used by instrument teams. Should mention that there are often training opportunities w/ NAIF.
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

