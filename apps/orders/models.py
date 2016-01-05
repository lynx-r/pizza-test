from __future__ import unicode_literals

from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    pizza = models.ForeignKey(to=Pizza)

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.first_name, self.last_name, self.pizza.name)

from .signals import *