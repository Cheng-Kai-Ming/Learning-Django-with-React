# Generated by Django 4.0 on 2023-12-25 14:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core_post', '0004_post_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveIndex(
            model_name='post',
            name='core_post_p_publish_4e0589_idx',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='post',
            name='publish',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='post',
            name='public_id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]