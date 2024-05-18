import numpy as np
from scipy.integrate import solve_ivp

# Put options at the top. Once you have more than a few, it is probably time to refactor.
test = False
compare_methods = True
generate_lines = True

def logger_init():
  # Print to stdout and main.log
  import os
  import logging
  # TODO: Get base filename from __file__ in case this script name changes.
  if os.path.exists("main.log"):
    os.remove("main.log")
  handlers = [logging.FileHandler("main.log"), logging.StreamHandler()]
  format = '%(asctime)s - %(message)s'
  logging.basicConfig(level=logging.INFO, handlers=handlers, format=format)
  return logging.getLogger(__name__)


def dipole_field(yz):
  y, z = yz
  r = np.linalg.norm(yz)
  # Cartesian form of dimensionless magnetic (or electric) field in y-z plane
  # due to ideal dipole at origin with moment pointing in z direction.
  # See Walt, 1994, Introduction to Geomagnetically Trapped Radiation, pg 30
  # (PDF in refs directory of this repository) for spherical form and
  # https://ccmc.gsfc.nasa.gov/RoR_WWW/presentations/Dipole.pdf
  By = 3*y*z/r**5
  Bz = (3*z**2 - r**2)/r**5
  return np.array([By, Bz])


def dipole_field_test():
  # Tests of dipole_field() based on hand calculations. Ideally one writes these
  # tests before writing the function.
  # At (y, z) = (1, 0), the field should be (0, -1)
  assert np.all(dipole_field([1, 0]) - np.array([0, -1])) < 1e-15
  # At (y, z) = (-1, 0), the field should be (0, -1)
  assert np.all(dipole_field([-1, 0]) - np.array([0, -1])) < 1e-15
  # At (y, z) = (0, 1), the field should be (0, 3)
  assert np.all(dipole_field([-1, 0]) - np.array([0, 3])) < 1e-15
  # At (y, z) = (0, -1), the field should be (0, -3)
  assert np.all(dipole_field([-1, 0]) - np.array([0, 3])) < 1e-15


def trace(field_function, yz0, events=None, rtol=1e-3, s_eval=None, method='RK23'):

  def dXds(s, yz):
    # Return the RHS of a system of ODEs in the form dX/ds = F(s, X)
    # where X = [y, z]
    # In 2-D (y, z), the system of ODEs for a field line are
    #   dy/ds = By/B
    #   dz/ds = By/B
    field = field_function(yz) # Returns Bx(y, z), By(y, z)
    field_mag = np.linalg.norm(field)
    return (1/field_mag)*field

  if s_eval is None:
    s_eval = np.linspace(0, 2, 100)

  # https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html
  kwargs = {
              "fun": dXds,
              "y0": yz0,
              "t_span": [s_eval[0], s_eval[-1]],
              "t_eval": s_eval,
              "events": events,
              "rtol": rtol,
              "method": method
  }
  soln = solve_ivp(**kwargs)

  return soln


def const(yz):
  # See Walt, 1994, Introduction to Geomagnetically Trapped Radiation, pg 30
  # (PDF in refs directory of this repository). For dipole considered, an 
  # analytic result is that field lines follow a path for which 
  # r/cos(latitude)^2 a constant.
  latitude = np.arctan2(yz[1], yz[0])
  return np.linalg.norm(yz)/np.cos(latitude)**2


def test():
  dipole_field_test()


def compare():

  def cross_equator(s, yz):
    return yz[1]
  cross_equator.terminal = True

  ic = [1, 1] # Initial condition (y, z)
  s_eval = np.linspace(0, 3, 10)

  logger.info(f'Initial position: (x, y) = ({ic[0]}, {ic[1]})')

  rtol = 1e-3
  logger.info(f'Using rtol = {rtol}')

  logger.info('')

  logger.info(f'Start RK23')
  soln23 = trace(dipole_field, ic, events=cross_equator, rtol=rtol, s_eval=s_eval, method='RK23')
  logger.info(f'Finish RK23')

  logger.info(f'Start RK45')
  soln45 = trace(dipole_field, ic, events=cross_equator, rtol=rtol, s_eval=s_eval, method='RK45')
  logger.info(f'Finish RK45')

  stop_yz23 = soln23.y_events[0][0]
  stop_yz45 = soln45.y_events[0][0]

  logger.info(f'RK23 Stop position: y = {stop_yz23[0]:.6f} z = {stop_yz23[1]:>9.2e}')
  logger.info(f'RK45 Stop position: y = {stop_yz45[0]:.6f} z = {stop_yz45[1]:>9.2e}')

  logger.info(f'y difference: {6371*abs(stop_yz23[0] - stop_yz45[0]):.0f} [km]')

  logger.info('')
  logger.info('const ≡ r/cos(latitude)^2')
  logger.info(f'Initial const   = {const(ic):.8f}')
  logger.info(f'RK23 stop const = {const(stop_yz23):.8f}')
  logger.info(f'RK45 stop const = {const(stop_yz45):.8f}')


def generate():

  s_eval = np.linspace(0, 2, 5)
  n_lines = 5
  start_thetas = np.linspace(np.pi/5, np.pi/2 - np.pi/5, n_lines)
  starts = 1.01*np.array([np.cos(start_thetas), np.sin(start_thetas)]).T

  # Third dimension of lines is for each start y value
  lines = np.full((2, len(s_eval), n_lines), np.nan)
  k = 0
  for ic in starts:
    soln45 = trace(dipole_field, ic, s_eval=s_eval, method='RK45')
    lines[:,:,k] = soln45.y
    logger.info(f'Line {k}\n{lines[:,:,k]}')
    k = k + 1
  return lines


logger = logger_init()

if compare_methods == True:
  compare()

if test == True:
  dipole_field_test()

if generate_lines == True:
  lines = generate()

  # Option 1 for saving data: NumPy's save function
  fname = 'data/lines.npy'
  logger.info(f'Writing {fname}')
  np.save(fname, lines)
  logger.info(f'Wrote {fname}')

  # Option 2 for saving data: CSV
  # If there is any reason that we would want to inspect the numbers, save each
  # field line in a separate CSV file.
  for i in range(lines.shape[2]):
    fname = f'data/line_{i}.csv'
    np.savetxt(fname, lines[:,:,i], delimiter=',')
    logger.info(f'Wrote {fname}')

  # For discussion:
  #  1. What are the pros and cons of each option?
  #  2. What about pkl file, HDF5, or CDF?
