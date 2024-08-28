from django.db import models
from django.utils.translation import gettext_lazy as _

class Contact(models.Model):
    location = models.CharField(max_length=200, null=True, verbose_name=_("Location"))
    telegram = models.URLField(max_length=200, null=True, verbose_name=_("Telegram"))
    instagram = models.URLField(max_length=200, null=True, verbose_name=_("Instagram"))
    call1 = models.CharField(max_length=15, null=True, verbose_name=_("Call"))
    call2 = models.CharField(max_length=15, null=True, verbose_name=_("Call"))

    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _("Link")