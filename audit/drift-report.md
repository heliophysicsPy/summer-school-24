# Drift Audit Report

- Generated: 2026-04-10 17:20 UTC
- Audit branch: `2026-updates` in `/Users/shpo9723/git/summer-school-24`
- Runtime env: `pyhc-all` with an isolated `PYTHONUSERBASE` overlay
- Artifacts audited: 37
- Findings recorded: 155

## Package Revisions

| Package | Branch | SHA | Source |
| --- | --- | --- | --- |
| `apexpy` | `main` | `ebc4761dfdb9` | `/Users/shpo9723/git/pyhc-chat-cli/pyhc_packages/apexpy` |
| `client-python` | `master` | `ca2d3cdba329` | `/Users/shpo9723/git/client-python` |
| `hapiplot` | `main` | `47eaded3d812` | `https://github.com/hapi-server/plot-python.git` |
| `PlasmaPy` | `main` | `3a7835201d57` | `/Users/shpo9723/git/PlasmaPy` |
| `pysat` | `main` | `3f0e5a43ad36` | `/Users/shpo9723/git/pysat` |
| `pysatMadrigal` | `main` | `e07ca366d341` | `https://github.com/pysat/pysatMadrigal.git` |
| `pysatMissions` | `main` | `7eae852d6238` | `https://github.com/pysat/pysatMissions.git` |
| `pysatNASA` | `main` | `a75df9ac6e43` | `https://github.com/pysat/pysatNASA.git` |
| `pysatSeasons` | `main` | `82a76e05bbeb` | `https://github.com/pysat/pysatSeasons.git` |
| `pysatSpaceWeather` | `main` | `e36d39d60ed7` | `https://github.com/pysat/pysatSpaceWeather.git` |
| `pyspedas` | `master` | `e4a634109a81` | `/Users/shpo9723/git/pyspedas` |
| `PyTplot` | `master` | `f7fb3042898a` | `/Users/shpo9723/git/pyhc-chat-cli/pyhc_packages/PyTplot` |
| `solarmach` | `main` | `1c6572e77257` | `/Users/shpo9723/git/pyhc-chat-cli/pyhc_packages/solarmach` |
| `spacepy` | `main` | `cb983af96e06` | `/Users/shpo9723/git/spacepy` |
| `stixpy` | `main` | `4f4e0c7d7d14` | `https://github.com/TCDSolar/stixpy.git` |
| `sunpy` | `main` | `e06e0743c0de` | `/Users/shpo9723/git/sunpy` |

## Runtime Smoke Check

- `sunpy`: ok
- `spacepy`: ok
- `pysat`: ok
- `plasmapy`: ok
- `pyspedas`: ok
- `hapiclient`: ok
- `pytplot`: ok
- `apexpy`: ok
- `solarmach`: ok
- `pysatNASA`: ok
- `pysatMissions`: failed - ModuleNotFoundError("No module named 'ephem'")
- `pysatSeasons`: ok
- `pysatSpaceWeather`: ok
- `pysatMadrigal`: ok
- `stixpy`: failed - ModuleNotFoundError("No module named 'stixpy'")
- `hapiplot`: ok

## Execution Matrix

