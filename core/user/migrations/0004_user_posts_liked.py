# Generated by Django 4.0 on 2023-10-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_post', '0002_rename_created_at_post_created_and_more'),
        ('core_user', '0003_rename_created_at_user_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='posts_liked',
            field=models.ManyToManyField(related_name='liked_by', to='core_post.Post'),
        ),
    ]
