import os
def full_path(p=""): return os.path.join(os.path.dirname(__file__), p)

def config_static_directory(d):
    return {
        "/{0}".format(d) : {
            'tools.staticdir.on'  : True,
            'tools.staticdir.dir' : d
        }
    }

def static_dirs():
    _static_dirs = 'css img images js media'.split()
    for static_dir in _static_dirs:
        yield config_static_directory(static_dir)
        yield config_static_directory("superior/{0}".format(static_dir))


config = {

    'global': {
        'environment': 'embedded',
        'log.screen': True
    },
    '/': {
        'tools.staticdir.root' : full_path(),
    }

}

for static_dir in static_dirs():
    config.update(static_dir)

