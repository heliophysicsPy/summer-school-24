import numpy as np
from scipy.integrate import solve_ivp

# Put options at the top. Once you have more than a few, it is time to refactor.
test = False
compare_methods = True
generate_lines = False

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
  By = 3*y*z/r**5
  Bz = (3*z**2 - r**2)/r**5
  return np.array([By, Bz])


def dipole_field_test():
  # Tests of dipole_field() based on hand calculations.
  # At (y, z) = (1, 0), the field should be (0, -1)
  assert np.all(dipole_field([1, 0]) - np.array([0, -1])) < 1e-15
  # At (y, z) = (-1, 0), the field should be (0, -1)
  assert np.all(dipole_field([-1, 0]) - np.array([0, -1])) < 1e-15
  # At (y, z) = (0, 1), the field should be (0, 3)
  assert np.all(dipole_field([-1, 0]) - np.array([0, 3])) < 1e-15
  # At (y, z) = (0, -1), the field should be (0, -3)
  assert np.all(dipole_field([-1, 0]) - np.array([0, 3])) < 1e-15


def trace(yz0, field_function, rtol=1e-3, s_eval=None, method='RK23'):

  def dXds(s, yz):
    field = field_function(yz)
    field_mag = np.linalg.norm(field)
    return (1/field_mag)*field

  if s_eval is None:
    s_eval = np.linspace(0, 1, 10)

  soln = solve_ivp(fun=dXds,
                  y0=yz0,
                  t_span=[s_eval[0], s_eval[-1]],
                  t_eval=s_eval,
                  rtol=rtol,
                  method=method)

  return soln.y


def const(yz):
  # See Walt, 1994, Introduction to Geomagnetically Trapped Radiation, pg 30
  # For dipole considered, an analytic result is that field lines follow a
  # path for which r/cos(latitude)^2 a constant.
  latitude = np.arctan2(yz[1], yz[0])
  return np.linalg.norm(yz)/np.cos(latitude)**2


def test():
  dipole_field_test()


def compare():
  ic = [1, 0] # Initial condition (y, z)
  s_eval = np.linspace(0, 1, 10)

  logger = logger_init()

  logger.info(f'Initial position: y = {ic[0]} z = {ic[1]}')
  logger.info(f'Length of traced field line: {s_eval[-1]}')

  logger.info('')

  logger.info(f'Start RK23')
  soln23 = trace(ic, dipole_field, method='RK23')
  logger.info(f'Finish RK23')

  logger.info(f'Start RK45')
  soln45 = trace(ic, dipole_field, method='RK45')
  logger.info(f'Finish RK45')

  logger.info(f'RK23 Final position: y = {soln23[0,-1]:>.16f} z = {soln23[1,-1]:>.16f}')
  logger.info(f'RK45 Final position: y = {soln45[0,-1]:>.16f} z = {soln45[1,-1]:>.16f}')

  logger.info('')
  logger.info('const ≡ r/cos(latitude)^2')
  logger.info(f'Initial const    = {const(ic)}')
  logger.info(f'RK23 final const = {const(soln23[:,-1])}')
  logger.info(f'RK45 final const = {const(soln45[:,-1])}')


def generate():
  s_eval = np.linspace(0, 1, 10)
  start_ys = np.arange(1, 16, 1)
  # Third dimension of lines is for each start y value
  lines = np.full((2, len(s_eval), len(start_ys)), np.nan)
  k = 0
  for y in start_ys:
    ic = [y, 0]
    soln45 = trace(ic, dipole_field, s_eval=s_eval, method='RK45')
    lines[:,:,k] = soln45
    k = k + 1
  return lines


if compare_methods == True:
  compare()

if test == True:
  dipole_field_test()

if generate_lines == True:
  lines = generate()
  np.save('data/lines.npy', lines)
