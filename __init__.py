from django.db.models.signals import post_save
from django.core.mail import mail_admins
from django.contrib.comments.models import Comment

def notify_of_comment(sender, instance, **kwargs):
    message = 'A new comment has been posted.\n'
    message += instance.get_as_text()
    mail_admins('New Comment', message)

post_save.connect(notify_of_comment, sender=Comment)
