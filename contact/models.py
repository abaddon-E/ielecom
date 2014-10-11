from django.db import models


class Contact(models.Model):
    subject = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateField()
    ip = models.IPAddressField()

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.subject, self.email, self.message, self.date, self.ip)


class Email(models.Model):
    email = models.EmailField()
    ip = models.IPAddressField()
    date = models.DateTimeField()

    def __unicode__(self):
        return u'%s %s %s' % (self.email, self.ip, self.date)