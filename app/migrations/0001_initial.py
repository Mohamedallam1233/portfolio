# Generated by Django 4.0 on 2021-12-16 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('photo', models.ImageField(upload_to='my_works/')),
                ('description', models.TextField()),
                ('link', models.URLField()),
            ],
        ),
    ]
