
# -*- python -*-

# core
import importlib
import os
import sys
import StringIO

# 3rd party
import cherrypy
import meld3

# local
def full_path(*extra):
    return os.path.join(os.path.dirname(__file__), *extra)
sys.path.insert(0, full_path())
from saorm import *


class Root(object):

    def person(self, kbid):
        #example on how to query your Schema
        from sqlalchemy.orm import sessionmaker
        session = sessionmaker(bind=engine)()
        p = session.query(Affiliate).filter_by(id=kbid).first()
        return p

    html_file = full_path('index.html')

    @cherrypy.expose
    def index(self, s="supreme", cmpg=None, opener='corp'):

        p = self.person(kbid=s)

        src = {
            'corp': 'http://www.youtube.com/embed/0lrqEGlu0Fo',
            'uk': 'http://www.youtube.com/embed/30MfCTLhdZ4',
        }

        followers = {
            'corp': 'uk',
            'uk': 'corp',
        }

        carousel = dict(
            opener=src[opener],
            follower = src[followers[opener]]
        )

        affiliate_url = 'http://karatbars.com/signup.php?s={0}'.format(s)
        landing_url = 'http://karatbars.com/landing/?s={0}'.format(s)
        skype_url = 'skype:{0}?add'.format(p.skype)
        affiliate_url = 'http://karatbars.com/signup.php?s={0}'.format(s)
        kbgold_uk_url = 'http://www.karatbarsgold.co.uk/{0}'.format(p.kbuk_id)
        #slide = '{0}?autoplay=1'.format(default_slide)
        email_href = 'mailto:{0}'.format(p.email)

        with open(self.html_file, 'r') as fp:
            html = fp.read()
        root = meld3.parse_htmlstring(html)
        for lookup, src in carousel.iteritems():
            root.findmeld(lookup).attributes(src='{0}?autoplay=1'.format(src))
        root.findmeld('affiliate_url').attributes(href=affiliate_url)
        root.findmeld('kbgold_uk_url').attributes(href=kbgold_uk_url)
        root.findmeld('enroll_free').attributes(href=affiliate_url)
        root.findmeld('contact_iframe').attributes(src=landing_url)
        root.findmeld('name').content(p.name)
        root.findmeld('name_in_title').content(
            "Karatbars International - {0}".format(p.name)
        )

        root.findmeld('pic').attributes(src=p.pic)
        root.findmeld('phone').content(p.number)
        root.findmeld('skype_url').attributes(href=skype_url)
        root.findmeld('skype_id').content(p.skype)
        # iterator = root.findmeld('numbers').repeat(u['numbers'])
        # for elem, item in iterator:
        #     elem.findmeld('number').content(item)
        #     #root.write_xhtml(output)
        root.findmeld('email_href').attributes(href=email_href)
        root.findmeld('email').content(p.email)

        return root.write_htmlstring()

