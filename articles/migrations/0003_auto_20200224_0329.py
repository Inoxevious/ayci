# Generated by Django 3.0.2 on 2020-02-24 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200224_0303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='commentor',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='phone',
        ),
        migrations.AddField(
            model_name='comment',
            name='commentor_email',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='commentor_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]