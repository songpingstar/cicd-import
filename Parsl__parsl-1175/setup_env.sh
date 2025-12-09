#!/bin/bash

pip install --upgrade pip setuptools
pip install numpy Cython
pip install -r test-requirements.txt    

cd /testbed/parsl
