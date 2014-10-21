
# -*- python -*-

# core
import os
import sys

# 3rd party
import cherrypy

# local
def full_path(*extra):
    a = os.path.abspath(__file__)
    #pathname  = os.path.dirname(sys.argv[0])
    #return os.path.abspath(pathname)
    # raise ValueError, "abspath = {}. d = {}".format(
    #     a, os.path.dirname(a)
    #     )
    return os.path.dirname(a)

sys.path.insert(0, full_path())


import config
import myapp

cherrypy.quickstart(myapp.Root(), script_name="", config=config.config)
