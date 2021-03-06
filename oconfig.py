import os
def full_path(p=""): return os.path.join(os.path.dirname(__file__), p)

config = {
    'global': {
        'environment': 'embedded',
        'log.error_file': full_path('cherrypy-errors.log'),
        'log.access_file': full_path('cherrypy-access.log')
    },
    '/': {
        'tools.staticdir.root' : full_path(),
    },
    '/css': {
        'tools.staticdir.on' : True,
        'tools.staticdir.dir' : 'css',
    },
    'css': {
        'tools.staticdir.on' : True,
        'tools.staticdir.dir' : 'css',
    },
    '/img': {
        'tools.staticdir.on' : True,
        'tools.staticdir.dir' : 'img',
    },
    '/images': {
        'tools.staticdir.on' : True,
        'tools.staticdir.dir' : 'images',
    },
    'images': {
        'tools.staticdir.on' : True,
        'tools.staticdir.dir' : 'images',
    },
    '/js': {
        'tools.staticdir.on' : True,
        'tools.staticdir.dir' : 'js',
    },
    'js': {
        'tools.staticdir.on' : True,
        'tools.staticdir.dir' : 'js',
    },

}
