
# imports
## core
import importlib
import logging
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
import email_rst
from saorm import *

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)


def make_session():
    from sqlalchemy.orm import sessionmaker
    session = sessionmaker(bind=engine)()
    return session

def session_commit(session):
    session.flush()
    session.commit()

class AffiliateModel(object):

    def __init__(self, kb_id):
        self.kb_id=kb_id
        self.affiliate = self.person()

    def person(self):
        #example on how to query your Schema
        session = make_session()
        p = session.query(Affiliate).get(self.kb_id)
        if p is None:
            raise Exception("could not locate affiliate instance with primary key {0}".format(self.kb_id))
        return p

    @staticmethod
    def shorten(s, length):
        if len(s) <= length:
            return s
        else:
            return "{0} ...".format(s[0:length])

    @staticmethod
    def prepare_email(e):
        if len(e) > 25:
            return "Click here to email"
        else:
            return e


class AffiliatePage(object):

    def __init__(self, kb_id, base_dir='', html_file='index.html'):
        self.kb_id = kb_id
        self.base_dir = base_dir
        self.html_file = full_path(self.base_dir, html_file)
        self.p = AffiliateModel(kb_id).affiliate

        self.gfg_url = 'http://{0}.GarageFullOfGold.com'.format(kb_id)


        self.supreme_team_url = '/?s={0}'.format(kb_id)
        self.supreme_team_url_contact = '/?s={0}#contact-link'.format(kb_id)
        self.supreme_team_url_corp = '/?s={0}&opener=corp'.format(kb_id)
        self.supreme_team_url_uk = '/?s={0}&opener=uk'.format(kb_id)
        self.supreme_team_contact_url = '/?s={0}#contact-link'.format(kb_id)

        self.affiliate_url = 'http://karatbars.com/signup.php?s={0}'.format(kb_id)
        self.intro_url = "/intro/{0}".format(kb_id)
        self.intro_iamgold_url = "{0}#theplan-link".format(self.intro_url) # http://localhost:8080/intro/bitcoin#theresults-link
        self.intro_pricing_url = "{0}#theprocess-link".format(self.intro_url)

        self.intro_kexchange_url = "/intro/{0}#theresults-link".format(kb_id)


        self.shop_url = 'http://karatbars.com/shop/?s={0}'.format(kb_id)
        self.main_url = 'http://karatbars.com/?s={0}'.format(kb_id)
        self.landing_url = 'http://karatbars.com/landing/?s={0}'.format(kb_id)
        self.mentor_url = '/trainwith/{0}'.format(kb_id)
        self.roadmap_details_url = self.mentor_url + '#roadmap'
        self.roadmap_landing_url = '/roadmap/{0}'.format(kb_id)


        self.corp_url = self.main_url
        self.corp_shop_url = self.shop_url
        self.corp_kexchange_url = 'http://karatbars.com/k-exchange/?s={0}'.format(kb_id)
        self.corp_landing_url = self.landing_url

        self.superior_url = '/superior/{0}'.format(kb_id)
        self.ben919_url = '/ben919/{0}'.format(kb_id)
        self.buy_gold_url = '/buygold/{0}'.format(kb_id)
        self.get13kilos_url = '/get13kilos/{0}'.format(kb_id)
        self.get3kilos_url = '/get3kilos/{0}'.format(kb_id)
        self.cyprus_url = '/cyprus/{0}'.format(kb_id)

        self.zimbabwe_url = '/zimbabwe/{0}'.format(kb_id)

        self.skype_url = 'skype:{0}?add'.format(self.p.skype)
        self.kbgold_uk_url = 'http://www.karatbarsgold.co.uk/{0}'.format(self.p.kbuk_id)
        self.email_href = 'mailto:{0}'.format(self.p.email)

    def render(self):
        self.root.findmeld('affiliate_url').attributes(href=self.affiliate_url)


