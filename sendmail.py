from configparser import ConfigParser
from smtplib import SMTP
from email.message import EmailMessage
import sys


def dprint(s: str):
    """Helper function for debug printing... uses global variable DEBUG"""
    global DEBUG
    if DEBUG:
        print(s)


config = ConfigParser()
config.read('mail.ini')

DEBUG = config['DEBUG'].getboolean('debug')

CONFIG_SMTP = config['SMTP']
CONFIG_RECIPIENTS = config['RECIPIENTS']

SMTP_HOST = CONFIG_SMTP.get('host')
SMTP_PORT = CONFIG_SMTP.getint('port')
SMTP_USER = CONFIG_SMTP.get('user')
SMTP_PASS = CONFIG_SMTP.get('password')
SMTP_AUTH = CONFIG_SMTP.getboolean('user_auth')
START_TLS = CONFIG_SMTP.getboolean('tls')
SENDER = CONFIG_SMTP.get('sender')

dprint(f'''
SMTP_HOST: {SMTP_HOST}
SMTP_PORT: {SMTP_PORT}
SMTP_USER: {SMTP_USER}
SMTP_PASS: {SMTP_PASS}
SMTP_AUTH: {SMTP_AUTH}
START_TLS: {START_TLS}
SENDER:    {SENDER}
''')

msg = EmailMessage()
msg.set_content('Testmail from python')
msg['Subject'] = 'Testmail'
msg['From'] = SENDER
msg['To'] = CONFIG_RECIPIENTS.get('to')
msg['Cc'] = CONFIG_RECIPIENTS.get('cc')
msg['Bcc'] = CONFIG_RECIPIENTS.get('bcc')

dprint(f'''
SUBJECT: {msg['Subject']}
FROM:    {msg['From']}
TO:      {msg['To']}
CC:      {msg['Cc']}
BCC:     {msg['Bcc']}
''')


try:
    with SMTP(host = SMTP_HOST, port = SMTP_PORT) as smtp:
        dprint('smtp start...')
        if START_TLS: 
            dprint('starttls...')
            smtp.starttls()
        if SMTP_AUTH: 
            dprint('authenticate...')
            smtp.login(SMTP_USER, SMTP_PASS)
        dprint('try to send...')
        smtp.send_message(msg)
    print('email sucessfully send')
except Exception as ex:
    print('error while sending mail', ex)
    sys.exit(1)