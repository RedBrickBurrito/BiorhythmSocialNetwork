# Generated by Django 4.0.2 on 2022-03-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
    ]