#!/bin/bash

# Determine if python3 is installed
python3 -V &> /dev/null
if [ $? -ne 0 ]
then
    echo "Python3 was not found! Please install this before proceeding."
    exit 1
fi

# Determine if pip3 is installed
pip3 -V &> /dev/null
if [ $? -ne 0 ]
then
    echo "Pip3 was not found! Please install this before proceeding."
    exit 1
fi

# Grab the major and minor version numbers
pythonVersion=`python3 -V | cut -d' ' -f2 | cut -d'.' -f1-2`
pipVersion=`pip3 -V | tr -d '()' | awk -F' ' '{print $NF}'`

# Check that python3 and pip3 versions are in agreement
if [ "$pythonVersion" != "$pipVersion" ]
then
    echo -e "Python3 is version $pythonVersion, but pip3 is version $pipVersion.\nPlease install the correct version of pip3 to support the python3 listed here."
    exit 1
fi

# Export the correct locations of our working python3/pip3 pair
export PYTHON3BIN=`which python$pythonVersion`
export PIP3BIN=`which pip$pipVersion`

echo "Python 3 bin is python$pythonVersion ($PYTHON3BIN)"
echo "Pip 3 bin is pip$pipVersion ($PIP3BIN)"
