import os;
import smtplib

EMAIL_ADDRESS = os.environ.get("BLOGIN_EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("BLOGIN_EMAIL_PASS")

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    subject = 'testing'
    body = 'testing still'
    msg = message = 'To reset your password visit the following link:\nIf not made by you then simply ignore and no changes will be made.'
    smtp.sendmail(EMAIL_ADDRESS,'dk0018w@gmail.com',msg)
    