class Superior(AffiliatePage):

    def __init__(self, kb_id, base_dir='superior'):
        super(Superior, self).__init__(kb_id, base_dir=base_dir)

    def render(self):
        super(Superior, self).render()
        for affiliate_url_id in 'affiliate_url2 affiliate_url3'.split():
            self.root.findmeld(affiliate_url_id).attributes(href=self.affiliate_url)

        self.root.findmeld('name').content(self.p.name)
        self.root.findmeld('name_in_title').content("{0}'s Superior Retirement Plan with Karatbars International".format(self.p.name))
        self.root.findmeld('pic').attributes(src=self.p.pic)
        self.root.findmeld('skype_url').attributes(href=self.skype_url)
        self.root.findmeld('skype_id').content(self.p.skype)
        self.root.findmeld('number').content(self.p.number)

        self.root.findmeld('home').attributes(href=self.supreme_team_url)
        self.root.findmeld('buy_gold_url').attributes(href=self.buy_gold_url)
        self.root.findmeld('get3kilos_url').attributes(href=self.get3kilos_url)

class Zimbabwe(AffiliatePage):

    def __init__(self, kb_id, base_dir='zimbabwe'):
        super(Zimbabwe, self).__init__(kb_id, base_dir=base_dir)

    def render(self):
        super(Zimbabwe, self).render()
        self.root.findmeld('supreme_team_url').attributes(href=self.supreme_team_url)

class Roadmap(AffiliatePage):

    def __init__(self, kb_id, base_dir='roadmap'):
        super(Roadmap, self).__init__(kb_id, base_dir=base_dir)

    def render(self):
        super(Roadmap, self).render()
        self.root.findmeld('roadmap_details_url').attributes(href=self.roadmap_details_url)

class Lookout(Zimbabwe):

    def __init__(self, kb_id):
        super(Lookout, self).__init__(kb_id, base_dir='lookout')

class Ben919(AffiliatePage):

    def __init__(self, kb_id):
        super(Ben919, self).__init__(kb_id, base_dir='ben919')
        self.affiliate_url_ids = ('affiliate_url{0}'.format(i) for i in xrange(2,9))
        self.cyprus_url = '/cyprus/{0}'.format(kb_id)


    def render(self):
        super(Ben919, self).render()
        for affiliate_url_id in self.affiliate_url_ids:
            self.root.findmeld(affiliate_url_id).attributes(href=self.affiliate_url)

        self.root.findmeld('name').content(self.p.name)
        self.root.findmeld('name_in_title').content("{0}'s Wealth Insurance Plan with Karatbars International".format(self.p.name))
        self.root.findmeld('pic').attributes(src=self.p.pic)
        self.root.findmeld('skype_id').content(self.p.skype)
        self.root.findmeld('number').content(self.p.number)

        self.root.findmeld('buy_gold_url').attributes(href=self.buy_gold_url)
        self.root.findmeld('get13kilos_url').attributes(href=self.get13kilos_url)

        for i in xrange(1,4):
            c = 'cyprus_url{0}'.format(i)
            self.root.findmeld(c).attributes(href=self.cyprus_url)


class Cyprus(AffiliatePage):

    def __init__(self, kb_id):
        super(Cyprus, self).__init__(kb_id, base_dir='cyprus')

    def render(self):
        self.root.findmeld('superior_url').attributes(href=self.superior_url)


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

class Get3Kilos(AffiliatePage):

    def __init__(self, kb_id):
        super(Get3Kilos, self).__init__(kb_id, base_dir='get3kilos')

    def render(self):
        super(Get3Kilos, self).render()
        for affiliate_url_id in 'affiliate_url2'.split():
            self.root.findmeld(affiliate_url_id).attributes(href=self.affiliate_url)

        self.root.findmeld('home').attributes(href=self.superior_url)
        self.root.findmeld('name_in_title').content("Buy Gold from {0} with Karatbars International".format(self.p.name))

        self.root.findmeld('buy_gold_url').attributes(href=self.buy_gold_url)



