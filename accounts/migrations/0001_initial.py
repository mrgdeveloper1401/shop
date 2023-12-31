# Generated by Django 4.2.6 on 2023-10-12 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('mobile_phone', models.CharField(max_length=15, unique=True, verbose_name='Mobile Phone')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6, verbose_name='Gender')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Superuser')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Otpcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('code', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create code')),
            ],
        ),
        migrations.CreateModel(
            name='UserWalletModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Balance')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user wallet',
                'verbose_name_plural': 'user wallets',
                'db_table': 'user_wallet',
            },
        ),
        migrations.CreateModel(
            name='UserMoreInformationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(help_text='enter province name', max_length=100, verbose_name='Province')),
                ('thonship', models.CharField(help_text='enter thonship name', max_length=100, verbose_name='Thonship')),
                ('city', models.CharField(help_text='enter city name', max_length=100, verbose_name='City')),
                ('address', models.CharField(help_text='enter address', max_length=100, verbose_name='Address')),
                ('postal_code', models.CharField(max_length=10, verbose_name='Postal Code')),
                ('birth_day', models.DateField(blank=True, null=True, verbose_name='Birthday')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='update at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user more information',
                'verbose_name_plural': 'user more information',
                'db_table': 'user_more_information',
            },
        ),
    ]
