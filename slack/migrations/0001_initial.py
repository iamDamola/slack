# Generated by Django 4.0.4 on 2022-10-31 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slackdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('backend', models.BooleanField()),
                ('age', models.IntegerField()),
                ('bio', models.CharField(max_length=255)),
            ],
        ),
    ]
