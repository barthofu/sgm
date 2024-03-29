from django.db import models
from constance import config


class Fiche(models.Model):
    affaire = models.ForeignKey(
        "Affaire",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="fiches",
    )
    titre = models.CharField(max_length=100, null=False, blank=False, default="")
    description = models.TextField(null=True, blank=True)
    observation = models.CharField(max_length=1000, null=True, blank=True)
    ref_doc = models.CharField(max_length=200, null=True, blank=True)

    terminee = models.BooleanField(
        "Fiche terminée", default=False, null=False, blank=False
    )
    fourniture = models.BooleanField(
        "Fournitures arrivées", default=False, null=False, blank=False
    )

    date_creation = models.DateField("date de création", auto_now_add=True)
    date_modification = models.DateTimeField("date de modification", auto_now=True)
    date_cloture = models.DateField("date de clôture", null=True, blank=True)

    def __str__(self):
        return f"Fiche : {self.description}"

    def cout_fiche(self) -> float:
        """
        Coût de la fiche
        :return: float
        """
        return sum([e.cout_etape() for e in self.etapes.all()])

    def avancement_fiche(self):
        """
        % des etape terminées = avancement de la fiche
        :return: float
        """
        total = self.etapes.count()
        nb_etapes_terminees: int = self.etapes.filter(terminee=True).count()
        if total > 0:
            return round((100 * nb_etapes_terminees) / total, 0)
        else:
            return 0

    def temps_ajustage(self):
        """
        Temps total d'ajustage de la fiche
        :return: int
        """
        return sum(
            [
                e.temps * e.quantite
                for e in self.etapes.all().filter(
                    groupe_machine=config.GROUPE_MACHINE_AJUSTAGE_ID
                )
            ]
        )

    def temps_machine(self):
        """
        Temps total machine de la fiche
        :return: int
        """
        return sum(
            [
                e.temps * e.quantite
                for e in self.etapes.all().exclude(
                    groupe_machine=config.GROUPE_MACHINE_AJUSTAGE_ID
                )
            ]
        )

    def temps_restant(self):
        """
        Temps restant de la fiche
        :return: int
        """
        return sum(
            [e.temps * e.quantite for e in self.etapes.all().filter(terminee=False)]
        )
