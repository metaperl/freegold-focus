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
    _static_dirs = 'css form img images js media slides'.split()
    for static_dir in _static_dirs:
        yield config_static_directory(static_dir)
        for subdir in 'ben919 buygold get13kilos superior tools trainwith'.split():
            yield config_static_directory("{0}/{1}".format(subdir, static_dir))


config = {

    'global': {
        'environment': 'embedded',
        'log.screen': True,
        'tools.staticdir.debug': True
    },
    '/': {
        'tools.staticdir.root' : full_path(),
    }

}

for static_dir in static_dirs():
    config.update(static_dir)