class Reese(AffiliatePage):

    def __init__(self, kb_id, opener, period):
        self.opener = opener
        self.src = {
            'corp': 'http://www.youtube.com/embed/hn2cVVJ99Sg',
            'uk': 'http://www.youtube.com/embed/30MfCTLhdZ4',
            'selina' : 'http://www.youtube.com/embed/37l6Wdzw490',
            'joe': 'http://youtube.com/embed/aBSCmgOyoxg',
            'simple': 'http://youtube.com/embed/qC2JUwE0zeY',
            'iamgold': 'http://youtube.com/embed/1Twnl6Lz0Nw',
            'silent': 'http://youtube.com/embed/jxR7VV7o-Pk',

        }
        self.period=period
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
            opener=autoplay(self.src[self.opener])
        )

        for meld_id, url in carousel.iteritems():
            self.root.findmeld(meld_id).attributes(src=url)

        for i in xrange(1,7):
            self.root.findmeld("period{0}".format(i)).content(self.period)

        #self.root.findmeld('kbgold_uk_url').attributes(href=self.kbgold_uk_url)
        self.root.findmeld('enroll_free').attributes(href=self.affiliate_url)
        #self.root.findmeld('contact_iframe').attributes(src=self.landing_url)
        self.root.findmeld('name').content(self.p.name)
        self.root.findmeld('name2').content(self.p.name)

        self.root.findmeld('name_in_title').content(
            "Karatbars International - {0}".format(self.p.name)
        )

        self.root.findmeld('pic').attributes(src=self.p.pic)
        self.root.findmeld('phone').content(self.p.number)
        self.root.findmeld('skype_url').attributes(href=self.skype_url)
        self.root.findmeld('skype_id').content(self.p.skype)
        self.root.findmeld('email_href').attributes(href=self.email_href)
        self.root.findmeld('email').content(AffiliateModel.prepare_email(self.p.email))

        self.root.findmeld('shop_url').attributes(href=self.shop_url)
        self.root.findmeld('main_url').attributes(href=self.main_url)
        self.root.findmeld('corp_url').content(self.main_url)
        self.root.findmeld('main_url2').attributes(href=self.main_url)

        self.root.findmeld('mentor_url').attributes(href=self.mentor_url)
        self.root.findmeld('intro_url').attributes(href=self.intro_url)
        self.root.findmeld('corp_kexchange_url').attributes(href=self.corp_kexchange_url)
        self.root.findmeld('intro_iamgold_url').attributes(href=self.intro_iamgold_url)
        self.root.findmeld('intro_pricing_url').attributes(href=self.intro_pricing_url)




class ReeseMentor(AffiliatePage):

    def __init__(self, kb_id):
        super(ReeseMentor, self).__init__(kb_id, 'trainwith')
        self.lttw_url = 'http://www.littletickettowealth.com/?id={0}'.format(self.p.lttw_id)


    def render(self):

        super(ReeseMentor, self).render()

        self.root.findmeld('roadmap_landing_url').attributes(href=self.roadmap_landing_url)
        self.root.findmeld('gfg_url').attributes(href=self.gfg_url)
        self.root.findmeld('supreme_team_url_contact').attributes(href=self.supreme_team_url_contact)

        self.root.findmeld('tools_register_url').attributes(href='/tools/{0}'.format(self.p.id))

        self.root.findmeld('supreme_team_url').attributes(href=self.supreme_team_url)
        self.root.findmeld('supreme_team_url2').attributes(href=self.supreme_team_url)
        self.root.findmeld('supreme_team_url3').attributes(href=self.supreme_team_url)
        self.root.findmeld('supreme_team_url_corp').attributes(href=self.supreme_team_url_corp)
        self.root.findmeld('supreme_team_url_uk').attributes(href=self.supreme_team_url_uk)
        self.root.findmeld('intro_url').attributes(href=self.intro_url)

        self.root.findmeld('superior_url').attributes(href=self.superior_url)
        self.root.findmeld('get13kilos_url').attributes(href=self.get13kilos_url)
        self.root.findmeld('buy_gold_url').attributes(href=self.buy_gold_url)
        self.root.findmeld('ben919_url').attributes(href=self.ben919_url)
        self.root.findmeld('cyprus_url').attributes(href=self.cyprus_url)

        self.root.findmeld('zimbabwe_url').attributes(href=self.zimbabwe_url)


        self.root.findmeld('landing_url').attributes(href=self.landing_url)

        self.root.findmeld('corp_url').attributes(href=self.corp_url)
        self.root.findmeld('corp_shop_url').attributes(href=self.corp_shop_url)
        self.root.findmeld('corp_kexchange_url').attributes(href=self.corp_kexchange_url)


        self.root.findmeld('name').content(self.p.name)
        self.root.findmeld('name_in_title').content(
            "{0} - Karatbars International Mentor Page".format(self.p.name)
        )

        self.root.findmeld('pic').attributes(src=self.p.pic)
        self.root.findmeld('phone').content(self.p.number)
        self.root.findmeld('skype_url').attributes(href=self.skype_url)
        self.root.findmeld('skype_id').content(self.p.skype)
        self.root.findmeld('email_href').attributes(href=self.email_href)
        self.root.findmeld('email').content(self.p.email)

