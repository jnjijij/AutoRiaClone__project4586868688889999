from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(["manage.py", "runserver", "--noreload"])