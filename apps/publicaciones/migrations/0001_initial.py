# Generated by Django 5.1.5 on 2025-02-05 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("vehiculos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Publicacion",
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
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "moneda",
                    models.CharField(
                        choices=[("Pesos", "Pesos"), ("Dólares", "Dólares")],
                        max_length=10,
                    ),
                ),
                (
                    "plataforma",
                    models.CharField(
                        choices=[
                            ("MercadoLibre", "MercadoLibre"),
                            ("Facebook", "Facebook"),
                            ("Instagram", "Instagram"),
                            ("WhatsApp", "WhatsApp"),
                            ("Otro", "Otro"),
                        ],
                        max_length=50,
                    ),
                ),
                ("fecha_publicacion", models.DateField(auto_now_add=True)),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("Activa", "Activa"),
                            ("Vendida", "Vendida"),
                            ("Inactiva", "Inactiva"),
                        ],
                        default="Activa",
                        max_length=20,
                    ),
                ),
                (
                    "vehiculo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vehiculos.vehiculo",
                    ),
                ),
            ],
        ),
    ]
