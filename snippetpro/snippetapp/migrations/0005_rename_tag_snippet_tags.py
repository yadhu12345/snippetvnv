# Generated by Django 4.2.1 on 2023-05-09 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippetapp', '0004_alter_snippet_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='tag',
            new_name='tags',
        ),
    ]
