from email.message import EmailMessage
import ssl
import smtplib
import schedule


def send_email():

    email_sender = "sender@domain.com"
    email_password = "password"
    email_receiver = "receiver@domain.com"

    subject = "Naslov"
    body = "Tekst"

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


def schedule_email():
    schedule.every().day.at("08:47").do(send_email)
