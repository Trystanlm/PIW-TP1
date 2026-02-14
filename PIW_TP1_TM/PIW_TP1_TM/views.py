from django.shortcuts import render

#Créer les vues ici

def accueilView(request):
    return render(request, "accueil.html")

def documentationView(request):
    return render(request, "documentation.html")

def filmsView(request):
    return render(request, "films.html")

def aproposView(request):
    return render(request, "apropos.html")