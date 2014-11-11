from django.db import models
from django.utils.translation import ugettext as _

#coding: utf-8
#-*- encoding=UTF-8 -*-


class Contact(models.Model):
    subject = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateField()
    ip = models.IPAddressField()

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Message')


class Email(models.Model):
    email = models.EmailField()
    ip = models.IPAddressField()
    date = models.DateTimeField()

    def __unicode__(self):
        return u'%s %s %s' % (self.email, self.ip, self.date)