# Generated by Django 2.2.4 on 2023-11-23 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_auto_20231123_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]