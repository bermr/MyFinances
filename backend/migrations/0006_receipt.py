# Generated by Django 4.2.5 on 2023-09-30 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("backend", "0005_client_active"),
    ]

    operations = [
        migrations.CreateModel(
            name="Receipt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="receipts")),
                ("total_price", models.FloatField(blank=True, null=True)),
                ("date", models.DateField(blank=True, null=True)),
                ("date_uploaded", models.DateTimeField(auto_now=True)),
                ("receipt_parsed", models.JSONField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
