# Generated by Django 4.1.6 on 2023-03-04 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_category_subscribers_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='category',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='user',
        ),
    ]