| Artifact | Kind | Result | Detail |
| --- | --- | --- | --- |
| `sunpy-tutorial/sunpy-tutorial/part-0-introduction.ipynb` | `notebook` | `executed` | Notebook executed successfully. |
| `sunpy-tutorial/sunpy-tutorial/part-1-sunpy.ipynb` | `notebook` | `failed` | cell 19 |
| `sunpy-tutorial/sunpy-tutorial/part-1-sunpy-instructor-version.ipynb` | `notebook` | `failed` | cell 19 |
| `sunpy-tutorial/sunpy-pyspedas-showcase/sunpy-pyspedas-demo.ipynb` | `notebook` | `failed` | cell 58 |
| `spacepy-tutorial/SpacePy - Cusp energetic particles.md` | `markdown` | `failed` | code fence 3 (line 94) |
| `spacepy-tutorial/SpacePy - Cutoff Rigidities.md` | `markdown` | `failed` | code fence 3 (line 62) |
| `spacepy-tutorial/SpacePy - MMS Ephemeris.md` | `markdown` | `failed` | code fence 2 (line 47) |
| `spacepy-tutorial/SpacePy - SWMF Dynamics.md` | `markdown` | `failed` | code fence 3 (line 82) |
| `pysat-tutorial/00 - ACE SWEPAM Demonstration.ipynb` | `notebook` | `failed` | cell 3 |
| `pysat-tutorial/01 - ACE SIS Customization.ipynb` | `notebook` | `failed` | cell 3 |
| `pysat-tutorial/02 - DMSP Polar Ion Drifts.ipynb` | `notebook` | `failed` | cell 3 |
| `pysat-tutorial/03 - ICON IVM Demonstration.ipynb` | `notebook` | `failed` | cell 4 |
| `pysat-tutorial/04 - ICON MIGHTI Demonstration.ipynb` | `notebook` | `failed` | cell 4 |
| `pysat-tutorial/05 - pysat Creating netCDF4 Files.ipynb` | `notebook` | `failed` | cell 4 |
| `pysat-tutorial/06 - pysatMissions.ipynb` | `notebook` | `failed` | cell 3 |
| `pysat-tutorial/07 - pysatSeasons Bin Averaging.ipynb` | `notebook` | `failed` | cell 4 |
| `pysat-tutorial/08 - pysatSeasons Occurrence Probability.ipynb` | `notebook` | `failed` | cell 4 |
| `pysat-tutorial/09 - pysat Loading.ipynb` | `notebook` | `failed` | cell 4 |
| `pysat-tutorial/10 - pysat Iteration.ipynb` | `notebook` | `failed` | cell 4 |
| `pysat-tutorial/11 - pysat Instantiation and Parameters.ipynb` | `notebook` | `failed` | cell 4 |
| `pysat-tutorial/12 - pyast Data Access and Assignment.ipynb` | `notebook` | `failed` | cell 4 |
| `plasmapy-tutorial/plasmapy-tutorial.ipynb` | `notebook` | `executed` | Notebook executed successfully. |
| `plasmapy-tutorial/plasmapy-tutorial-completed.ipynb` | `notebook` | `executed` | Notebook executed successfully. |
| `pyspedas-tutorial/Finding_Magnetic_Nulls_MMS_20230324.ipynb` | `notebook` | `failed` | cell 6 |
| `pyspedas-tutorial/Generate_2D_slices_of_MMS_FPI_data.ipynb` | `notebook` | `failed` | cell 9 |
| `pyspedas-tutorial/Introduction_to_PySPEDAS.ipynb` | `notebook` | `failed` | cell 11 |
| `pyspedas-tutorial/MMS, THEMIS, Arase orbits 2023-03-24.ipynb` | `notebook` | `failed` | cell 6 |
| `pyspedas-tutorial/MMS_summary_plot_20230324.ipynb` | `notebook` | `executed` | Notebook executed successfully. |
| `pyspedas-tutorial/Magnetic_Field_Modeling.ipynb` | `notebook` | `failed` | cell 5 |
| `pyspedas-tutorial/PyTplot_range_options.ipynb` | `notebook` | `failed` | cell 4 |
| `pyspedas-tutorial/PyTplot_variable_options.ipynb` | `notebook` | `failed` | cell 4 |
| `pyspedas-tutorial/Working_with_dates_and_times_with_PySPEDAS_PyTplot.ipynb` | `notebook` | `executed` | Notebook executed successfully. |
| `hapi-tutorial/HAPI_00.ipynb` | `notebook` | `executed` | Notebook executed successfully. |
| `hapi-tutorial/HAPI_01.ipynb` | `notebook` | `failed` | runtime |
| `hapi-tutorial/HAPI_02.ipynb` | `notebook` | `executed` | Notebook executed successfully. |
| `hapi-tutorial/HAPI_03.ipynb` | `notebook` | `failed` | cell 27 |
| `hapi-tutorial/HAPI_04.ipynb` | `notebook` | `executed` | Notebook executed successfully. |

## Findings

### Blocking

