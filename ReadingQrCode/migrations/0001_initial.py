# Generated by Django 2.2.5 on 2019-10-23 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('number_phone', models.CharField(max_length=11)),
                ('e_mail', models.CharField(max_length=80)),
                ('company', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('web_site', models.CharField(max_length=50)),
            ],
        ),
    ]
