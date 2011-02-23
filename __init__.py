from django.contrib.comments.models import Comment, FreeComment
from django.core.mail import send_mail
from django.dispatch import dispatcher
from django.db.models import signals

def comment_notification(sender, instance):
    subject = 'New Comment on %s' % instance.get_content_object().title
    msg = 'Comment text:\n\n%s' % instance.comment
    send_mail(subject, msg, 'bmheight@gmail.com', ['lasko@djangoblog.net'])

dispatcher.connect(comment_notification, sender=FreeComment, signal=signals.post_save)
dispatcher.connect(comment_notification, sender=Comment, signal=signals.post_save)