- `hapi-tutorial/HAPI_03.ipynb` cell 27 `pyspedas`: Import statement `from pyspedas.hapi.hapi import hapi as pyhapi` fails against the current audit environment. ModuleNotFoundError: No module named 'pyspedas.hapi' Current source candidates: pyspedas/hapi_tools/hapi.py
- `hapi-tutorial/HAPI_03.ipynb` cell 27: Notebook execution failed. 
- `pysat-tutorial/06 - pysatMissions.ipynb` cell 3 `pysatMissions`: Import statement `import pysatMissions` fails against the current audit environment. ModuleNotFoundError: No module named 'ephem'
- `pysat-tutorial/06 - pysatMissions.ipynb` cell 3: Notebook execution failed. 
- `sunpy-tutorial/sunpy-pyspedas-showcase/sunpy-pyspedas-demo.ipynb` cell 58 `stixpy`: Import statement `from stixpy.net.client import STIXClient` fails against the current audit environment. ModuleNotFoundError: No module named 'stixpy' Current source candidates: stixpy/net/client.py
- `sunpy-tutorial/sunpy-pyspedas-showcase/sunpy-pyspedas-demo.ipynb` cell 58: Notebook execution failed. 
- `sunpy-tutorial/sunpy-pyspedas-showcase/sunpy-pyspedas-demo.ipynb` cell 63 `stixpy`: Import statement `from stixpy.timeseries import quicklook` fails against the current audit environment. ModuleNotFoundError: No module named 'stixpy'
- `sunpy-tutorial/sunpy-pyspedas-showcase/sunpy-pyspedas-demo.ipynb` cell 81 `sunpy_soar`: Import statement `import sunpy_soar` fails against the current audit environment. ModuleNotFoundError: No module named 'sunpy_soar'
### High-Risk

- `hapi-tutorial/HAPI_01.ipynb` runtime: Notebook execution failed. 
- `pysat-tutorial/00 - ACE SWEPAM Demonstration.ipynb` cell 3: Notebook execution failed. 
- `pysat-tutorial/01 - ACE SIS Customization.ipynb` cell 3: Notebook execution failed. 
- `pysat-tutorial/02 - DMSP Polar Ion Drifts.ipynb` cell 3: Notebook execution failed. 
- `pysat-tutorial/03 - ICON IVM Demonstration.ipynb` cell 4: Notebook execution failed. 
- `pysat-tutorial/04 - ICON MIGHTI Demonstration.ipynb` cell 4: Notebook execution failed. 
- `pysat-tutorial/05 - pysat Creating netCDF4 Files.ipynb` cell 4: Notebook execution failed. 
- `pysat-tutorial/07 - pysatSeasons Bin Averaging.ipynb` cell 4: Notebook execution failed. 
- `pysat-tutorial/08 - pysatSeasons Occurrence Probability.ipynb` cell 4: Notebook execution failed. 
- `pysat-tutorial/09 - pysat Loading.ipynb` cell 4: Notebook execution failed. 
- `pysat-tutorial/10 - pysat Iteration.ipynb` cell 4: Notebook execution failed. 
- `pysat-tutorial/11 - pysat Instantiation and Parameters.ipynb` cell 4: Notebook execution failed. 
- `pysat-tutorial/12 - pyast Data Access and Assignment.ipynb` cell 4: Notebook execution failed. 
- `pyspedas-tutorial/Finding_Magnetic_Nulls_MMS_20230324.ipynb` cell 6: Notebook execution failed. 
- `pyspedas-tutorial/Generate_2D_slices_of_MMS_FPI_data.ipynb` cell 9: Notebook execution failed. 
- `pyspedas-tutorial/PyTplot_range_options.ipynb` cell 4: Notebook execution failed. 
- `spacepy-tutorial/SpacePy - Cusp energetic particles.md` code fence 3 (line 94): Markdown snippet execution failed. OSError: [Errno 45] Operation not supported: '/home/jovyan'
- `spacepy-tutorial/SpacePy - Cutoff Rigidities.md` code fence 3 (line 62): Markdown snippet execution failed. OSError: [Errno 45] Operation not supported: '/home/jovyan'
- `spacepy-tutorial/SpacePy - MMS Ephemeris.md` code fence 2 (line 47): Markdown snippet execution failed. OSError: [Errno 45] Operation not supported: '/home/jovyan'
- `spacepy-tutorial/SpacePy - SWMF Dynamics.md` code fence 3 (line 82): Markdown snippet execution failed. SyntaxError: invalid syntax
- `sunpy-tutorial/sunpy-tutorial/part-1-sunpy-instructor-version.ipynb` cell 19: Notebook execution failed. 
- `sunpy-tutorial/sunpy-tutorial/part-1-sunpy.ipynb` cell 19: Notebook execution failed. 
### Medium

