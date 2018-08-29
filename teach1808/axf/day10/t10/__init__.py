from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .mysigal import mysigal

def pre_save_admin(sender,**kwargs):
    print(sender)
    print(kwargs)

pre_save.connect(pre_save_admin)

@receiver(post_save)
def hehe(sender,**kwargs):
    print(sender)
    print(kwargs)

@receiver(mysigal)
def callback(sender,**kwargs):
    print(sender)
    print(kwargs)