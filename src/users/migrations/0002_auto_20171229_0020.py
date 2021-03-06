# Generated by Django 2.0 on 2017-12-29 00:20

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.crypto
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoKeypair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('type', models.PositiveSmallIntegerField(default=1, verbose_name=[(0, 'None'), (1, 'IPDB')])),
                ('private_key', models.TextField(blank=True, null=True)),
                ('public_key', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LanguageName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=255)),
                ('enabled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Language name',
                'verbose_name_plural': 'Language names',
            },
        ),
        migrations.CreateModel(
            name='MemberOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('identifiers', models.TextField()),
                ('domains', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=80), blank=True, size=None)),
            ],
            options={
                'verbose_name': 'Member organization',
                'verbose_name_plural': 'Member organizations',
            },
        ),
        migrations.CreateModel(
            name='OneTimePassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('one_time_password', models.CharField(default=django.utils.crypto.get_random_string, max_length=64)),
                ('is_used', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('login_attempts', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='onetimepassword',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cryptokeypair',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
