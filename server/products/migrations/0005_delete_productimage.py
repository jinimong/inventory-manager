# Generated by Django 3.1.7 on 2021-03-24 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_auto_20210322_0756"),
    ]

    operations = [
        migrations.DeleteModel(name="ProductImage",),
    ]
