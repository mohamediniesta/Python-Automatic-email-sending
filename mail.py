import smtplib
import xlrd
from time import sleep
gmail_user = 'email'
gmail_password = "password"
sent_from = gmail_user
to = ""
subject = 'the subject of the mail'
body = """
your email message
"""

list = []
loc = "list.txt" # The list of emails that we want to sent them an email.


cpt = 0
k = 0
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)

for line in open(loc,'r'):
    email = line.strip()
    # Send 20 mail every minute.
    if cpt == 20:
        print("Wait 1 minute to continue ....")
        sleep(60)
        cpt = 0
    to = email
    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, to, subject, body)
    server.sendmail(sent_from, to, email_text.encode('utf-8'))
    print('Email sent to {0} !'.format(to))
    cpt = cpt + 1
    k = k + 1
server.close()
print("{0} Sent Emails".format(k))