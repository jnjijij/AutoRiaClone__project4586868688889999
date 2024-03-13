from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from models import User

class Permissions:
    @staticmethod
    def add_custom_permissions():
        content_type = ContentType.objects.get_for_model(User)
        Permission.objects.create(content_type=content_type, codename='view_statistics', name='Can view listing '
                                                                                              'statistics')
