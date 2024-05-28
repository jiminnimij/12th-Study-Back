# Generated by Django 5.0.5 on 2024-05-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('upload_time', models.DateTimeField(unique=True)),
                ('content', models.TextField(verbose_name='내용')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='사진')),
                ('category', models.CharField(choices=[('교육, 학문', '교육, 학문'), ('컴퓨터통신', '컴퓨터통신'), ('게임', '게임'), ('엔터테인먼트, 예술', '엔터테인먼트, 예술'), ('생활', '생활'), ('건강', '건강'), ('사회, 정치', '사회, 정치'), ('경제', '경제'), ('여행', '여행'), ('스포츠, 레저', '스포츠, 레저'), ('쇼핑', '쇼핑'), ('지역&플레이스', '지역&플레이스'), ('고민Q&A', '고민Q&A')], default='uncategorized', max_length=20, verbose_name='분야')),
            ],
        ),
    ]
