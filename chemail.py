import smtplib
import credentials as cred

port = 587
host = 'smtp.gmail.com'


def send_email(subject, body):
    content = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP(host, port) as smtp:
        smtp.starttls()
        smtp.login(cred.sender_email, cred.app_pw)
        smtp.sendmail(cred.sender_email, cred.receiver_email, content)
