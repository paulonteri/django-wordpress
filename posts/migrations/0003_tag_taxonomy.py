# Generated by Django 3.0.7 on 2021-03-23 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210324_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='taxonomy',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]