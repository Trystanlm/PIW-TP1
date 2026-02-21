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
         'meilleurVendeur': 'non'},
        {'nom': "Shrek 2", 
         'date': '07/02/2023', 
         'heure': '18:00', 
         'salle': '3', 
         'categorie': 'Animation',
         'description': 'Shrek et Fiona reviennent de leur lune de miel pour rencontrer les parents de celle-ci. Mais ces derniers ne s\'attendaient pas à ce que leur fille épouse un ogre.',
         'image': 'https://m.media-amazon.com/images/M/MV5BMzNmNjQ1NmUtNzhiZS00YWE2LTg4N2ItZTA2ODdmOTMwOTQ1XkEyXkFqcGc@._V1_.jpg',
         'meilleurVendeur': 'non'},
        {'nom': "Le Loup de Wall Street", 
         'date': '08/02/2023', 
         'heure': '21:00', 
         'salle': '4', 
         'categorie': 'Biographie',
         'description': 'L\'histoire vraie de Jordan Belfort, courtier en bourse à New York qui a bâti une fortune colossale grâce à la corruption et la fraude avant de tout perdre.',
         'image': 'https://m.media-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_.jpg',
         'meilleurVendeur': 'non'},
        {'nom': "Oppenheimer", 
         'date': '09/02/2023', 
         'heure': '19:30', 
         'salle': '5', 
         'categorie': 'Biographie',
         'description': 'L\'histoire de J. Robert Oppenheimer, physicien théoricien qui a dirigé le développement de la première bombe atomique dans le cadre du projet Manhattan pendant la Seconde Guerre mondiale.',
         'image': 'https://upload.wikimedia.org/wikipedia/en/4/4a/Oppenheimer_%28film%29.jpg',
         'meilleurVendeur': 'non'},
        {'nom': "Lendemain de veille", 
         'date': '10/02/2023', 
         'heure': '22:00', 
         'salle': '6', 
         'categorie': 'Comédie',
         'description': 'Trois amis se réveillent à Las Vegas après une soirée d\'enterrement de vie de garçon complètement hors de contrôle, sans aucun souvenir de la veille et avec un tigre dans leur suite.',
         'image': 'https://m.media-amazon.com/images/M/MV5BYmIyODg0N2EtYjg5NC00NjdlLWFkZTgtMmE0NzI4ZGM5ODk1XkEyXkFqcGc@._V1_.jpg',
         'meilleurVendeur': 'non'}
    ]}
    return render(request, "films.html", contexte)

def aproposView(request):
    return render(request, "apropos.html")