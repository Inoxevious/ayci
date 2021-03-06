# Generated by Django 3.0.2 on 2020-02-24 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('official_language', models.TextField()),
                ('flag', models.ImageField(upload_to='static/images/countries/flags')),
                ('longi', models.TextField(blank=True)),
                ('lat', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('user_group', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AccountUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=70, null=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('country', models.CharField(blank=True, max_length=70, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('date_birth', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=70, null=True)),
                ('email', models.CharField(blank=True, max_length=70, null=True)),
                ('id_number', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20, null=True)),
                ('education_level', models.CharField(blank=True, choices=[('Graduate', 'Graduated'), ('Not_Graduate', 'Not_Graduate')], max_length=70, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, null=True)),
                ('number_dependants', models.IntegerField(blank=True, null=True)),
                ('total_worth', models.IntegerField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='staticfiles/images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
