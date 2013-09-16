
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

    def __init__(self, kb_id, base_dir='', html_file='index.html'):
        self.base_dir = base_dir
        self.html_file = full_path(self.base_dir, html_file)
        self.p = AffiliateModel(kb_id).affiliate

        self.supreme_team_url = '/?s={0}'.format(kb_id)
        self.supreme_team_url_corp = '/?s={0}&opener=corp'.format(kb_id)
        self.supreme_team_url_uk = '/?s={0}&opener=uk'.format(kb_id)
        self.affiliate_url = 'http://karatbars.com/signup.php?s={0}'.format(kb_id)

        self.landing_url = 'http://karatbars.com/landing/?s={0}'.format(kb_id)

        self.superior_url = '/superior/{0}'.format(kb_id)
        self.buy_gold_url = '/buygold/{0}'.format(kb_id)
        self.get13kilos_url = '/get13kilos/{0}'.format(kb_id)

        self.skype_url = 'skype:{0}?add'.format(self.p.skype)
        self.kbgold_uk_url = 'http://www.karatbarsgold.co.uk/{0}'.format(self.p.kbuk_id)
        self.email_href = 'mailto:{0}'.format(self.p.email)

    def render(self):
        self.root.findmeld('affiliate_url').attributes(href=self.affiliate_url)


class Superior(AffiliatePage):

    def __init__(self, kb_id):
        super(Superior, self).__init__(kb_id, base_dir='superior')

    def render(self):
        super(Superior, self).render()
        for affiliate_url_id in 'affiliate_url2 affiliate_url3'.split():
            self.root.findmeld(affiliate_url_id).attributes(href=self.affiliate_url)

        self.root.findmeld('name').content(self.p.name)
        self.root.findmeld('name_in_title').content("{0}'s Superior Retirement Plan with Karatbars International".format(self.p.name))
        self.root.findmeld('pic').attributes(src=self.p.pic)
        self.root.findmeld('skype_url').attributes(href=self.skype_url)
        self.root.findmeld('skype_id').content(self.p.skype)

        self.root.findmeld('home').attributes(href=self.supreme_team_url)
        self.root.findmeld('buy_gold_url').attributes(href=self.buy_gold_url)
        self.root.findmeld('get13kilos_url').attributes(href=self.get13kilos_url)

class BuyGold(AffiliatePage):

    def __init__(self, kb_id):
        super(BuyGold, self).__init__(kb_id, base_dir='buygold')

    def render(self):
        super(BuyGold, self).render()
        for affiliate_url_id in 'affiliate_url2 affiliate_url3'.split():
            self.root.findmeld(affiliate_url_id).attributes(href=self.affiliate_url)

        self.root.findmeld('home').attributes(href=self.superior_url)
        self.root.findmeld('name_in_title').content("Buy Gold from {0} with Karatbars International".format(self.p.name))
        #self.root.findmeld('pic').attributes(src=self.p.pic)

class Get13Kilos(AffiliatePage):

    def __init__(self, kb_id):
        super(Get13Kilos, self).__init__(kb_id, base_dir='get13kilos')

    def render(self):
        super(Get13Kilos, self).render()
        for affiliate_url_id in 'affiliate_url2'.split():
            self.root.findmeld(affiliate_url_id).attributes(href=self.affiliate_url)

        self.root.findmeld('home').attributes(href=self.superior_url)
        self.root.findmeld('name_in_title').content("Buy Gold from {0} with Karatbars International".format(self.p.name))

        self.root.findmeld('buy_gold_url').attributes(href=self.buy_gold_url)

class Reese(AffiliatePage):

    def __init__(self, kb_id, opener='selina.html', html_file='index.html'):
        self.opener = opener
        self.src = {
            'corp': 'http://www.youtube.com/embed/0lrqEGlu0Fo',
            'uk': 'http://www.youtube.com/embed/30MfCTLhdZ4',
            'selina' : 'http://www.youtube.com/embed/37l6Wdzw490'
        }
        super(Reese, self).__init__(kb_id)
        self.shop_url = 'http://karatbars.com/shop/?s={0}'.format(kb_id)
        self.main_url = 'http://karatbars.com/?s={0}'.format(kb_id)
        self.mentor_url = '/trainwith/{0}'.format(kb_id)


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

        self.root.findmeld('shop_url').attributes(href=self.shop_url)
        self.root.findmeld('main_url').attributes(href=self.main_url)
        self.root.findmeld('mentor_url').attributes(href=self.mentor_url)


class ReeseMentor(AffiliatePage):

    def __init__(self, kb_id):
        super(ReeseMentor, self).__init__(kb_id, 'trainwith')
        self.lttw_url = 'http://www.littletickettowealth.com/?id={0}'.format(self.p.lttw_id)

    def render(self):

        super(ReeseMentor, self).render()

        self.root.findmeld('kbgold_uk_url').attributes(href=self.kbgold_uk_url)
        self.root.findmeld('kbgold_uk_url2').attributes(href=self.kbgold_uk_url)
        self.root.findmeld('lttw_url').attributes(href=self.lttw_url)

        self.root.findmeld('supreme_team_url').attributes(href=self.supreme_team_url)
        self.root.findmeld('supreme_team_url2').attributes(href=self.supreme_team_url)
        self.root.findmeld('supreme_team_url_corp').attributes(href=self.supreme_team_url_corp)
        self.root.findmeld('supreme_team_url_uk').attributes(href=self.supreme_team_url_uk)

        self.root.findmeld('superior_url').attributes(href=self.superior_url)

        self.root.findmeld('landing_url').attributes(href=self.landing_url)

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
    def superior(self, s, cmpg=None, banner=None):
        return self.render(Superior(s))

    @cherrypy.expose
    def buygold(self, s, cmpg=None, banner=None):
        return self.render(BuyGold(s))

    @cherrypy.expose
    def get13kilos(self, s, cmpg=None, banner=None):
        return self.render(Get13Kilos(s))

    @cherrypy.expose
    def trainwith(self, s):
        return self.render(ReeseMentor(s))

