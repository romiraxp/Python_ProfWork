import email
import smtplib
import imaplib
# в оригинале использовали это, но с ним не работало у меня
# from email.MIMEText import MIMEText  
# from email.MIMEMultipart import MIMEMultipart
# заменимл на это
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Post.inputs import GMAIL_IMAP, GMAIL_SMTP
class Post:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def send_email(self, recipients, subject, message):
        # send message
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.login, self.password)
        # в оригинале использовали это, но с ним не работало у меня        
        # ms.sendmail(l,ms, msg.as_string())
        # заменил ms на msg['To']
        ms.sendmail(self.login, msg['To'], msg.as_string())

        ms.quit()
        # send end

    def receive_email(self, header):
        # recieve
        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid ('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        # в оригинале использовали это, но с ним не работало у меня
        # email_message = email.message_from_string(raw_email)
        # заменил email.message_from_string на email.message_from_bytes
        email_message = email.message_from_bytes(raw_email)
        mail.logout()
        # end recieve
        return email_message # возращаем результат