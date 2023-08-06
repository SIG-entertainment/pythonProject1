from django.conf import settings
from django.db.models.signals import post_save,  m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Post, PostCategory, Category
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives


def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
    {
        'text': preview,
        'link': f'{settings.SITE_URL}/news/{pk}'
    }
    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def post_created(instance, sender, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.postCategory.all()
        subscribers = []

        for cat in categories:
            subscribers += cat.subscribers.all()
        subscribers = [s.email for s in subscribers]
        send_notifications(instance.preview(), instance.pk, instance.title, subscribers)

    # emails = User.objects.filter(
    #     email=instance.postCategory.name
    # ).values_list('email', flat=True)

    # subject = f'New post in category {instance.postCategory.name}'
    #
    # text_content = (
    #     f'Post: {instance.title}\n'
    #     f'Author: {instance.author.authorUser.username}\n\n'
    #     f'Link to the post: http://127.0.0.1:8000{instance.get_absolute_url()}'
    # )
    # html_content = (
    #     f'Post: {instance.title}<br>'
    #     f'Author: {instance.author.authorUser.username}<br><br>'
    #     f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
    #     f'Link to post</a>'
    # )
    # for email in subscribers_emails:
    #     msg = EmailMultiAlternatives(subject, text_content, None, [email])
    #     msg.attach_alternative(html_content, "text/html")
    #     msg.send()
# @receiver(post_save, sender=Category)
# def post_created(instance, created, **kwargs):
#     if not created:
#         return
#
#     categories = instance.postCategory.all()
#     subscribers_emails = []
#     for cat in categories:
#         subscribers = cat.subscibers.all()
#         subscribers_emails += [s.email for s in subscribers]
#
#     emails = subscribers_emails
#     # emails = User.objects.filter(
#     #     email=instance.postCategory.name
#     # ).values_list('email', flat=True)
#
#     subject = f'New post in category {instance.postCategory.name}'
#
#     text_content = (
#         f'Post: {instance.title}\n'
#         f'Author: {instance.author.authorUser.username}\n\n'
#         f'Link to the post: http://127.0.0.1:8000{instance.get_absolute_url()}'
#     )
#     html_content = (
#         f'Post: {instance.title}<br>'
#         f'Author: {instance.author.authorUser.username}<br><br>'
#         f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
#         f'Link to post</a>'
#     )
#     for email in emails:
#         msg = EmailMultiAlternatives(subject, text_content, None, [email])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()

    # print('Post created', instance)
    # print(emails)
    #
