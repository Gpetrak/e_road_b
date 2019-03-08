from django.contrib.gis import admin
from crete_gis.e_road_b.models import Event


admin.site.register(Event, admin.OSMGeoAdmin)
