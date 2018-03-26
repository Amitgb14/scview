# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from datetime import datetime

from .models import Category, SSLCertificate, RawCertificate


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'user', 'parent', 'category_name', 'status')

class SSLCertificateSerializer(serializers.ModelSerializer):
    # date_ = serializers.DateTimeField(source='date')
    # datetime_object = date_.source.strftime('%b. %d, %Y, %H:%M %p')
    class Meta:
        model = SSLCertificate
        fields = ('id', 'category', 'url', 'date', 'save_copy', 'priority',
                'status')
class RawCertificateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RawCertificate
        fields = ('id', 'certificate', 'raw_text', 'date', 'status')
