# Generated by Django 4.0.3 on 2022-03-20 16:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('csv_importer', '0003_contact_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='last_four_card_numbers',
            field=models.CharField(default=django.utils.timezone.now, max_length=16),
            preserve_default=False,
        ),
    ]