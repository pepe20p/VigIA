# Generated by Django 4.2.4 on 2023-09-19 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuPrincipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_menu', models.CharField(max_length=50, verbose_name='Item do menu')),
                ('ordem_menu', models.IntegerField(default=0, verbose_name='Ordem no Menu')),
                ('url', models.CharField(max_length=500, verbose_name='URL')),
            ],
            options={
                'ordering': ['ordem_menu'],
            },
        ),
    ]