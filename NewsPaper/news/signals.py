from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import PostCategory
from .tasks import send_notify


@receiver(m2m_changed, sender=PostCategory)
def post_notify(sender, instance, **kwargs):
    print("I'm signal!!!")
    if kwargs['action'] == 'post_add':
        print("I'm ready!!!")
        categories = instance.postCategory.all()
        subscribers_emails = []

        for category in categories:

            subscribers = category.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]

        send_notify.delay(instance.preview(), instance.pk, instance.title, subscribers_emails,)