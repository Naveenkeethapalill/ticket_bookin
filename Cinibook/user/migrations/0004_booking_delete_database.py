# Generated by Django 4.1 on 2023-03-10 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_database_c_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_count', models.TextField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=2)),
                ('b_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Database',
        ),
    ]
