# Generated by Django 5.0.4 on 2024-05-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0010_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(verbose_name='답변 내용'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.CharField(max_length=20, verbose_name='닉네임'),
        ),
    ]
