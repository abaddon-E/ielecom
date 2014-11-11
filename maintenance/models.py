from django.db import models
from randomslugfield.fields import RandomSlugField
from django.utils.translation import ugettext as _


class Customer(models.Model):
    fullname = models.CharField(max_length=50, verbose_name=_('fullname'))
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name=_('phone'))
    mobile = models.CharField(max_length=15, null=True, blank=True, verbose_name=_('mobile'))

    def __unicode__(self):
        return self.fullname

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('customer')


class Device(models.Model):
    model = models.CharField(max_length=20, verbose_name=_('model'))
    sn = models.CharField(max_length=20, verbose_name=_('serial'))
    own = models.ForeignKey(Customer, verbose_name=_('own'))
    last_service = models.DateField(null=True, blank=True, verbose_name=_('last_service'))

    def __unicode__(self):
        return u'%s ==> %s' % (self.model, self.own)

    class Meta:
        verbose_name = _('Device')
        verbose_name_plural = _('device')


class FollowM(models.Model):
    in_wait = 'Wait'
    in_check = 'Check'
    repaired = 'Success'
    status_choices = (
        (in_wait, _('in_wait')),
        (in_check, _('in_check')),
        (repaired, _('repaired')),
    )
    serial = RandomSlugField(primary_key=True, unique=True, editable=False, length=6,
                             exclude_lower=True, exclude_upper=True,
                             exclude_vowels=True, verbose_name=_('follow_serial'))
    status = models.CharField(max_length=7, choices=status_choices, default=in_wait, verbose_name=_('status'))
    device = models.ForeignKey(Device,verbose_name=_('device'))
    date = models.DateField(verbose_name=_('date'))

    def __unicode__(self):
        return u'%s %s %s' % (self.serial, self.device, self.date)

    class Meta:
        verbose_name = _('Follow')
        verbose_name_plural = _('follow')


