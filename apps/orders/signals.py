# coding=utf-8

from django.core.mail import mail_admins
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order


@receiver(post_save, sender=Order, dispatch_uid='send_email')
def send_email_notification(sender, instance, **kwargs):
    mail_admins(u'Новый заказ', u'Поступил новый заказ {0}'.format(instance.pizza.name))
