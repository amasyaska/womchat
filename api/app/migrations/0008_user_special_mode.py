# Generated by Django 5.0.4 on 2024-04-29 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_chat_chat_type_alter_usertochat_chat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='special_mode',
            field=models.BooleanField(default=False),
        ),
    ]
