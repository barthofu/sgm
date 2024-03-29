from django.db import models


class FicheModele(models.Model):
    # modele infos
    date_creation = models.DateField("date de création", auto_now_add=True)

    # fiche infos
    titre = models.CharField(max_length=100, null=False, blank=False, default="")
    description = models.TextField(null=True, blank=True)

    fourniture = models.BooleanField(
        "Fournitures arrivées", default=False, null=False, blank=False
    )

    def cout_fiche(self) -> float:
        """
        Coût de la fiche
        :return: float
        """
        return sum([e.cout_etape() for e in self.etapes_modele.all()])

    class Meta:
        verbose_name = "Fiche modèle"
        verbose_name_plural = "Fiches modèle"

    def __str__(self):
        return f"Fiche : {self.description}"
