# Generated by Django 4.2.2 on 2023-07-13 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_profile_bio_profile_company_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="company_logo",
            field=models.ImageField(
                default="default_co.jpg", upload_to="company_logos"
            ),
        ),
    ]