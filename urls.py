from django.conf.urls import patterns, url
from crete_gis.e_road_b.views import datastore

urlpatterns = patterns(
        'crete_gis.e_road_b',
        url(r'^results/', datastore, name = 'datastore'),
        )
