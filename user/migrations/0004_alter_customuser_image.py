# Generated by Django 4.0.2 on 2022-03-20 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(null=True, upload_to='media/images/', verbose_name=''),
        ),
    ]
