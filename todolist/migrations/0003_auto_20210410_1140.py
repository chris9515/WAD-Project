# Generated by Django 3.1.5 on 2021-04-10 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todolist_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='text',
            field=models.CharField(max_length=100),
        ),
    ]