- `hapi-tutorial/HAPI_00.ipynb` cell 1: Artifact references plain HTTP endpoint `http://SERVER/hapi/data?dataset=DATASET&parameters=PARAMETERS&start=START&stop=STOP`. cell 1 contains `http://SERVER/hapi/data?dataset=DATASET&parameters=PARAMETERS&start=START&stop=STOP`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `hapi-tutorial/HAPI_00.ipynb` cell 1: Artifact references plain HTTP endpoint `http://github.com/hapi-server/`. cell 1 contains `http://github.com/hapi-server/`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `hapi-tutorial/HAPI_00.ipynb` cell 1: Artifact references plain HTTP endpoint `http://hapi-server.org/`. cell 1 contains `http://hapi-server.org/`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `hapi-tutorial/HAPI_00.ipynb` cell 1: Artifact references plain HTTP endpoint `http://hapi-server.org/servers/,`. cell 1 contains `http://hapi-server.org/servers/,`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `hapi-tutorial/HAPI_00.ipynb` cell 1: Artifact references plain HTTP endpoint `http://hapi-server.org/servers`. cell 1 contains `http://hapi-server.org/servers`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `hapi-tutorial/HAPI_01.ipynb` cell 20: Artifact references plain HTTP endpoint `http://cdaweb.gsfc.nasa.gov/hapi`. cell 20 contains `http://cdaweb.gsfc.nasa.gov/hapi`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `hapi-tutorial/HAPI_01.ipynb` cell 25: Artifact references plain HTTP endpoint `http://cdaweb.gsfc.nasa.gov/hapi`. cell 25 contains `http://cdaweb.gsfc.nasa.gov/hapi`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `hapi-tutorial/HAPI_01.ipynb` cell 9 output: Artifact references plain HTTP endpoint `http://hapi-server.org/servers/TestData2.0/hapi`. cell 9 output contains `http://hapi-server.org/servers/TestData2.0/hapi`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `hapi-tutorial/HAPI_02.ipynb` cell 28: Artifact references plain HTTP endpoint `http://hapi-server.org/servers/TestData2.0/hapi`. cell 28 contains `http://hapi-server.org/servers/TestData2.0/hapi`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `hapi-tutorial/HAPI_02.ipynb` cell 6: Artifact references plain HTTP endpoint `http://hapi-server.org/servers/TestData2.0/hapi`. cell 6 contains `http://hapi-server.org/servers/TestData2.0/hapi`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `hapi-tutorial/HAPI_03.ipynb` cell 14: Artifact references plain HTTP endpoint `http://datashop.elasticbeanstalk.com/hapi`. cell 14 contains `http://datashop.elasticbeanstalk.com/hapi`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `hapi-tutorial/HAPI_03.ipynb` cell 18: Artifact references plain HTTP endpoint `http://hapi-server.org/servers/TestData2.0/hapi`. cell 18 contains `http://hapi-server.org/servers/TestData2.0/hapi`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `hapi-tutorial/HAPI_03.ipynb` cell 24: Artifact references plain HTTP endpoint `http://hapi-server.org/servers/TestData2.0/hapi`. cell 24 contains `http://hapi-server.org/servers/TestData2.0/hapi`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `pysat-tutorial/00 - ACE SWEPAM Demonstration.ipynb` cell 2 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 2 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/00 - ACE SWEPAM Demonstration.ipynb` cell 3: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat/`. cell 3 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/00 - ACE SWEPAM Demonstration.ipynb` cell 3 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 3 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/00 - ACE SWEPAM Demonstration.ipynb` cell 3 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 3 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/00 - ACE SWEPAM Demonstration.ipynb` cell 6 output: Artifact hard-codes environment-specific path `/srv/conda/envs/notebook/lib/python3.10/site-packages/pysatSpaceWeather/instruments/ace_swepam.py`. cell 6 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/01 - ACE SIS Customization.ipynb` cell 3: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat/`. cell 3 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/01 - ACE SIS Customization.ipynb` cell 3 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 3 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/01 - ACE SIS Customization.ipynb` cell 3 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 3 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/01 - ACE SIS Customization.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/01 - ACE SIS Customization.ipynb` cell 7 output: Artifact hard-codes environment-specific path `/srv/conda/envs/notebook/lib/python3.10/site-packages/pysatSpaceWeather/instruments/ace_sis.py`. cell 7 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/02 - DMSP Polar Ion Drifts.ipynb` cell 3: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat/`. cell 3 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/02 - DMSP Polar Ion Drifts.ipynb` cell 3 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 3 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/02 - DMSP Polar Ion Drifts.ipynb` cell 3 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 3 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/02 - DMSP Polar Ion Drifts.ipynb` cell 6 output: Artifact hard-codes environment-specific path `/srv/conda/envs/notebook/lib/python3.10/site-packages/pysatMadrigal/instruments/dmsp_ivm.py`. cell 6 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/03 - ICON IVM Demonstration.ipynb` cell 4: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat/`. cell 4 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/03 - ICON IVM Demonstration.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/03 - ICON IVM Demonstration.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/03 - ICON IVM Demonstration.ipynb` cell 7 output: Artifact hard-codes environment-specific path `/srv/conda/envs/notebook/lib/python3.10/site-packages/pysatNASA/instruments/icon_ivm.py`. cell 7 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/04 - ICON MIGHTI Demonstration.ipynb` cell 4: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat/`. cell 4 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/04 - ICON MIGHTI Demonstration.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/04 - ICON MIGHTI Demonstration.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/04 - ICON MIGHTI Demonstration.ipynb` cell 7 output: Artifact hard-codes environment-specific path `/srv/conda/envs/notebook/lib/python3.10/site-packages/pysatNASA/instruments/icon_mighti.py`. cell 7 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/05 - pysat Creating netCDF4 Files.ipynb` cell 10 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat/pysat/testing/`. cell 10 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/05 - pysat Creating netCDF4 Files.ipynb` cell 11 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat/pysat/testing`. cell 11 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/05 - pysat Creating netCDF4 Files.ipynb` cell 11 output: Artifact references plain HTTP endpoint `http://doi.org/10.5281/zenodo.1199703`. cell 11 output contains `http://doi.org/10.5281/zenodo.1199703`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `pysat-tutorial/05 - pysat Creating netCDF4 Files.ipynb` cell 4: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat/`. cell 4 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/05 - pysat Creating netCDF4 Files.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/05 - pysat Creating netCDF4 Files.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/06 - pysatMissions.ipynb` cell 4: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat/`. cell 4 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/06 - pysatMissions.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/06 - pysatMissions.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/06 - pysatMissions.ipynb` cell 5 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 5 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/06 - pysatMissions.ipynb` cell 8 output: Artifact hard-codes environment-specific path `/srv/conda/envs/notebook/lib/python3.10/site-packages/pysatMissions/instruments/missions_sgp4.py`. cell 8 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/07 - pysatSeasons Bin Averaging.ipynb` cell 4: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat/`. cell 4 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/07 - pysatSeasons Bin Averaging.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/07 - pysatSeasons Bin Averaging.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/08 - pysatSeasons Occurrence Probability.ipynb` cell 10 output: Artifact hard-codes environment-specific path `/srv/conda/envs/notebook/lib/python3.10/site-packages/pysatSeasons/occur_prob.py:260:`. cell 10 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/08 - pysatSeasons Occurrence Probability.ipynb` cell 4: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat/`. cell 4 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/08 - pysatSeasons Occurrence Probability.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/08 - pysatSeasons Occurrence Probability.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/09 - pysat Loading.ipynb` cell 4: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat/`. cell 4 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/09 - pysat Loading.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/09 - pysat Loading.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/10 - pysat Iteration.ipynb` cell 4: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat/`. cell 4 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/10 - pysat Iteration.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/10 - pysat Iteration.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/11 - pysat Instantiation and Parameters.ipynb` cell 14 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 14 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/11 - pysat Instantiation and Parameters.ipynb` cell 18 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 18 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/11 - pysat Instantiation and Parameters.ipynb` cell 4: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat/`. cell 4 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/11 - pysat Instantiation and Parameters.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/11 - pysat Instantiation and Parameters.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/11 - pysat Instantiation and Parameters.ipynb` cell 8 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat/pysat/testing/`. cell 8 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/12 - pyast Data Access and Assignment.ipynb` cell 4: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat/`. cell 4 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/12 - pyast Data Access and Assignment.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pysat-tutorial/12 - pyast Data Access and Assignment.ipynb` cell 4 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/.pysat`. cell 4 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pyspedas-tutorial/Finding_Magnetic_Nulls_MMS_20230324.ipynb` cell 3: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/pyspedas_data`. cell 3 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pyspedas-tutorial/Generate_2D_slices_of_MMS_FPI_data.ipynb` cell 4: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/pyspedas_data`. cell 4 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pyspedas-tutorial/Introduction_to_PySPEDAS.ipynb` cell 11 output: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/pyspedas_data/themis/tha/l2/fgm/2023/tha_l2_fgm_20230324_v01.cdf`. cell 11 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pyspedas-tutorial/Introduction_to_PySPEDAS.ipynb` cell 11 output: Artifact hard-codes environment-specific path `/home/jovyan`. cell 11 output still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pyspedas-tutorial/Introduction_to_PySPEDAS.ipynb` cell 11 output: Artifact references plain HTTP endpoint `http://themis.ssl.berkeley.edu/data/themis/tha/l2/fgm/2023/`. cell 11 output contains `http://themis.ssl.berkeley.edu/data/themis/tha/l2/fgm/2023/`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `pyspedas-tutorial/Introduction_to_PySPEDAS.ipynb` cell 11 output: Artifact references plain HTTP endpoint `http://themis.ssl.berkeley.edu/data/themis/tha/l2/fgm/2023/tha_l2_fgm_20230324_v01.cdf`. cell 11 output contains `http://themis.ssl.berkeley.edu/data/themis/tha/l2/fgm/2023/tha_l2_fgm_20230324_v01.cdf`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `pyspedas-tutorial/Introduction_to_PySPEDAS.ipynb` cell 5: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/pyspedas_data`. cell 5 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pyspedas-tutorial/MMS, THEMIS, Arase orbits 2023-03-24.ipynb` cell 5: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/pyspedas_data`. cell 5 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pyspedas-tutorial/MMS_summary_plot_20230324.ipynb` cell 2: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/pyspedas_data`. cell 2 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pyspedas-tutorial/MMS_summary_plot_20230324.ipynb` cell 3 output: Artifact references plain HTTP endpoint `http://themis.ssl.berkeley.edu/data/themis/thg/l1/mag/idx/2023/`. cell 3 output contains `http://themis.ssl.berkeley.edu/data/themis/thg/l1/mag/idx/2023/`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `pyspedas-tutorial/Magnetic_Field_Modeling.ipynb` cell 15 output: Artifact references plain HTTP endpoint `http://wdc.kugi.kyoto-u.ac.jp/`. cell 15 output contains `http://wdc.kugi.kyoto-u.ac.jp/`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `pyspedas-tutorial/Magnetic_Field_Modeling.ipynb` cell 2: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/pyspedas_data`. cell 2 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pyspedas-tutorial/PyTplot_range_options.ipynb` cell 2: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/pyspedas_data`. cell 2 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `pyspedas-tutorial/PyTplot_variable_options.ipynb` cell 19 output: Artifact references plain HTTP endpoint `http://themis.ssl.berkeley.edu/data/themis/tha/l2/fgm/2023/`. cell 19 output contains `http://themis.ssl.berkeley.edu/data/themis/tha/l2/fgm/2023/`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `pyspedas-tutorial/PyTplot_variable_options.ipynb` cell 2: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/pyspedas_data`. cell 2 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `spacepy-tutorial/SpacePy - Cusp energetic particles.md` markdown body: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/spacepy_tutorial`. markdown body still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `spacepy-tutorial/SpacePy - Cutoff Rigidities.md` markdown body: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/spacepy_tutorial`. markdown body still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `spacepy-tutorial/SpacePy - MMS Ephemeris.md` markdown body: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/spacepy_tutorial`. markdown body still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `spacepy-tutorial/SpacePy - SWMF Dynamics.md` markdown body: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/spacepy_tutorial/`. markdown body still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `spacepy-tutorial/SpacePy - SWMF Dynamics.md` markdown body: Artifact references plain HTTP endpoint `http://herot.engin.umich.edu/~gtoth/SWMF/doc/SWMF.pdf`. markdown body contains `http://herot.engin.umich.edu/~gtoth/SWMF/doc/SWMF.pdf`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `sunpy-tutorial/sunpy-pyspedas-showcase/sunpy-pyspedas-demo.ipynb` cell 3: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/sunpy-tutorial/sunpy-pyspedas/`. cell 3 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `sunpy-tutorial/sunpy-tutorial/part-1-sunpy-instructor-version.ipynb` cell 2: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/sunpy-tutorial/sunpy/`. cell 2 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `sunpy-tutorial/sunpy-tutorial/part-1-sunpy-instructor-version.ipynb` cell 7: Artifact references plain HTTP endpoint `http://docs.astropy.org/en/stable/units/index.html`. cell 7 contains `http://docs.astropy.org/en/stable/units/index.html`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
- `sunpy-tutorial/sunpy-tutorial/part-1-sunpy.ipynb` cell 2: Artifact hard-codes environment-specific path `/home/jovyan/scratch_space/sunpy-tutorial/sunpy/`. cell 2 still points at a Binder/JupyterHub path, which is likely to drift outside the original 2024 teaching environment.
- `sunpy-tutorial/sunpy-tutorial/part-1-sunpy.ipynb` cell 7: Artifact references plain HTTP endpoint `http://docs.astropy.org/en/stable/units/index.html`. cell 7 contains `http://docs.astropy.org/en/stable/units/index.html`; verify the provider still supports this endpoint in 2026 and prefer HTTPS where available.
### Informational

