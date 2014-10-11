from django.db import models
from randomslugfield.fields import RandomSlugField
from django.utils.translation import ugettext_lazy as _


class Customer(models.Model):
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)

    def __unicode__(self):
        return self.fullname


class Device(models.Model):
    model = models.CharField(max_length=20)
    sn = models.CharField(max_length=20)
    own = models.ForeignKey(Customer)
    last_service = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return u'%s ==> %s' % (self.model, self.own)


class FollowM(models.Model):
    in_wait = 'Wait'
    in_check = 'Check'
    repaired = 'Success'
    status_choices = (
        (in_wait, 'in_wait'),
        (in_check, 'in_check'),
        (repaired, 'repaired'),
    )
    serial = RandomSlugField(primary_key=True, unique=True, editable=False, length=6,
                             exclude_lower=True, exclude_upper=True, exclude_vowels=True)
    status = models.CharField(max_length=7, choices=status_choices, default=in_wait)
    device = models.ForeignKey(Device)
    date = models.DateField()

    def __unicode__(self):
        return u'%s %s %s' % (self.serial, self.device, self.date)

    class Meta:
        verbose_name = _('Follow')
        verbose_name_plural = _('follow')

