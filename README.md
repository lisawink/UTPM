# Urban Transport Policy Model (UTPM)
This is the repository for the UTPM model behind the Nature Communications article:

## Overview
The model can be accessed by cloning the github repository and following the instructions below or by using the demo jupyter notebook.

## Table of contents

## Prerequisites
To work with everything in this repository, you'll need the following installed:

- [Python](https://www.python.org/)

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
pip install --user pipenv
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

### Install from Github
```
git clone https://github.com/neurodata/mgcpy
cd mgcpy
python3 setup.py install
```
- `sudo`, if required
- `python3 setup.py build_ext --inplace  # for cython`, if you want to test in-place, first execute this

# Setting up the development environment:
- To build image and run from scratch:
  - Install [docker](https://docs.docker.com/install/)
  - Build the docker image, `docker build -t mgcpy:latest .`
    - This takes 10-15 mins to build
  - Launch the container to go into mgcpy's dev env, `docker run -it --rm --name mgcpy-env mgcpy:latest`
- Pull image from Dockerhub and run:
  - `docker pull tpsatish95/mgcpy:latest` or `docker pull tpsatish95/mgcpy:development`
  - `docker run -it --rm -p 8888:8888 --name mgcpy-env tpsatish95/mgcpy:latest` or `docker run -it --rm -p 8888:8888 --name mgcpy-env tpsatish95/mgcpy:development`


- To run demo notebooks (from within Docker):
  - `cd demos`
  - `jupyter notebook --ip 0.0.0.0 --no-browser --allow-root`
  - Then copy the url it generates, it looks something like this: `http://(0de284ecf0cd or 127.0.0.1):8888/?token=e5a2541812d85e20026b1d04983dc8380055f2d16c28a6ad`
  - Edit this: `(0de284ecf0cd or 127.0.0.1)` to: `127.0.0.1`, in the above link and open it in your browser
  - Then open `mgc.ipynb`

- To mount/load local files into docker container:
  - Do `docker run -it --rm -v <local_dir_path>:/root/workspace/ -p 8888:8888 --name mgcpy-env tpsatish95/mgcpy:latest`, replace `<local_dir_path>` with your local dir path.
  - Do `cd ../workspace` when you are inside the container to view the mounted files. The **mgcpy** package code will be in `/root/code` directory.

# License

This project is covered under the **Apache 2.0 License**.

# automation-scripts

0. Install Python 3.8
```
Only install version 3.8 please from https://www.python.org/downloads/ 
```

1. Install pip (package manager)

```
python -m ensurepip --upgrade
```

2. Install pipenv

```
pip install --user pipenv
```

3. Set up pipenv

```
pipenv install
```

# if pipenv command not found

2. Install pipenv for python 3

```
pip3 install pipenv
```

3. Change path

```
PYTHON_BIN_PATH="$(python3 -m site --user-base)/bin"
PATH="$PATH:$PYTHON_BIN_PATH"
```
4. Set up pipenv

```
pipenv install
```

# to install a new package

```
pipenv install PACKAGE_NAME
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

# If you have the issue "Import pandas could not be resolved from source Pylance(reportMissingModuleSource)"

1. Check out: https://stackoverflow.com/questions/71617057/import-pandas-could-not-be-resolved-from-source-pylancereportmissingmodulesourc

Have fun!