- `pysat-tutorial/00 - ACE SWEPAM Demonstration.ipynb` cell 6 output: Artifact output still references an old site-packages path. cell 6 output includes `site-packages/pysatSpaceWeather/instruments/ace_swepam.py`, which ties the notebook output to the historical 2024 environment.
- `pysat-tutorial/01 - ACE SIS Customization.ipynb` cell 7 output: Artifact output still references an old site-packages path. cell 7 output includes `site-packages/pysatSpaceWeather/instruments/ace_sis.py`, which ties the notebook output to the historical 2024 environment.
- `pysat-tutorial/02 - DMSP Polar Ion Drifts.ipynb` cell 6 output: Artifact output still references an old site-packages path. cell 6 output includes `site-packages/pysatMadrigal/instruments/dmsp_ivm.py`, which ties the notebook output to the historical 2024 environment.
- `pysat-tutorial/03 - ICON IVM Demonstration.ipynb` cell 7 output: Artifact output still references an old site-packages path. cell 7 output includes `site-packages/pysatNASA/instruments/icon_ivm.py`, which ties the notebook output to the historical 2024 environment.
- `pysat-tutorial/04 - ICON MIGHTI Demonstration.ipynb` cell 7 output: Artifact output still references an old site-packages path. cell 7 output includes `site-packages/pysatNASA/instruments/icon_mighti.py`, which ties the notebook output to the historical 2024 environment.
- `pysat-tutorial/05 - pysat Creating netCDF4 Files.ipynb` cell 3 output `pysat`: Artifact output still records package version `pysat 3.2.0`. cell 3 output contains a captured environment version line from the 2024 run; this is documentation drift even when code still executes.
- `pysat-tutorial/05 - pysat Creating netCDF4 Files.ipynb` cell 3 output `pysatMadrigal`: Artifact output still records package version `pysatMadrigal 0.2.0`. cell 3 output contains a captured environment version line from the 2024 run; this is documentation drift even when code still executes.
- `pysat-tutorial/05 - pysat Creating netCDF4 Files.ipynb` cell 3 output `pysatMissions`: Artifact output still records package version `pysatMissions 0.3.4`. cell 3 output contains a captured environment version line from the 2024 run; this is documentation drift even when code still executes.
- `pysat-tutorial/05 - pysat Creating netCDF4 Files.ipynb` cell 3 output `pysatNASA`: Artifact output still records package version `pysatNASA 0.0.5`. cell 3 output contains a captured environment version line from the 2024 run; this is documentation drift even when code still executes.
- `pysat-tutorial/05 - pysat Creating netCDF4 Files.ipynb` cell 3 output `pysatSeasons`: Artifact output still records package version `pysatSeasons 0.2.0`. cell 3 output contains a captured environment version line from the 2024 run; this is documentation drift even when code still executes.
- `pysat-tutorial/05 - pysat Creating netCDF4 Files.ipynb` cell 3 output `pysatSpaceWeather`: Artifact output still records package version `pysatSpaceWeather 0.1.0`. cell 3 output contains a captured environment version line from the 2024 run; this is documentation drift even when code still executes.
- `pysat-tutorial/06 - pysatMissions.ipynb` cell 8 output: Artifact output still references an old site-packages path. cell 8 output includes `site-packages/pysatMissions/instruments/missions_sgp4.py`, which ties the notebook output to the historical 2024 environment.
- `pysat-tutorial/08 - pysatSeasons Occurrence Probability.ipynb` cell 10 output: Artifact output still references an old site-packages path. cell 10 output includes `site-packages/pysatSeasons/occur_prob.py:260:`, which ties the notebook output to the historical 2024 environment.
- `pyspedas-tutorial/Finding_Magnetic_Nulls_MMS_20230324.ipynb` cell 4 output: Artifact output still references an old site-packages path. cell 4 output includes `site-packages/urllib3/__init__.py:35:`, which ties the notebook output to the historical 2024 environment.
- `pyspedas-tutorial/Introduction_to_PySPEDAS.ipynb` cell 11 output: Artifact output still references an old site-packages path. cell 11 output includes `site-packages/pyspedas/themis/spacecraft/fields/fgm.py:89[0m,`, which ties the notebook output to the historical 2024 environment.
- `pyspedas-tutorial/Introduction_to_PySPEDAS.ipynb` cell 11 output: Artifact output still references an old site-packages path. cell 11 output includes `site-packages/pyspedas/themis/load.py:197[0m,`, which ties the notebook output to the historical 2024 environment.
- `pyspedas-tutorial/Introduction_to_PySPEDAS.ipynb` cell 11 output: Artifact output still references an old site-packages path. cell 11 output includes `site-packages/pyspedas/utilities/download.py:489[0m,`, which ties the notebook output to the historical 2024 environment.
- `pyspedas-tutorial/Introduction_to_PySPEDAS.ipynb` cell 11 output: Artifact output still references an old site-packages path. cell 11 output includes `site-packages/pyspedas/utilities/download.py:505[0m,`, which ties the notebook output to the historical 2024 environment.
- `pyspedas-tutorial/Introduction_to_PySPEDAS.ipynb` cell 11 output: Artifact output still references an old site-packages path. cell 11 output includes `site-packages/pyspedas/utilities/download.py:231[0m,`, which ties the notebook output to the historical 2024 environment.
- `pyspedas-tutorial/Introduction_to_PySPEDAS.ipynb` cell 7 output: Artifact output still references an old site-packages path. cell 7 output includes `site-packages/urllib3/__init__.py:35:`, which ties the notebook output to the historical 2024 environment.
- `pyspedas-tutorial/MMS_summary_plot_20230324.ipynb` cell 3 output: Artifact output still references an old site-packages path. cell 3 output includes `site-packages/urllib3/__init__.py:35:`, which ties the notebook output to the historical 2024 environment.
- `pyspedas-tutorial/MMS_summary_plot_20230324.ipynb` cell 3 output: Artifact output still references an old site-packages path. cell 3 output includes `site-packages/pytplot/MPLPlotter/specplot.py:285:`, which ties the notebook output to the historical 2024 environment.
- `pyspedas-tutorial/MMS_summary_plot_20230324.ipynb` cell 3 output: Artifact output still references an old site-packages path. cell 3 output includes `site-packages/pytplot/MPLPlotter/specplot.py:285:`, which ties the notebook output to the historical 2024 environment.
### External Blocker

