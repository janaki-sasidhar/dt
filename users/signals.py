from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

user = get_user_model()

@receiver(post_save,sender=user)
def author_post_save(sender,instance,created,**kwargs):
    if created:
        print('yes')
        print(instance)
