# Urban Transport Policy Model (UTPM)
This is the repository for the UTPM model behind the Nature Communications article:

## Overview
The model can be accessed by cloning the github repository and following the instructions below.

## Table of contents

## Prerequisites
To work with everything in this repository, you'll need [Python](https://www.python.org/) installed

# System Requirements
## Hardware requirements
The UTPM requires only a standard computer with enough RAM to support the in-memory operations.

## Software requirements
### OS Requirements
The UTPM has been tested on *Windows* and *macOS*.

### Python Dependencies
The UTPM mainly depends on the Python scientific stack.

```
numpy
pandas
matplotlib
scipy
seaborn
ipython
openpyxl
```

# Installation Guide:

### Install from Github
git clone https://github.com/LisaOJWinkler/UrbanTransportPolicyModel
cd UrbanTransportPolicyModel
### Install dependencies using pip
1. Install pip (package manager)

```
python -m ensurepip --upgrade
```

2. Install pipenv

```
pip3 install --user pipenv
```

3. Install dependencies from the Pipfile

```
pipenv install
```
# to run a script

1. Open the pipenv shell so you have access to the right packages

```
pipenv shell
```

2. Run the script

```
python PATH_TO_SCRIPT
```

# Running the UTPM

- The main method is located in UTPM_Run_Model.py
- Calling the function __main__(phase_out_date,phase_out_hybrid,scrap_age_pre2020,scrap_age_post2020,mass,\
  fleet_size_projection,miles_driven_projection,retrofit_percentage,manufacture,elec,rate)
  returns a dictionary of emissions and energy demand results

# Calling the baseline case

- __main__(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
  fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
  
# Saving results for multiple runs of the model

- The save results method is located in save_results.py
- Calling this method loops through policy combinations and calls the main method multiple times
- Results are saved in a .csv or .xlsx file
