# Generated by Django 3.1.2 on 2021-04-01 07:42

import json

from django.db import migrations

import djstripe.fields


def populate_new_metadata(apps, schema_editor):
    Invoice = apps.get_model("djstripe", "Invoice")

    for invoice in Invoice.objects.all():
        if invoice.metadata:
            invoice.new_metadata = json.loads(invoice.metadata)
            invoice.save()


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0020_add_index_on_invoice_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="new_metadata",
            field=djstripe.fields.JSONField(
                blank=True,
                help_text="A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.",
                null=True,
            ),
        ),
        migrations.RunPython(populate_new_metadata),
    ]