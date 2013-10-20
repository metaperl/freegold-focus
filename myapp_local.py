
# -*- python -*-

# core
import os
import sys

# 3rd party
import cherrypy

# local
def full_path(*extra):
    pathname  = os.path.dirname(sys.argv[0])
    full_path = os.path.abspath(pathname)
    return '{0}/{1}'.format(full_path, __file__)
sys.path.insert(0, full_path())
import config
import myapp

cherrypy.quickstart(myapp.Root(), script_name="", config=config.config)
