# Generated by Django 3.0.2 on 2020-02-26 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_accountuser_writer'),
        ('articles', '0005_auto_20200224_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.AccountUser'),
        ),
    ]
