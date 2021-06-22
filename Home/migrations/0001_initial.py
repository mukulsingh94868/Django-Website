# Generated by Django 3.2.4 on 2021-06-21 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
                ('address2', models.CharField(max_length=122)),
                ('city', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=12)),
                ('zip', models.CharField(max_length=8)),
            ],
        ),
    ]