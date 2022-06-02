from django.db import models
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class NotificationModel(models.Model):
    note =models.TextField()
    is_seen = models.BooleanField(default=False)


    def __str__(self):
        return self.note


    def save(self, *args, **kwargs):
        
        super(NotificationModel,self).save(*args, **kwargs)


@receiver(post_save, sender=NotificationModel)
def at_ending_save(sender, instance, created,**kwargs):
    if created:
        print(instance)
        channel_layer = get_channel_layer()
        print(channel_layer)
        notify = NotificationModel.objects.filter(is_seen=False).count() 
        print(notify)
        data = {
            'noti':notify, 'instance':instance.note
        }
        print(data)
        async_to_sync(channel_layer.group_send)(
            "test_notify_group",
            {
                'type':"send_notification",
                'value':json.dumps(data)
            }
        )

            