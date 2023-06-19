from django.contrib import admin
from . import models

admin.site.register(models.HRRepresentative),
admin.site.register(models.MeetingReservation)
