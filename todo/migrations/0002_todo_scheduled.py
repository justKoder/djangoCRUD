# Generated by Django 3.2.5 on 2021-12-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='scheduled',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
