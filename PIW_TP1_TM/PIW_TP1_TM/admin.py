from django.contrib import admin
from .models import Amelioration

# Sert à enregistrer le modèle Amelioration dans l'interface d'administration de Django, ce qui permet de gérer les améliorations proposées pour le projet via l'interface d'administration.
admin.site.register(Amelioration)

