# Generated by Django 4.1 on 2023-03-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_database_delete_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='c_moviename',
            field=models.ManyToManyField(to='user.movie'),
        ),
    ]