class Intro(AffiliatePage):

    def __init__(self, kb_id, page):
        super(Intro, self).__init__(kb_id, 'intro')
        self.page=page
        self.snapback_url = '{0}&opener=silent#contact-link'.format(
            self.supreme_team_url)

    def render(self):
        super(Intro, self).render()

        # self.root.findmeld('tools_register_url').attributes(href='/tools/{0}'.format(self.p.id))
        #
        # self.root.findmeld('kbgold_uk_url').attributes(href=self.kbgold_uk_url)
        # self.root.findmeld('kbgold_uk_url2').attributes(href=self.kbgold_uk_url)
        # self.root.findmeld('lttw_url').attributes(href=self.lttw_url)
        #
        self.root.findmeld('supreme_team_url').attributes(href=self.supreme_team_url)
        self.root.findmeld('supreme_team_url2').attributes(href=self.supreme_team_url)
        self.root.findmeld('supreme_team_contact_url').attributes(href=self.snapback_url)
        # self.root.findmeld('supreme_team_url_uk').attributes(href=self.supreme_team_url_uk)
        #
        # self.root.findmeld('superior_url').attributes(href=self.superior_url)
        # self.root.findmeld('ben919_url').attributes(href=self.ben919_url)
        # self.root.findmeld('landing_url').attributes(href=self.landing_url)
        #
        self.root.findmeld('name').content(self.p.name)
        #self.root.findmeld('name2').content(self.p.name)
        #self.root.findmeld('main_url').attributes(href=self.main_url)
        #self.root.findmeld('corp_url').content(self.main_url)


        self.root.findmeld('name_in_title').content(
            "{0} - Karatbars International Intro Page".format(self.p.name)
        )

        self.root.findmeld('pic').attributes(src=self.p.pic)
        self.root.findmeld('phone').content(self.p.number)
        self.root.findmeld('skype_url').attributes(href=self.skype_url)
        self.root.findmeld('skype_id').content(self.p.skype)
        self.root.findmeld('email_href').attributes(href=self.email_href)
        self.root.findmeld('email').content(self.p.email)

class Tools(AffiliatePage):

    def __init__(self, kb_id):
        super(Tools, self).__init__(kb_id, 'tools')
        self.toolsform_url = '/toolsform/{0}'.format(kb_id)


    def render(self):
        super(Tools, self).render()
        self.root.findmeld('name').content(self.p.name)
        self.root.findmeld('supreme_team_url').attributes(href=self.supreme_team_url)
        self.root.findmeld('toolsform_url').attributes(src=self.toolsform_url)

