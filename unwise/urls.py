from django.urls import path, re_path #include, url

import coadd.views as co
import sdssphot.views as phot

tilepattern = r'[0-9]{4}[pm][0-9]{3}'

urlpatterns = [
    # These are redirects for Aaron
    re_path(r'^neo4/?$', co.fulldepth_neo4),
    re_path(r'^tr_neo3/?$', co.tr_neo3),
    re_path(r'^fulldepth_neo3/?$', co.fulldepth_neo3),
    re_path(r'^tr_neo2/?$', co.tr_neo2),

    re_path(r'^tiles/$', co.TileList.as_view()),
    re_path(r'^tiles_near/$', co.CoordSearchTileList.as_view()),

    # Add new dataset names here!
    re_path(r'^tiledata/(?P<version>(neo7|neo6|neo5|neo4|neo3|neo2|neo1|allwise))/(?P<coadd>' + tilepattern +
        ')-w(?P<bands>1?2?3?4?).tgz/?$',
        co.tile_tgz, name='tile-tgz'),

    re_path(r'^tiledata/(?P<version>(neo4|neo3|neo2|neo1|allwise))/(?P<coadd>' + tilepattern + ').tgz/?$',
        co.tile_tgz, name='tile-tgz'),
    re_path(r'^tilesetdata/?$', co.tileset_tgz, name='tileset-tgz'),
    re_path(r'^imgsearch/?$', co.coord_search, name='search'),
    re_path(r'^search/?$', co.coord_search, name='search'),
    re_path(r'^cutout_fits/?$', co.cutout_fits, name='cutout_fits'),
    re_path(r'^cutout_jpg/?$', co.cutout_jpg, name='cutout_jpg'),
    # re_path(r'^usage/?$', usage),
    re_path(r'^$', co.index, name='index'),
]

urlpatterns += [
  re_path(r'^photsearch/?$', phot.coord_search, name='phot-search'),
  re_path(r'^phot_near/?$', phot.conesearch_results),
  re_path(r'^phot_box/?$', phot.boxsearch_results),
  re_path(r'^phot_fieldset/?$', phot.phot_fieldset_tgz, name='phot-fieldset-tgz'),
  re_path(r'^phot_tileset/?$', phot.phot_tileset_tgz, name='phot-tileset-tgz'),
  re_path(r'^fits_sdss_fields_near/?$', phot.fields_near_fits, name='fits_sdss_fields_near'),
  re_path(r'^fits_sdss_fields_box/?$', phot.fields_box_fits, name='fits_sdss_fields_box'),
]

#urlpatterns += patterns('animate',
#  url(r'^gif/?$', 'animate'))

### DEBUG
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# urlpatterns += staticfiles_urlpatterns()
# 
# from django.conf import settings
# urlpatterns += [
#     '',
#     #url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#     #    {'document_root': settings.MEDIA_ROOT}),
#     url(r'^data/(?P<path>.*)$', django.views.static.serve,
#         {'document_root': settings.DATA_DIR, 'show_indexes': True}),
#     url(r'^data-sdssphot/(?P<path>.*)$', django.views.static.serve,
#         {'document_root': settings.SDSSPHOT_DATA_DIR, 'show_indexes': True}),
# ]
