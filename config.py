import os
import pprint

pp = pprint.PrettyPrinter(indent=4)

def full_path(p=''):
    return os.path.join(os.path.dirname(__file__), p)

def config_static_directory(d):
    return {
        "/{0}".format(d) : {
            'tools.staticdir.on'  : True,
            'tools.staticdir.dir' : d
        }
    }

def static_dirs():
    static_dirs = 'css form img data1/images engine1 images includes js media slides styles'.split()
    for static_dir in static_dirs:
        subdirs = 'ben919 buygold get3kilos get13kilos intro lookout numbers superior tools toolsform trainwith zimbabwe'.split()
        for subdir in subdirs:
            yield config_static_directory("{0}/{1}".format(subdir, static_dir))

        yield config_static_directory("{0}".format(static_dir))


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

print "FULLPATH", full_path()

pp.pprint(config)
