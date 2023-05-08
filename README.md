# Mirnov viewer

## Installation

Instructions for linux

### Requirements

#### QT

This program uses the QT library.
With ubuntu based distributions, you can install it via:

```
sudo apt install qt6-base-dev
```

Older distributions do not provide this package.
In this case, there's a qt5 branch that should work without installing anything.

```
git checkout qt5
```

#### Python:

Install the requirements via:

```
pip install -r requirements.txt
```

#### TJII library

The python package to access the TJII library needs to be compiled with gfortran.
The easiest way is using the provided makefile:

```
make build
```

## Running

From the main folder, running

```
make
```

should be enough.
