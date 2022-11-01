# Urban Transport Policy Model (UTPM)
This is the repository for the UTPM model behind the Nature Communications article:

## Overview
The model can be accessed by cloning the github repository and following the instructions below.

## Table of contents
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [Running the UTPM](#running-the-utpm)
- [License](#license)

## Prerequisites
To work with everything in this repository, you'll need [Python](https://www.python.org/) 3.0 or higher installed

# System Requirements
## Hardware requirements
The UTPM requires only a standard computer with enough RAM to support the in-memory operations. For minimal performance, this will be a computer with about 2 GB of RAM. For optimal performance, we recommend a computer with the following specs:

RAM: 16+ GB
CPU: 4+ cores, 3.3+ GHz/core

## Software requirements
### OS Requirements
The UTPM should be compatible with Windows, Mac, and Linux operating systems.
The UTPM has been tested on *Windows 11* and *macOS Mojave (10.14.1)*.

### Prerequisites
To work with everything in this repository, you'll need [Python](https://www.python.org/) 3.0 or higher installed

### Python Dependencies
The UTPM depends mainly on the Python scientific stack and the following packages:

```
numpy
pandas
matplotlib
scipy
seaborn
ipython
openpyxl
```

# Installation Guide

Takes 5-10 minutes

### Install from Github
```
git clone https://github.com/LisaOJWinkler/UrbanTransportPolicyModel
cd UrbanTransportPolicyModel
```
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
### Run a script

1. Open the pipenv shell so you have access to the right packages

```
pipenv shell
```

2. Run the script

```
python PATH_TO_SCRIPT
```

# Running the UTPM (Demo)

The main method is located in UTPM_Run_Model.py Calling the function 
```
__main__(phase_out_date,phase_out_hybrid,scrap_age_pre2020,scrap_age_post2020,mass,\
  fleet_size_projection,miles_driven_projection,retrofit_percentage,manufacture,elec,rate)
```
returns a dictionary of emissions and energy demand results. One run of the model takes ~ 30 seconds.

### Calling the baseline case
```
__main__(phase_out_date=2030,phase_out_hybrid=2035,scrap_age_pre2020=20,scrap_age_post2020=15,mass=1400,\
  fleet_size_projection=20,miles_driven_projection=20,retrofit_percentage=0,manufacture=0,elec=2050,rate=28)
```

### Running the UTPM for a different city

The UTPM can be applied to a different city by changing the input data for the initialisation of the car fleet. Data for London is currently included in RegionalData.py. Data for a different city should replace the data in the RegionalData.py file following the same format. This includes
```
#2019 number of cars in city (thousands)
cars_2019

#adoption rate of fuel type in GB yearly from 2001 to 2020 (%)
#number of newly registered vehicles of fuel type / total new registrations in that year
adop_car_p (petrol)
adop_car_d (diesel)
adop_car_h (hybrid)
adop_car_ph (plug-in hybrid)
adop_car_b (battery-electric)

#ages of cars in 2019
#% of fleet age 0 to 30+ (i.e. manufactured in 2019 to <1989) for the year 2019
car_per_age

#average fuel consumption in litres per 100km for new cars registered from 1997 to 2019
fuel_car_p (petrol)
fuel_car_d (diesel)

#km driven per year by cars & taxis in 2019 (billion km)
km_2019
```

### Running different policies

Different policy combinations can be run in the model by adjusting the parameters when calling the main method. The description of the policies and parameters they can take are as follows:
- Phase out date - the ban on the sale of new ICEVs (petrol and diesel vehicles). Can take any integer value between 2022-2050
```
phase_out_date
```
- Hybrid phase out date - the ban on the sale of plug-in hybrid vehicles (PHEVs). Can take values 2025, 2030, 2035 and 2040
```
phase_out_hybrid
```
- Scrap age (pre-2020 and post-2020) - the age at which cars are removed from the model. Can take any integer value between 0 and 30
```
scrap_age_pre2020
scrap_age_post2020
```
- Lightweighting - mass of the average car in fleet. Can take values 500-2500 kg
```
mass
```
- Car travel activity - defined by: 
   - future fleet size - number of future cars in fleet, given as a percentage increase from 2019 values in 2040, e.g. +20% or -60%. Can take any positive or negative integer value between -100% and +100%
   - miles driven - magnitude of future distance driven, given as a percentage from 2019 values, e.g. +20% or -60%. Can take any positive or negative integer       value between -100% and +100%
   - rate - rate of change in future distance driven, given as a number of years from the year 2022. Can take any integer greater than 1.
```
  fleet_size_projection
  miles_driven_projection
  rate
 ```
 - Retrofitting - percentage of scrapped fossil fuel cars which are retrofitted with electric engines. Can take any percentage between 0% and 100%.
 ```
  retrofit_percentage
 ```
 - Regulated manufacturing standards - lower embedded emissions for manufacturing electric vehicles. Can take boolean values (0  being non-regulated manufacturing and 1 being regulated manufacturing).
 ```
 manufacture
 ```
 - Decarbonisation of electrical grid - increased speed of forecasted decarbonisation of electrical grid. Takes year of net-zero as parameter which can take any integer value between 2020 and 2070.
 ```
 elec
 ```
 More information on these parameters and the method can be found in the Nature Communications paper and corresponding supplementary information.

### Saving results for multiple runs of the model

The method for saving results to a file is located in save_results.py. Calling this method loops through policy combinations (which can be adjusted) and calls the main method multiple times. Results are saved in a .csv or .xlsx file

### Reproducing figures 

The code for reproducing figures 1, 3 and 4 and supplementary figure 1 is included in the folder titled 'Figures'

# License

This project is covered under the **Apache 2.0 License**.
