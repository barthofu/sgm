# Generated by Django 4.1.6 on 2023-10-14 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_alter_etapemodele_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="etape",
            name="quantite",
            field=models.IntegerField(default=1, verbose_name="Quantité"),
        ),
        migrations.AlterField(
            model_name="etapemodele",
            name="quantite",
            field=models.IntegerField(default=1, verbose_name="Quantité"),
        ),
    ]