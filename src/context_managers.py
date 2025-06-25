# /////////////////////////////////////////////////////////////////////////////
# © 2023 SUNIL J. PATEL
# VERSION: 1.0.0
#
# This module contains context managers used in the application.
# /////////////////////////////////////////////////////////////////////////////


# IMPORT PACKAGES, MODULES, CLASSES AND CLASS INSTANCES
# /////////////////////////////////////////////////////////////////////////////
import os
from contextlib import contextmanager


# CONTEXT MANAGERS
# /////////////////////////////////////////////////////////////////////////////
@contextmanager
def directory(path):
    """Temporarily change current working directory to path directory."""
    try:
        cwd = os.getcwd()
        os.chdir(path)
        yield
    finally:
        os.chdir(cwd)