# Generated by Django 4.2 on 2023-04-30 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='confirm_password',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
