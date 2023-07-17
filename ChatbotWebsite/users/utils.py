from flask import url_for, current_app
from flask_mail import Message
import secrets
import os
from PIL import Image
from ChatbotWebsite import mail


# function to save the user profile picture
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, "static/profile_images", picture_fn
    )
    output_size = (190, 190)
    image = Image.open(form_picture).convert("RGB")
    image.thumbnail(output_size)
    image.save(picture_path)

    return picture_fn


# function to send the reset password email
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        "Password Reset Request", sender="noreply@chatbot.com", recipients=[user.email]
    )
    msg.body = f"""To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
Please do not reply to this email and share this email with anyone.
    
If you did not make this request then simply ignore this email and no changes will be made.
"""
    mail.send(msg)
