import json

from django.core.management.base import BaseCommand

from installations.models import Installation


class Command(BaseCommand):
    help = "Load installations from a GeoJSON file"

    def add_arguments(self, parser):
        parser.add_argument("geojson_file", type=str)

    def handle(self, *args, **kwargs):
        geojson_file = kwargs["geojson_file"]
        with open(geojson_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        for feature in data["features"]:
            props = feature["properties"]
            coords = feature["geometry"]["coordinates"]
            Installation.objects.update_or_create(
                gid=props["gid"],
                defaults={
                    "gml_id": props.get("gml_id", ""),
                    "codeaiot": props.get("codeaiot", ""),
                    "raisonsociale": props.get("raisonsociale", ""),
                    "adresse1": props.get("adresse1", ""),
                    "codepostal": props.get("codepostal", ""),
                    "codeinsee": props.get("codeinsee", ""),
                    "commune": props.get("commune", ""),
                    "statutseveso": props.get("statutseveso"),
                    "etatactivite": props.get("etatactivite"),
                    "regimevigueur": props.get("regimevigueur", ""),
                    "serviceaiot": props.get("serviceaiot", ""),
                    "siret": props.get("siret"),
                    "geo_point_lat": coords[1],
                    "geo_point_lon": coords[0],
                    "bovins": props.get("bovins") == "true",
                    "porcs": props.get("porcs") == "true",
                    "volailles": props.get("volailles") == "true",
                    "carriere": props.get("carriere") == "true",
                    "eolienne": props.get("eolienne") == "true",
                    "industrie": props.get("industrie") == "true",
                    "prioritenationale": props.get("prioritenationale") == "true",
                    "ied": props.get("ied") == "true",
                    "departement": props.get("departement", ""),
                },
            )
        self.stdout.write(self.style.SUCCESS("Installations loaded successfully."))
