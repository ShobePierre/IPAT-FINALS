# Generated by Django 5.0.4 on 2024-07-07 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_graduates_item_citizenship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Baranggay',
            new_name='Barangga',
        ),
    ]
