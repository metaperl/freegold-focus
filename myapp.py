
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
        p = session.query(Affiliate).get(self.kb_id)
        if p is None:
            raise Exception("could not locate affiliate instance with primary key {0}".format(self.kb_id))
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


class Superior(AffiliatePage):

    def __init__(self, kb_id, html_file='index.html'):
        super(Superior, self).__init__(kb_id, html_file=html_file)
        self.base_dir = 'superior'
        self.html_file = full_path(self.base_dir, html_file)

    def render(self):
        pass


class Reese(AffiliatePage):

    def __init__(self, kb_id, opener):
        self.opener = opener
        self.src = {
            'corp': 'http://www.youtube.com/embed/0lrqEGlu0Fo',
            'uk': 'http://www.youtube.com/embed/30MfCTLhdZ4',
            'selina' : 'http://www.youtube.com/embed/37l6Wdzw490'
        }
        super(Reese, self).__init__(kb_id)

    def followers(self):
        followers = dict(self.lead_and_followers(l) for l in self.src.keys())
        return followers

    def lead_and_followers(self, lead):
        followers = self.src.keys()
        followers.remove(lead)
        return (lead, followers)

    def render(self):

        super(Reese, self).render()

        def autoplay(u): return '{0}?autoplay=1'.format(u)

        followers = self.followers()

        carousel = dict(
            opener=autoplay(self.src[self.opener]),
            follower = self.src[followers[self.opener][0]],
            follower2 = self.src[followers[self.opener][1]]
        )

        for meld_id, url in carousel.iteritems():
            self.root.findmeld(meld_id).attributes(src=url)


class ReeseMentor(Reese):

    def __init__(self, kb_id, opener='selina'):
        super(ReeseMentor, self).__init__(kb_id, opener)

    def render(self):
        pass

class Root(object):

    def render(self, affiliate_page):

        with open(affiliate_page.html_file, 'r') as fp:
            html = fp.read()

        affiliate_page.root = meld3.parse_htmlstring(html)
        affiliate_page.render()

        return affiliate_page.root.write_htmlstring()

    @cherrypy.expose
    def index(self, s="supreme", opener='selina', cmpg=None, banner=None):

        return self.render(Reese(s, opener))


    @cherrypy.expose
    def superior(self, s="supreme", cmpg=None, banner=None):

        return self.render(Superior(s))


