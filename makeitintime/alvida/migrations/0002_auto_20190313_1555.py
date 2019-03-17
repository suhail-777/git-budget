# Generated by Django 2.1.5 on 2019-03-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alvida', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='permutations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.IntegerField()),
                ('team2', models.IntegerField()),
                ('winner_no', models.IntegerField()),
                ('isallowed', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='month',
        ),
        migrations.AddField(
            model_name='schedule',
            name='no_of_teams',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schedule',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
