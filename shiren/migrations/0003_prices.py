# Generated by Django 4.0.3 on 2022-04-15 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shiren', '0002_rename_sword_swords_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
