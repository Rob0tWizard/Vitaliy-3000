# Generated by Django 5.0 on 2023-12-26 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_remove_customuser_user_name_alter_customuser_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
