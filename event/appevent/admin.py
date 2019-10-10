from django.contrib import admin

# Register your models here.
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
    list_filter = (
        'statut',
        'date_udapte',
        'dat_add',
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


class CommuneAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'statut', 'date_udapte', 'dat_add')
    list_filter = (
        'statut',
        'date_udapte',
        'dat_add',
        'id',
        'nom',
        'statut',
        'date_udapte',
        'dat_add',
    )


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
        'id_commune',
        'compagnie_id',
        'id_categorie',
        'date_udapte',
        'dat_add',
        'statut',
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


class UsersAdmin(admin.ModelAdmin):

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
        'id_commune',
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


class Categorie_eventAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'date_udapte', 'dat_add', 'statut')
    list_filter = (
        'date_udapte',
        'dat_add',
        'statut',
        'id',
        'nom',
        'date_udapte',
        'dat_add',
        'statut',
    )


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
        'id_event',
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


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Compagnie, CompagnieAdmin)
_register(models.Commune, CommuneAdmin)
_register(models.Events, EventsAdmin)
_register(models.Users, UsersAdmin)
_register(models.Categorie_event, Categorie_eventAdmin)
_register(models.Participants, ParticipantsAdmin)
