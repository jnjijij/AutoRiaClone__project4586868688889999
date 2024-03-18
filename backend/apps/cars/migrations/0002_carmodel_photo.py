import core.services.file_service
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='photo',
            field=models.ImageField(blank=True, upload_to=core.services.file_service.FileService.upload_car_photo),
        ),
    ]
