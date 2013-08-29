from django.core.management import setup_environ

import sys
sys.path.append('/home/schemelab/domains/biz/freegold/focus/focus')
import focus.settings

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'focus.settings'
setup_environ(focus.settings)

sys.path.append('/home/schemelab/domains/biz/freegold/focus/focus')
from focusapp.models import Person

p = Person.objects.filter(kbid='supreme')
print p
