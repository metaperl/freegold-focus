#!/usr/bin/python


# core
import os

# 3rd party
import argh

# local


def full_path(*extra):
    return os.path.join(os.path.dirname(__file__), *extra)

rst_file = full_path('tools', 'new-user-welcome.rst')

def slurp():
    with open (rst_file, "r") as myfile:
        return myfile.read()

def templated(kb_id, sponsor_id):
    raw_file = slurp()
    customized = raw_file.format(kbid=kb_id, sponsorid=sponsor_id)
    return customized

def htmlized(rst):
    from docutils.core import publish_string
    return publish_string(rst, writer_name='html')

def send(rst, html, email, name, cc):
    from mailer import Mailer
    from mailer import Message

    message = Message(From="binarypower@TerrenceBrannon.com",
                  To=email,
                      CC=cc,
                      BCC='thequietcenter@gmail.com',
                  charset="utf-8")
    message.Subject = "Karatbars replicated website for {0}".format(name)
    message.Html = html
    message.Body = rst

    sender = Mailer('localhost')
    sender.send(message)


kb_id = 'bodytuner'
kb_email = 'denise@highonenergy.com'
kb_name = 'Denise Higgison'
sponsor_id = 'rikmccoy'
sponsor_email = 'rikmccoy@gmail.com'

def main(kb_id, kb_email, kb_name, sponsor_id, sponsor_email):
    cc = sponsor_email
    rst = templated(kb_id, sponsor_id)
    html = htmlized(rst)
    send(rst, html, kb_email, kb_name, cc)
    return html

if __name__ == '__main__':
    argh.dispatch_command(main)
