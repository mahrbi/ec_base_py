# Generated by Django 3.2.9 on 2021-11-29 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20211123_1639'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name'], 'permissions': [('view_history', 'Can View History')]},
        ),
    ]
