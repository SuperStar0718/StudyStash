from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    # Custom fields
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=150, unique=True, null=True)

    # Fields inherited from AbstractUser
    # username (already included in AbstractUser)
    # email (already included in AbstractUser)
    # password (already included in AbstractUser)

    # Additional fields (Optional, you can add more if needed)
    # age = models.IntegerField()
    # address = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# Add the related_name argument to avoid conflicts
User._meta.get_field('groups').remote_field.related_name = 'user_custom_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'user_custom_permissions'
