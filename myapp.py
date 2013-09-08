
# imports
## core
import importlib
import os
import sys
import StringIO

## 3rd party
import cherrypy
import meld3

## local
def full_path(*extra):
    return os.path.join(os.path.dirname(__file__), *extra)
sys.path.insert(0, full_path())
from saorm import *


class AffiliateModel(object):

    def __init__(self, kb_id):
        self.kb_id=kb_id
        self.affiliate = self.person()

    def person(self):
        #example on how to query your Schema
        from sqlalchemy.orm import sessionmaker
        session = sessionmaker(bind=engine)()
        p = session.query(Affiliate).filter_by(id=self.kb_id).first()
        return p

class AffiliatePage(object):

    def __init__(self, kb_id, html_file='index.html'):
        self.html_file = full_path(html_file)
        self.p = AffiliateModel(kb_id).affiliate
        self.affiliate_url = 'http://karatbars.com/signup.php?s={0}'.format(kb_id)
        self.landing_url = 'http://karatbars.com/landing/?s={0}'.format(kb_id)
        self.skype_url = 'skype:{0}?add'.format(self.p.skype)
        self.kbgold_uk_url = 'http://www.karatbarsgold.co.uk/{0}'.format(self.p.kbuk_id)
        self.email_href = 'mailto:{0}'.format(self.p.email)

    def render(self):
        self.root.findmeld('affiliate_url').attributes(href=self.affiliate_url)
        self.root.findmeld('kbgold_uk_url').attributes(href=self.kbgold_uk_url)
        self.root.findmeld('enroll_free').attributes(href=self.affiliate_url)
        self.root.findmeld('contact_iframe').attributes(src=self.landing_url)
        self.root.findmeld('name').content(self.p.name)
        self.root.findmeld('name_in_title').content(
            "Karatbars International - {0}".format(self.p.name)
        )

        self.root.findmeld('pic').attributes(src=self.p.pic)
        self.root.findmeld('phone').content(self.p.number)
        self.root.findmeld('skype_url').attributes(href=self.skype_url)
        self.root.findmeld('skype_id').content(self.p.skype)
        self.root.findmeld('email_href').attributes(href=self.email_href)
        self.root.findmeld('email').content(self.p.email)


class Reese(AffiliatePage):

    def __init__(self, kb_id, opener):
        self.opener = opener
        super(Reese, self).__init__(kb_id)

    def render(self):

        super(Reese, self).render()

        src = {
            'corp': 'http://www.youtube.com/embed/0lrqEGlu0Fo',
            'uk': 'http://www.youtube.com/embed/30MfCTLhdZ4',
            'selina' : 'http://www.youtube.com/embed/37l6Wdzw490'
        }

        def lead_and_followers(lead):
            followers = src.keys()
            followers.remove(lead)
            return (lead, followers)

        followers = dict(lead_and_followers(l) for l in src.keys())

        def autoplay(u): return '{0}?autoplay=1'.format(u)

        carousel = dict(
            opener=autoplay(src[self.opener]),
            follower = src[followers[self.opener][0]],
            follower2 = src[followers[self.opener][1]]
        )

        for meld_id, url in carousel.iteritems():
            self.root.findmeld(meld_id).attributes(src=url)


class Root(object):

    @cherrypy.expose
    def index(self, s="supreme", page='Reese', opener='selina', cmpg=None, banner=None):

        module = __import__(__name__)
        class_ = getattr(module, page)
        if page == 'Reese':
            affiliate_page = class_(s, opener)
        else:
            affiliate_page = class_(s)

        with open(affiliate_page.html_file, 'r') as fp:
            html = fp.read()

        affiliate_page.root = meld3.parse_htmlstring(html)
        affiliate_page.render()

        return affiliate_page.root.write_htmlstring()

