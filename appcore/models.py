# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.


class User(AbstractUser):
    DEFAULT_SRC = 'images/avatars/profile.png'
    UPLOAD_SRC = 'images/avatars/'

    second_surname = models.CharField(_('second surname'), max_length=30, blank=True, )
    avatar = models.ImageField(upload_to=UPLOAD_SRC, default=DEFAULT_SRC, null=True, blank=True, )
    role = models.ForeignKey('Role', verbose_name=_('Role'), on_delete=models.CASCADE, null=True, blank=True, )

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s %s' % (self.first_name, self.last_name, self.second_surname)

        return full_name.strip()

    class Meta:
        db_table = 'user'


class Role(models.Model):
    name = models.CharField(_('Role'), max_length=50, unique=False, default="", )
    is_active = models.BooleanField(_('Active'), default=True, help_text=_('is active'), )
    date_created = models.DateTimeField(_('date created'), default=timezone.now, )
    date_update = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'role'
        verbose_name_plural = _('Type of roles')
        verbose_name = _('Role')


class Ticket(models.Model):
    STATUS_CHOICES = (
        (1, 'Abierto'),
        (2, 'Pendiente'),
        (3, 'En proceso'),
        (4, 'Resuelto'),
        (5, 'Cerrado'),
    )

    title = models.CharField(max_length=80, )
    description = models.CharField(max_length=300, )
    status = models.IntegerField(choices=STATUS_CHOICES, default=2, )
    user = models.ForeignKey('User', verbose_name=_('User'), on_delete=models.CASCADE, null=True, blank=True, )
    date_created = models.DateTimeField(default=timezone.now, )
    date_update = models.DateTimeField(null=True, )

    def get_status(self):
        return dict(self.STATUS_CHOICES).get(self.status)

    class Meta:
        db_table = 'ticket'
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
