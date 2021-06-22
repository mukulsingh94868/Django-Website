# Generated by Django 3.2.4 on 2021-06-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='address',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='address2',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='password',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='state',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='zip',
        ),
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(max_length=122),
        ),
    ]