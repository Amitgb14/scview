# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, permissions

from .models import Category, SSLCertificate, RawCertificate
from .serializers import (CategorySerializer,
        SSLCertificateSerializer,
        RawCertificateSerializer)



class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = permissions.IsAuthenticatedOrReadOnly,

class SSLCertificateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SSLCertificate to be viewed or edited.
    """
    queryset = SSLCertificate.objects.all()
    serializer_class = SSLCertificateSerializer
    # permission_classes = permissions.IsAuthenticatedOrReadOnly,

class RawCertificateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SSLCertificate to be viewed or edited.
    """
    queryset = RawCertificate.objects.all()
    serializer_class = RawCertificateSerializer
    # permission_classes = permissions.IsAuthenticatedOrReadOnly,


