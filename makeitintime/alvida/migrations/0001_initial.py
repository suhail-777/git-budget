# Generated by Django 2.1.5 on 2019-03-13 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateField(auto_now_add=True)),
                ('duration', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
