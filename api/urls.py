# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers

from userinfo.views import UserViewSet, MessageViewSet
from certmngt.views import (CategoryViewSet,
        SSLCertificateViewSet,
        RawCertificateViewSet)


router = routers.DefaultRouter()
router.register(r'user/userinfo', UserViewSet)
router.register(r'user/message', MessageViewSet)


router.register(r'certificate/category', CategoryViewSet)
router.register(r'certificate/certificate', SSLCertificateViewSet)
router.register(r'certificate/rawcertificate', RawCertificateViewSet)

urlpatterns = [

   url(r'^', include(router.urls)),

]
