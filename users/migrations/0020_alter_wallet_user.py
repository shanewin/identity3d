# Generated by Django 4.2.1 on 2023-08-03 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0019_alter_wallet_private_key_alter_wallet_wallet_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wallet",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wallet",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
