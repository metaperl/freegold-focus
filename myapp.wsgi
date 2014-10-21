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



application = cherrypy.Application(myapp.Root(), "/", config.config)
