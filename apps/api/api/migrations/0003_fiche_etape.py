# Generated by Django 4.1.4 on 2023-01-25 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_affaire_date_rendu_alter_affaire_etat_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fiche",
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
                (
                    "description",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "observation",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "ref_doc",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "date_creation",
                    models.DateField(
                        auto_now_add=True, verbose_name="date de création"
                    ),
                ),
                (
                    "date_modification",
                    models.DateTimeField(
                        auto_now=True, verbose_name="date de modification"
                    ),
                ),
                (
                    "date_cloture",
                    models.DateField(
                        blank=True, null=True, verbose_name="date de clôture"
                    ),
                ),
                (
                    "affaire",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.affaire",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Etape",
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
                ("num_etape", models.IntegerField()),
                (
                    "description",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "observation",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "ref_doc",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "date_creation",
                    models.DateField(
                        auto_now_add=True, verbose_name="date de création"
                    ),
                ),
                (
                    "date_modification",
                    models.DateTimeField(
                        auto_now=True, verbose_name="date de modification"
                    ),
                ),
                (
                    "date_cloture",
                    models.DateField(
                        blank=True, null=True, verbose_name="date de clôture"
                    ),
                ),
                (
                    "fiche",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.fiche",
                    ),
                ),
            ],
        ),
    ]
