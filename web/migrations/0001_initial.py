# Generated by Django 5.0.6 on 2024-07-04 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=10000000, verbose_name='姓名')),
                ('subject', models.CharField(max_length=10000000, verbose_name='主題')),
                ('content', models.TextField(verbose_name='內容')),
                ('cterted', models.DateTimeField(auto_now_add=True, verbose_name='留言時間')),
            ],
        ),
    ]
