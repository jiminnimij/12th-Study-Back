# Generated by Django 5.0.4 on 2024-05-01 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0013_alter_question_upload_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Question',
            new_name='question',
        ),
    ]
