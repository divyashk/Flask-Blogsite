import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import  mail
import smtplib




def save_picture(form_picture):
    random_hex = secrets.token_hex(8);
    _, f_ext = os.path.splitext(form_picture.filename);
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile-pic', picture_fn)
    output_size = (200,200);
    i = Image.open(form_picture);
    i.thumbnail(output_size);
    i.save(picture_path);
    return picture_fn




def send_email(user):

    EMAIL_ADDRESS = os.environ.get("BLOGIN_EMAIL_USER")
    EMAIL_PASSWORD = os.environ.get("BLOGIN_EMAIL_PASS")


    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        subject = 'Password Reset for Blogin'
        token = user.get_reset_token()
        body = 'To reset your password visit the following link:{}.\nIf not made by you then simply ignore and no changes will be made.'.format(url_for('users.reset_token', token = token, _external=True))
        msg = f'Subject: {subject}\n\n {body}'
        smtp.sendmail(EMAIL_ADDRESS, user.email, msg)
