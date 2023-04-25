import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Sender:
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_message(self, recipient, subject, html_content):
        msg = MIMEMultipart('alternative')
        msg['From'] = self.username
        msg['To'] = recipient
        msg['Subject'] = subject

        html_body = MIMEText(html_content, 'html')
        msg.attach(html_body)

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(self.username, self.password)
            smtp.sendmail(self.username, recipient, msg.as_string())