# Generated by Django 4.0.3 on 2022-03-20 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_importer', '0003_alter_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
