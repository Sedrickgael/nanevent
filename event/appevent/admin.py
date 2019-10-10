# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CompagnieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom_compagnie',
        'addresse',
        'email',
        'contact',
        'password',
        'statut',
        'date_udapte',
        'dat_add',
    )
    list_filter = ('statut', 'date_udapte', 'dat_add')


class CommuneAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'statut', 'date_udapte', 'dat_add')
    list_filter = ('statut', 'date_udapte', 'dat_add')


class EventsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom_event',
        'date_debut',
        'date_fin',
        'id_commune',
        'compagnie_id',
        'id_categorie',
        'description',
        'lieu',
        'date_udapte',
        'dat_add',
        'statut',
    )
    list_filter = (
        'date_debut',
        'date_fin',
        'date_udapte',
        'dat_add',
        'statut',
    )
    raw_id_fields = ('id_commune', 'compagnie_id', 'id_categorie')


class Image_eventAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'image_url',
        'event',
        'date_udapte',
        'dat_add',
        'statut',
    )
    list_filter = (
        'date_udapte',
        'dat_add',
        'statut',
        'id',
        'image_url',
        'event',
        'date_udapte',
        'dat_add',
        'statut',
    )
    raw_id_fields = ('event',)


class UtilisateursAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'id_commune',
        'contacts',
        'date_udapte',
        'dat_add',
        'statut',
    )
    list_filter = (
        'user',
        'date_udapte',
        'dat_add',
        'statut',
        'id',
        'user',
        'id_commune',
        'contacts',
        'date_udapte',
        'dat_add',
        'statut',
    )
    raw_id_fields = ('id_commune',)


class Categorie_eventAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'date_udapte', 'dat_add', 'statut')
    list_filter = ('date_udapte', 'dat_add', 'statut')


class ParticipantsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'id_user',
        'id_event',
        'date_udapte',
        'dat_add',
        'statut',
    )
    list_filter = (
        'id_user',
        'date_udapte',
        'dat_add',
        'statut',
        'id',
        'id_user',
        'id_event',
        'date_udapte',
        'dat_add',
        'statut',
    )
    raw_id_fields = ('id_event',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Compagnie, CompagnieAdmin)
_register(models.Commune, CommuneAdmin)
_register(models.Events, EventsAdmin)
_register(models.Image_event, Image_eventAdmin)
_register(models.Utilisateurs, UtilisateursAdmin)
_register(models.Categorie_event, Categorie_eventAdmin)
_register(models.Participants, ParticipantsAdmin)
