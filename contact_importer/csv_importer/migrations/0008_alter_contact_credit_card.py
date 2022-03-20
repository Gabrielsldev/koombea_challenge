# Generated by Django 4.0.3 on 2022-03-20 19:19

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('csv_importer', '0007_alter_contact_franchise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='credit_card',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=20, null=True)),
        ),
    ]