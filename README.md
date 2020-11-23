# Python SendMail example with ConfigFile

Sending mails with Python is very easy thanks to the standard library.

In this example, we're using the [smtplib](https://docs.python.org/3/library/smtplib.html#module-smtplib) to connect to a SMTP server
and [EmailMessage](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage) to create e simple text-mail, which will be send through 
the SMTP server.

We also read the mail configuration from a separate config-file, using the
[ConfigParser](https://docs.python.org/3/library/configparser.html#module-configparser) from the Python standardlib.


## Useful links
* [Python portable for Windows](https://github.com/winpython/winpython/releases)