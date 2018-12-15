# core
import os
import sys

# 3rd party
import argh

# local
import mymail


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
    from marrow.mailer import Mailer, Message

    mailer = Mailer(
        dict(
            transport = dict(
                use = 'smtp',
                host = 'localhost')))

    mailer.start()

    message = Message(
        author="FindYourTwoAndBeFree@TerrenceBrannon.com",
        to=email,
        cc=cc,
        bcc='thequietcenter@gmail.com'
    )

    message.subject = "Karatbars replicated website for {0}".format(name)
    message.rich = html
    message.plain = rst

    mailer.send(message)
    mailer.stop()

def main(kb_id, kb_email, kb_name, sponsor_id, sponsor_email):
    cc = sponsor_email
    rst = templated(kb_id, sponsor_id)
    html = htmlized(rst)

    import mymail

    mymail.send(rst, html, kb_email, kb_name, cc)
    return html

if __name__ == '__main__':
    argh.dispatch_command(main)
