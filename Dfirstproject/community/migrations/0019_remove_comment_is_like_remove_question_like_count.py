# Generated by Django 5.0.4 on 2024-05-02 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0018_comment_is_like_question_like_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='is_like',
        ),
        migrations.RemoveField(
            model_name='question',
            name='like_count',
        ),
    ]
