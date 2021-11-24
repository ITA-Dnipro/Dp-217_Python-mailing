from flask import Flask, render_template, url_for, request, Response
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail:
    port = 465
    smtp_server_domain_name = 'smtp.gmail.com'
    sender_mail = 'dp217py@gmail.com'
    password = '51729pa$$'

    def __init__(self, data):
        self.email = data['mail']
        self.text_template = data['text']
        self.subject = data['subject']

    def send_mail(self):
        report = ""
        try:
            service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port)
            service.login(self.sender_mail, self.password)

            mail = MIMEMultipart('alternative')
            mail['Subject'] = self.subject
            mail['From'] = self.sender_mail
            mail['To'] = self.email

            # html_content = MIMEText(html_template, 'html')
            text_content = MIMEText(self.text_template, 'plain')

            mail.attach(text_content)
            # mail.attach(html_content)

            service.sendmail(self.sender_mail, self.email, mail.as_string())
            report += f"Mail to {self.email} was sent.\n"
            report += "Mails was sent!"
            return report

        except Exception as _ex:
            return f'{_ex}\nSend mail error!'

        finally:
            service.quit()
