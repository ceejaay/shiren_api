# Generated by Django 4.0.3 on 2022-04-02 15:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
