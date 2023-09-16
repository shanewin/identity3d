# Generated by Django 4.2.1 on 2023-07-27 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0011_alter_nft_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nft",
            name="image",
            field=models.ImageField(blank=True, upload_to="nft_images/"),
        ),
        migrations.AlterField(
            model_name="nft",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
