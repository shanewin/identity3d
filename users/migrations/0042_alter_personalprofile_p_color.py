# Generated by Django 4.2.1 on 2023-09-14 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0041_alter_personalprofile_p_color"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personalprofile",
            name="p_color",
            field=models.CharField(default="#f8f9fa", max_length=255),
        ),
    ]