class ToolsForm(AffiliatePage):

    def __init__(self, kb_id):
        super(ToolsForm, self).__init__(kb_id, 'tools/form')

    def render(self):
        super(ToolsForm, self).render()
        self.root.findmeld('sponsorid').attributes(value=self.kb_id)
        self.root.findmeld('sponsorid2').content(self.kb_id)
        self.root.findmeld('sponsoremail').attributes(value=self.p.email)

class ToolsRegister(object):

    def __init__(self, **dbargs):
        self.dbargs = dbargs

    @staticmethod
    def insert_affiliate(email, id, name, number, skype, pic='http://j.mp/17y4bFj'):
        a = Affiliate(
            email=email,
            id=id,
            name=name,
            number=number,
            pic=pic,
            skype=skype)

        session = make_session()
        session.add(a)
        session_commit(session)

    @staticmethod
    def email_affiliate(email, id, name, sponsor_id, sponsor_email):
        html = email_rst.main(
            id, email, name, sponsor_id, sponsor_email)
        return html

    @staticmethod
    def insert_and_email_affiliate(email, id, name, number, skype, sponsor_id, sponsor_email, pic='http://j.mp/17y4bFj'):
        ToolsRegister.insert_affiliate(email, id, name, number, skype, pic)
        return ToolsRegister.email_affiliate(email, id, name, sponsor_id, sponsor_email)

    def render(self):
        sponsor_id = self.dbargs.pop('sponsorid')
        sponsor_email  = self.dbargs.pop('sponsoremail')
        for deletable in 'lttw_id kbuk_id form_id submit'.split():
            self.dbargs.pop(deletable, None)


        for k,v in self.dbargs.iteritems():
            self.dbargs[k] = v.strip()

        self.insert_affiliate(**self.dbargs)

        html = self.email_affiliate(
            self.dbargs['email'], self.dbargs['id'], self.dbargs['name'],
            sponsor_id, sponsor_email)

        return html


class Root(object):

    def render(self, affiliate_page):

        with open(affiliate_page.html_file, 'r') as fp:
            html = fp.read()

        affiliate_page.root = meld3.parse_htmlstring(html)
        affiliate_page.render()

        return affiliate_page.root.write_htmlstring()

    @cherrypy.expose
    def index(self, s="supreme", opener='corp', cmpg=None, banner=None, period='week'):
        return self.render(Reese(s, opener, period))

    @cherrypy.expose
    def paidfast(self, s, cmpg=None, banner=None):
        raise cherrypy.HTTPRedirect(
            "/?s={0}&opener=simple".format(s))

    @cherrypy.expose
    def superior(self, s, cmpg=None, banner=None):
        return self.render(Superior(s))

    @cherrypy.expose
    def ben919(self, s, cmpg=None, banner=None):
        return self.render(Ben919(s))

    @cherrypy.expose
    def cyprus(self, s, cmpg=None, banner=None):
        return self.render(Cyprus(s))

    @cherrypy.expose
    def buygold(self, s, cmpg=None, banner=None):
        return self.render(BuyGold(s))

    @cherrypy.expose
    def get13kilos(self, s, cmpg=None, banner=None):
        return self.render(Get13Kilos(s))

    @cherrypy.expose
    def get3kilos(self, s, cmpg=None, banner=None):
        return self.render(Get3Kilos(s))

    @cherrypy.expose
    def tools(self, s):
        return self.render(Tools(s))

    @cherrypy.expose
    def toolsform(self, s):
        return self.render(ToolsForm(s))

    @cherrypy.expose
    def tools_register(self, **dbargs):
        return (ToolsRegister(**dbargs)).render()

    @cherrypy.expose
    def trainwith(self, s):
        return self.render(ReeseMentor(s))

    @cherrypy.expose
    def zimbabwe(self, s):
        return self.render(Zimbabwe(s))

    @cherrypy.expose
    def roadmap(self, s):
        return self.render(Roadmap(s))

    @cherrypy.expose
    def lookout(self, s):
        return self.render(Lookout(s))

    @cherrypy.expose
    def intro(self, s, page='pricing', cmpg=None, banner=None):
        return self.render(Intro(s, page))
