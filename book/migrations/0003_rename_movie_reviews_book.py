# Generated by Django 5.1.1 on 2024-11-06 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0002_reviews"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reviews",
            old_name="movie",
            new_name="book",
        ),
    ]