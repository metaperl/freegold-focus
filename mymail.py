import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send(text, html, email, name, cc):

    import smtplib

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    me = "ElDorado@FreeGold.Biz"
    you = email

    COMMASPACE = ', '
    addressees = [you, cc, 'terrence.brannon@gmail.com']

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Karatbars replicated website for {0}".format(name)
    msg['From'] = me
    msg['To'] = COMMASPACE.join(addressees)


    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('localhost')

    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(me, addressees, msg.as_string())
    s.quit()
