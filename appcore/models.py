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

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s %s' % (self.first_name, self.last_name, self.second_surname)

        return full_name.strip()

    class Meta:
        db_table = 'user'


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
    date_created = models.DateTimeField(default=timezone.now, )
    date_update = models.DateTimeField(null=True, )

    class Meta:
        db_table = 'ticket'
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
