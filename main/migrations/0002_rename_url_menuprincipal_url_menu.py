# Generated by Django 4.2.4 on 2023-09-19 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuprincipal',
            old_name='url',
            new_name='url_menu',
        ),
    ]