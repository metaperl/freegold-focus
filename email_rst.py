import os
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

def send(rst, html, email, cc):
    from mailer import Mailer
    from mailer import Message

    message = Message(From="binarypower@TerrenceBrannon.com",
                  To=email,
                      CC=cc,
                      BCC='thequietcenter@gmail.com',
                  charset="utf-8")
    message.Subject = "Your karatbars replicated website"
    message.Html = html
    message.Body = rst

    sender = Mailer('localhost')
    sender.send(message)


kb_id = 'princepawn'
sponsor_id = 'supreme'
email = 'schemelab@gmail.com'
cc = 'metaperl@gmail.com'

def main(kb_id, sponsor_id, email, cc):
    rst = templated(kb_id, sponsor_id)
    html = htmlized(rst)
    send(rst, html, email, cc)
    return html

if __name__ == '__main__':
    main()
