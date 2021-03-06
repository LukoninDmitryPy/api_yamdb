# Generated by Django 3.0 on 2022-03-02 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220228_1705'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='XXXX', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('user', 'Пользователь'), ('moderator', 'Модератор'), ('admin', 'Администратор')], default='user', max_length=20),
        ),
    ]
