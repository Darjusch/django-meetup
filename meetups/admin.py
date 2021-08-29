from django.contrib import admin
from .models import Meetup, Location, Organizer, Participant

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'date', 'organizer_email') 
    list_filter = ('location', 'date', 'organizer_email') 
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
admin.site.register(Organizer)