# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils import timezone

STATUS_CHOICES = ((1, 'Yes'),(0, 'No'),)
PRIORITY_CHOICES = (('1', 'High'),('2', 'Medium'),('3', 'Low'),)


class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)
    parent = models.ForeignKey("self", null=True, blank=True, default=None,
            on_delete=models.CASCADE)
    category_name = models.CharField("Category Name",
            max_length=100, blank=False)
    status = models.BooleanField('Status', default=1,
            choices=STATUS_CHOICES, blank=False)
    def __str__(self):
        return self.category_name


class SSLCertificate(models.Model):
    category = models.ForeignKey(Category)
    url = models.URLField("URL", blank=False)
    date = models.DateTimeField("Date", default=timezone.now,
            blank=False)
    save_copy = models.BooleanField('Save copy', default=1,
            choices=STATUS_CHOICES, blank=False)
    priority = models.CharField("Priority", default='3',
            choices=PRIORITY_CHOICES, max_length=7, blank=False)
    status = models.BooleanField('Status', default=1,
            choices=STATUS_CHOICES, blank=False)

    def __str__(self):
        return self.url

