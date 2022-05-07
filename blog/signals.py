from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def post_save_user(created, **kwargs):
    instance = kwargs['instance']
    if created:
        print(f'Save user', {instance.username})
    else:
        print(f'User updated', {instance.username})


@receiver(post_save, sender=User)
def post_save_user(sender, **kwargs):
    grp = Group.objects.get(name='author')
    user = kwargs.get('instance')
    if not user.groups.contains(grp):
        user.groups.add(grp)
        user.save()
    print('Save group', user)
