
# -*- python -*-

# core
import os
import sys

# 3rd party
import cherrypy

# local
def full_path(*extra):
    return os.path.join(os.path.dirname(__file__), *extra)
sys.path.insert(0, full_path())
import config
import myapp

cherrypy.quickstart(myapp.Root(), script_name="/", config=config.config)
