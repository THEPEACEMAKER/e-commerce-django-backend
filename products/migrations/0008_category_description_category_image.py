# Generated by Django 4.2 on 2023-05-10 23:32

import cloudinary.models
import django.core.validators
from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='default.jpg', max_length=255, null=True, validators=[products.models.validate_image_size, products.models.validate_image_extension], verbose_name='images'),
        ),
    ]