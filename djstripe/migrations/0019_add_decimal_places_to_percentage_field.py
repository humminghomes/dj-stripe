# Generated by Django 3.1.2 on 2020-10-05 08:40

import django.core.validators
from django.db import migrations
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0018_customer_default_balance_delinquent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxrate',
            name='percentage',
            field=djstripe.fields.StripePercentField(decimal_places=3, help_text='This represents the tax rate percent out of 100.', max_digits=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
