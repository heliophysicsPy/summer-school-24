import spacepy.time as spt
import spacepy.coordinates as spc
import spacepy.irbempy as irbem

extMag = '0'
# extMag described at https://spacepy.github.io/irbempy.html
# Possible values are '0', 'MEAD', 'T87SHORT', 'T87LONG', 'T89', 'OPQUIET',
# 'OPDYN', 'T96', 'OSTA', 'T01QUIET', 'T01STORM', 'T05', 'ALEX', and 'TS07'.

options = [0, 0, 0, 0, 1]

# options described at https://spacepy.github.io/irbempy.html
# 5th element sets internal magnetic field model
# 0 = IGRF
# 1 = Eccentric tilted dipole
# 2 = Jensen & Cain 1960
# 3 = GSFC 12/66 updated to 1970
# 4 = User-defined model (Default: Centred dipole + uniform [Dungey open model] )
# 5 = Centred dipole

t = spt.Ticktock(['2002-02-02T12:00:00'], 'ISO')
y = spc.Coords([3, 0, 0], 'GEO', 'car', use_irbem=True)
B = irbem.get_Bfield(t, y, extMag=extMag, options=options)

print(B)
