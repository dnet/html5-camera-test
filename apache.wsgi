#!/usr/bin/env python

import os, sys

workspace = os.path.dirname(__file__)
sys.path.append(workspace)

from camtest import app as application
