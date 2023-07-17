# Generated by Django 4.2.3 on 2023-07-16 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_user_perm'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=1024)),
                ('email', models.CharField(max_length=512)),
                ('is_expire', models.BooleanField(default=False)),
                ('tries', models.SmallIntegerField(default=0)),
                ('step', models.CharField(max_length=26)),
                ('by', models.IntegerField(choices=[(1, 'By register'), (2, 'By login')])),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
