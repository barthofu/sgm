# Generated by Django 4.1.4 on 2023-01-30 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_groupemachine_machine"),
    ]

    operations = [
        migrations.CreateModel(
            name="Zone",
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
                ("nom", models.CharField(max_length=200)),
                ("description", models.TextField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name="etape",
            name="observation",
        ),
        migrations.AddField(
            model_name="etape",
            name="machine",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.machine",
            ),
        ),
        migrations.AddField(
            model_name="etape",
            name="matiere",
            field=models.CharField(
                blank=True, max_length=2000, null=True, verbose_name="Matière"
            ),
        ),
        migrations.AddField(
            model_name="etape",
            name="nom_piece",
            field=models.CharField(
                blank=True, max_length=2000, null=True, verbose_name="Nom de la pièce"
            ),
        ),
        migrations.AddField(
            model_name="etape",
            name="quantite",
            field=models.IntegerField(default=0, verbose_name="Quantité"),
        ),
        migrations.AddField(
            model_name="etape",
            name="temps",
            field=models.IntegerField(default=0, verbose_name="Temps nécessaire"),
        ),
        migrations.AddField(
            model_name="etape",
            name="terminee",
            field=models.BooleanField(default=False, verbose_name="Terminée ?"),
        ),
        migrations.AddField(
            model_name="fiche",
            name="fourniture",
            field=models.BooleanField(
                default=False, verbose_name="Fournitures arrivées"
            ),
        ),
        migrations.AddField(
            model_name="fiche",
            name="terminee",
            field=models.BooleanField(default=False, verbose_name="Fiche terminée"),
        ),
        migrations.AlterField(
            model_name="etape",
            name="description",
            field=models.TextField(
                blank=True, max_length=10000, null=True, verbose_name="Description"
            ),
        ),
        migrations.AlterField(
            model_name="etape",
            name="num_etape",
            field=models.IntegerField(verbose_name="N°Étape"),
        ),
        migrations.AlterField(
            model_name="etape",
            name="ref_doc",
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="salarie",
            name="aptitude",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.ProtectedError,
                to="api.aptitude",
            ),
        ),
        migrations.AddField(
            model_name="salarie",
            name="zone",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.ProtectedError,
                to="api.zone",
            ),
        ),
    ]
