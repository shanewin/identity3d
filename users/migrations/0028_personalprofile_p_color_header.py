# Generated by Django 4.2.1 on 2023-08-22 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0027_alter_personalprofile_office"),
    ]

    operations = [
        migrations.AddField(
            model_name="personalprofile",
            name="p_color_header",
            field=models.CharField(default="#000000", max_length=7),
        ),
    ]
