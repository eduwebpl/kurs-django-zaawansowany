from django.contrib import admin

from events.models import Event, EventDate


class EventDateInline(admin.TabularInline):
    model = EventDate
    readonly_fields = ('date',)


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    inlines = (EventDateInline,)
