from rest_framework import serializers
from api.zone.models import Zone
from api.fiche.models import Fiche
from api.etape.models import Etape
from api.affaire.models import Affaire
from api.fiche.serializer import FicheDetailSerializer
from api.affaire.serializer import AffaireFichesEtapesSerializer
from django.db.models import Prefetch, Count
from datetime import datetime, timedelta
from drf_spectacular.utils import extend_schema_field


class ListZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ["id", "nom", "description"]


class ZoneSerializer(serializers.ModelSerializer):
    # permet de serializer plusieurs fiches
    fiches = FicheDetailSerializer(
        many=True,
    )

    class Meta:
        model = Zone
        fields = "__all__"


def week_to_date_range(week) -> (datetime, datetime):
    year = datetime.now().year
    start = datetime.strptime(f"{year}-W{week}-{1}", "%Y-W%U-%w")
    end = start + timedelta(weeks=1) - timedelta(days=1)

    return start, end
