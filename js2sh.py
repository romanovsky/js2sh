#!/usr/bin/env python

"""
Created on Feb 27, 2017
@author = Sergey Romanovsky
"""
import sys
from os import fstat
from stat import S_ISFIFO, S_ISREG
from json import load
from pipes import quote


sys.tracebacklimit = 0
mode = fstat(0).st_mode
if not S_ISFIFO(mode) and not S_ISREG(mode):
    print """
        This script will help you to convert a json dictionary fed to stdin to a set of bash exports.
        The following command will make json dictionary key/value pairs as environment variables
        in the current shell process:
            eval `echo '{"foo": "bar"}' | js2sh.py`
            eval `js2sh.py < myconfig.json`
        """
    exit(0)
for (name, value) in load(sys.stdin).items():
    print "export {}={}".format(quote(name), quote(value))