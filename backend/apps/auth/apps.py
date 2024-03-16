import os
from pathlib import Path

apps_directory = Path('path/to/apps')
auth_directory = apps_directory / 'auth'

files_to_create = [
    auth_directory / 'apps.py',
    auth_directory / 'models.py',
    auth_directory / 'serializers.py',
    auth_directory / 'urls.py',
    auth_directory / 'views.py'
]

for file_path in files_to_create:
    if not file_path.exists():
        file_path.touch()

# Content of apps.py
with open(auth_directory / 'apps.py', 'w') as apps_file:
    apps_file.write('from django.apps import AppConfig\n\n')
    apps_file.write('class AuthConfig(AppConfig):\n')
    apps_file.write('    default_auto_field = \'django.db.models.BigAutoField\'\n')
    apps_file.write('    name = \'apps.auth\'\n')