- `(environment)` PlasmaPy `PlasmaPy`: Editable install failed for `PlasmaPy`. ERROR: Package 'plasmapy' requires a different Python: 3.11.11 not in '>=3.12'

ERROR conda.cli.main_run:execute(125): `conda run python -m pip install --user --no-deps -e /var/folders/4f/t664wvxn4nd8864qfqwknh7r008q5h/T/summer-school-audit-n541fked/repos/PlasmaPy` failed. (See above for error)
- `(environment)` pysatMissions `pysatMissions`: Audit environment cannot import `pysatMissions` after setup. ModuleNotFoundError("No module named 'ephem'")
- `(environment)` stixpy `stixpy`: Audit environment cannot import `stixpy` after setup. ModuleNotFoundError("No module named 'stixpy'")
- `(environment)` stixpy `stixpy`: Editable install failed for `stixpy`. ERROR: Package 'stixpy' requires a different Python: 3.11.11 not in '>=3.12'

ERROR conda.cli.main_run:execute(125): `conda run python -m pip install --user --no-deps -e /var/folders/4f/t664wvxn4nd8864qfqwknh7r008q5h/T/summer-school-audit-n541fked/repos/stixpy` failed. (See above for error)
- `(environment)` sunpy `sunpy`: Editable install failed for `sunpy`. ERROR: Package 'sunpy' requires a different Python: 3.11.11 not in '>=3.12'

ERROR conda.cli.main_run:execute(125): `conda run python -m pip install --user --no-deps -e /var/folders/4f/t664wvxn4nd8864qfqwknh7r008q5h/T/summer-school-audit-n541fked/repos/sunpy` failed. (See above for error)
- `pyspedas-tutorial/Introduction_to_PySPEDAS.ipynb` cell 11: Notebook execution failed. 
- `pyspedas-tutorial/MMS, THEMIS, Arase orbits 2023-03-24.ipynb` cell 6: Notebook execution failed. 
- `pyspedas-tutorial/Magnetic_Field_Modeling.ipynb` cell 5: Notebook execution failed. 
- `pyspedas-tutorial/PyTplot_variable_options.ipynb` cell 4: Notebook execution failed. 
