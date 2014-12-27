# Add non-system directories to sys.path

# Uses a list of top level directories of any and all of your repos.
# Loop below will recurse through the path, ignoring .git 
# sub-directories and not diving into packages.

# edit as needed... 
# PYTHON_MODULES_DIR_LIST = [os.path.join(os.path.expandvars('$HOME'),'DIRECTORY_NAME')]
PYTHON_MODULES_DIR_LIST = []

import os
import sys

for python_module_dir in PYTHON_MODULES_DIR_LIST:
    print 'Recurseively adding %s to the python path...' % python_module_dir
    sys.path.append(python_module_dir)
    for root, dirs, files in os.walk(python_module_dir):
        for d in dirs:
            if '.git' in root or '.git' in d: # ignore the .git directory
                pass
            # add non-package directories to the path
            elif not os.path.exists(os.path.join(root, d, '__init__.py')):
                fulldir = os.path.join(root,d)
                print '---> Adding %s to the python path...' % fulldir
                sys.path.append(fulldir)

# Data analysis imports
import numpy as np
import pandas as pd

# IO imports
import json

# Misc imports, but stuff always trips me up
from datetime import datetime, timedelta
from numpy import arange

#IPython references
from IPython.core.magic import register_line_magic
_ip = get_ipython()
