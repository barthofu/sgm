# Generated by Django 4.1.6 on 2023-03-23 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0019_remove_etape_matiere_etape_plan_etape_rep"),
    ]

    operations = [
        migrations.AlterField(
            model_name="affaire",
            name="montant",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
