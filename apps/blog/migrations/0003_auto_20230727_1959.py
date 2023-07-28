# Generated by Django 3.2.16 on 2023-07-27 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230727_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='blog',
        ),
        migrations.AddField(
            model_name='comments',
            name='blog_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.blog'),
        ),
    ]
