# Generated by Django 5.0.6 on 2024-10-05 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_total_copies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='total_copies',
        ),
    ]
