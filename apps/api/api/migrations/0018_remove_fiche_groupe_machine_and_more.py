# Generated by Django 4.1.6 on 2023-03-11 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0017_remove_affaire_devis"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fiche",
            name="groupe_machine",
        ),
        migrations.RemoveField(
            model_name="machine",
            name="groupe_machine",
        ),
        migrations.DeleteModel(
            name="GroupeMachine",
        ),
    ]
