# Generated by Django 3.2.9 on 2021-12-07 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='surname',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
