# Generated by Django 4.2.2 on 2023-07-22 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailverification', '0001_initial'),
        ('notebook', '0002_share_notebook'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='notebook',
            unique_together={('book_name', 'user')},
        ),
    ]
