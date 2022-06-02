from django.contrib import admin
from .models import NotificationModel
# Register your models here.


@admin.register(NotificationModel)
class NotificationModelAdmin(admin.ModelAdmin):
    list_display = ("is_seen", "note")
