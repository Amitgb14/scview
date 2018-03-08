# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Country, State, City, User, Message

class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'status')
admin.site.register(Country, CountryAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ('state_name', 'country', 'status')
admin.site.register(State, StateAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'state', 'status')
admin.site.register(City, CityAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
            'email', 'contact_no', 'status')
admin.site.register(User, UserAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'read',
            'date', 'status')
admin.site.register(Message, MessageAdmin)
