from django.shortcuts import render

#Créer les vues ici

def accueilView(request):
    return render(request, "accueil.html")

def documentationView(request):
    return render(request, "documentation.html")

def filmsView(request):
    contexte = {'films': [
        {'nom': "Forrest Gump", 
         'date': '05/02/2023', 
         'heure': '20:00', 
         'salle': '1', 
         'categorie': 'Drame',
         'description': 'Témoin de nombreux événements marquants des années 60 et 70, un homme simple d\'esprit et au grand cœur inspire ceux qui l\'entourent à travers son optimisme constant.',
         'image': 'https://mlpnk72yciwc.i.optimole.com/cqhiHLc.IIZS~2ef73/w:auto/h:auto/q:75/https://bleedingcool.com/wp-content/uploads/2020/09/Forrest-Gump-Tom-Hanks.jpg',
         'meilleurVendeur': 'oui'},
        {'nom': "Bienvenue chez les Ch'tis", 
         'date': '06/02/2023', 
         'heure': '20:30', 
         'salle': '2', 
         'categorie': 'Comédie',
         'description': 'Témoin de nombreux événements marquants des années 60 et 70, un homme simple d\'esprit et au grand cœur inspire ceux qui l\'entourent à travers son optimisme constant.',
         'image': 'https://img.lapresse.ca/924x615/201207/17/531046.jpg',
         'meilleurVendeur': 'non'}
    ]}
    return render(request, "films.html", contexte)

def aproposView(request):
    return render(request, "apropos.html")