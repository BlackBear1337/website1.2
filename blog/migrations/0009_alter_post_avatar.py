# Generated by Django 4.0.3 on 2022-04-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_comment_avatar_post_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='avatar',
            field=models.ImageField(upload_to='comment', default=None, null=True),
        ),
    ]
