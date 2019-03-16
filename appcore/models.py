# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone


# Create your models here.


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
