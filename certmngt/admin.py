# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Category, SSLCertificate, RawCertificate


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'parent', 'category_name', 'status')
admin.site.register(Category, CategoryAdmin)

class SSLCertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'url', 'date', 'save_copy', 'priority',
            'status')
admin.site.register(SSLCertificate, SSLCertificateAdmin)

class RawCertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'certificate', 'raw_text', 'date', 'status')
admin.site.register(RawCertificate, RawCertificateAdmin)
