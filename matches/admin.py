# -*- coding: utf-8 -*-
from django.contrib import admin

from . import models


@admin.register(models.Match)
class MatchAdmin(admin.ModelAdmin):
    """
    Match admin panel configuration
    """
    fieldsets = [
        (None, {
            'fields': ['league', 'game', 'robot1', 'robot2']
        }),
    ]

    list_display = ('__str__', 'robot1', 'robot2', 'league', 'game',
                    'datetime')

    list_filter = ('league', 'game', 'datetime')

    search_fields = ('league', 'robot1', 'robot2')
