# Generated by Django 4.2.6 on 2023-10-17 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("available_stock", models.PositiveIntegerField()),
            ],
            options={
                "verbose_name": "products",
                "verbose_name_plural": "products",
                "db_table": "product",
            },
        ),
    ]
