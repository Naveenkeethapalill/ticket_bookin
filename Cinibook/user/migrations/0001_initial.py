# Generated by Django 4.1 on 2023-03-09 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('name', models.CharField(max_length=50)),
                ('disc', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_count', models.TextField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=2)),
                ('c_date', models.DateField()),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
