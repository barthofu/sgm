# Generated by Django 4.1.4 on 2022-12-13 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Affaire",
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
                ("raison", models.CharField(max_length=200)),
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
                ("date_rendu", models.DateField(verbose_name="date rendu")),
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
                    "montant",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("devis", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Aptitude",
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
                ("designation", models.CharField(max_length=200)),
                (
                    "taux_horaire",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Client",
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
                ("raison", models.CharField(max_length=200)),
                (
                    "type",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("adresse1", models.CharField(max_length=200)),
                (
                    "adresse2",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "adresse3",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("zip_code", models.CharField(max_length=200)),
                ("ville", models.CharField(max_length=200)),
                ("pays", models.CharField(max_length=200)),
                ("tel1", models.CharField(max_length=200)),
                (
                    "tel2",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("email", models.CharField(max_length=200)),
                ("correspondant", models.CharField(max_length=200)),
                (
                    "memo",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "compte",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Etat",
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
                ("designation", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Fournisseur",
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
                ("raison", models.CharField(max_length=200)),
                ("adresse1", models.CharField(max_length=200)),
                (
                    "adresse2",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("code_postal", models.CharField(max_length=200)),
                ("ville", models.CharField(max_length=200)),
                ("pays", models.CharField(max_length=200)),
                ("telephone", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                (
                    "correspondant",
                    models.CharField(
                        max_length=200,
                        verbose_name="Correspondant de l'entreprise",
                    ),
                ),
                (
                    "siret",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "tva",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "iban",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="iban",
                    ),
                ),
                (
                    "bic",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="bic",
                    ),
                ),
                (
                    "delais_livraison",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name="délais de livraison (jours)",
                    ),
                ),
                (
                    "memo",
                    models.TextField(blank=True, null=True, verbose_name="mémo"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Statut",
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
                ("description", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="TypeFourniture",
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
                    "code_type_fourniture",
                    models.CharField(
                        max_length=200, verbose_name="Code type fourniture"
                    ),
                ),
                (
                    "description",
                    models.TextField(verbose_name="Description du type de fourniture"),
                ),
            ],
            options={
                "db_table": "type_fourniture",
            },
        ),
        migrations.CreateModel(
            name="Salarie",
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
                ("num_secu", models.CharField(max_length=200)),
                ("civilite", models.CharField(max_length=200)),
                ("nom", models.CharField(max_length=200)),
                ("prenom", models.CharField(max_length=200)),
                ("adresse1", models.CharField(max_length=200)),
                (
                    "adresse2",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("zip_code", models.CharField(max_length=200)),
                ("ville", models.CharField(max_length=200)),
                ("pays", models.CharField(max_length=200)),
                ("tel", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("date_embauche", models.DateField()),
                ("date_depart", models.DateField(blank=True, null=True)),
                (
                    "aptitude",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.aptitude",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pointage",
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
                    "date_debut",
                    models.DateTimeField(verbose_name="Pointage debut"),
                ),
                (
                    "date_fin",
                    models.DateTimeField(verbose_name="Pointage fin"),
                ),
                (
                    "affaire",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.affaire",
                    ),
                ),
                (
                    "salarie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.salarie",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Fourniture",
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
                ("code_fourniture", models.CharField(max_length=200)),
                (
                    "description",
                    models.TextField(verbose_name="Description de la fourniture"),
                ),
                (
                    "prix_ht",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=100,
                        verbose_name="Prix HT",
                    ),
                ),
                (
                    "fournisseur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.fournisseur",
                    ),
                ),
                (
                    "type_fourniture",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.typefourniture",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Facture",
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
                    "date_envoi",
                    models.DateField(
                        blank=True, null=True, verbose_name="date d'envoi"
                    ),
                ),
                (
                    "date_echeance",
                    models.DateField(
                        blank=True, null=True, verbose_name="date d'échéance"
                    ),
                ),
                (
                    "date_paiement",
                    models.DateField(
                        blank=True, null=True, verbose_name="date de paiement"
                    ),
                ),
                (
                    "date_relance",
                    models.DateField(
                        blank=True, null=True, verbose_name="date de relance"
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
        migrations.AddField(
            model_name="affaire",
            name="charge_affaire",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.salarie",
            ),
        ),
        migrations.AddField(
            model_name="affaire",
            name="client",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.client",
            ),
        ),
        migrations.AddField(
            model_name="affaire",
            name="etat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.etat"
            ),
        ),
        migrations.AddField(
            model_name="affaire",
            name="statut",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.statut"
            ),
        ),
        migrations.CreateModel(
            name="AchatFourniture",
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
                    "quantite",
                    models.IntegerField(default=1, verbose_name="Quantité"),
                ),
                (
                    "date_demande",
                    models.DateField(
                        auto_now_add=True, verbose_name="Date de la demande"
                    ),
                ),
                (
                    "date_achat",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date d'achat"
                    ),
                ),
                (
                    "date_reception",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date de réception"
                    ),
                ),
                (
                    "affaire",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.affaire",
                    ),
                ),
                (
                    "fourniture",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.fourniture",
                    ),
                ),
            ],
            options={
                "db_table": "achat_fourniture",
            },
        ),
    ]