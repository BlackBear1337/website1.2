# Generated by Django 4.0.3 on 2022-04-19 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='avatar',
            field=models.ImageField(default=None, upload_to='comment', null=True),
            preserve_default=False,
        ),
    ]