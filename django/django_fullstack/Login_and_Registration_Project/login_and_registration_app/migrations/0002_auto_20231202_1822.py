# Generated by Django 2.2.4 on 2023-12-02 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_and_registration_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='passowrd',
            new_name='password',
        ),
    ]
