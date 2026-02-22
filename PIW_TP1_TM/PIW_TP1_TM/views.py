from django.shortcuts import render
# Importer le modèle Amelioration pour pouvoir l'utiliser dans la vue documentationView
from .models import Amelioration

#Créer les vues ici

def accueilView(request):
    return render(request, "accueil.html")

def documentationView(request):
    # Sert à afficher les améliorations proposées pour le projet. Récupère toutes les améliorations de la base de données et les passe au template documentation.html pour les afficher.
    ameliorations = Amelioration.objects.all()
    return render(request, "documentation.html", {'ameliorations': ameliorations})


# Sert à afficher les films disponibles dans la salle de cinéma.
def filmsView(request):
    contexte = {'films': [
        {'nom': "Forrest Gump", 
         'date': '05/02/2023', 
         'heure': '20:00', 
         'salle': '1', 
         'categorie': 'Drame',
         'description': 'Témoin de nombreux événements marquants des années 60 et 70, un homme simple d\'esprit et au grand cœur inspire ceux qui l\'entourent à travers son optimisme constant.',
         'image': 'https://i.ebayimg.com/images/g/y9gAAOSwUQhi-9Nq/s-l1200.jpg',
         'meilleurVendeur': 'oui',
         'bandeAnnonce': 'https://youtu.be/7pDDuroFBGM'},
        
        {'nom': "Bienvenue chez les Ch'tis", 
         'date': '06/02/2023', 
         'heure': '20:30', 
         'salle': '2', 
         'categorie': 'Comédie',
         'description': 'Témoin de nombreux événements marquants des années 60 et 70, un homme simple d\'esprit et au grand cœur inspire ceux qui l\'entourent à travers son optimisme constant.',
         'image': 'https://fr.web.img5.acsta.net/medias/nmedia/18/64/74/53/18889951.jpg',
         'meilleurVendeur': 'non',
         'bandeAnnonce': 'https://youtu.be/OycTfchnopU'},
        
        {'nom': "Shrek 2", 
         'date': '07/02/2023', 
         'heure': '18:00', 
         'salle': '3', 
         'categorie': 'Animation',
         'description': 'Shrek et Fiona reviennent de leur lune de miel pour rencontrer les parents de celle-ci. Mais ces derniers ne s\'attendaient pas à ce que leur fille épouse un ogre.',
         'image': 'https://m.media-amazon.com/images/M/MV5BMzNmNjQ1NmUtNzhiZS00YWE2LTg4N2ItZTA2ODdmOTMwOTQ1XkEyXkFqcGc@._V1_.jpg',
         'meilleurVendeur': 'non',
         'bandeAnnonce': 'https://youtu.be/xBgSfhp5Fxo'},
        
        {'nom': "Le Loup de Wall Street", 
         'date': '08/02/2023', 
         'heure': '21:00', 
         'salle': '4', 
         'categorie': 'Biographie',
         'description': 'L\'histoire vraie de Jordan Belfort, courtier en bourse à New York qui a bâti une fortune colossale grâce à la corruption et la fraude avant de tout perdre.',
         'image': 'https://m.media-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_.jpg',
         'meilleurVendeur': 'non',
         'bandeAnnonce': 'https://youtu.be/GT9UfSqBz9o'},
        
        {'nom': "Oppenheimer", 
         'date': '09/02/2023', 
         'heure': '19:30', 
         'salle': '5', 
         'categorie': 'Biographie',
         'description': 'L\'histoire de J. Robert Oppenheimer, physicien théoricien qui a dirigé le développement de la première bombe atomique dans le cadre du projet Manhattan pendant la Seconde Guerre mondiale.',
         'image': 'https://i.ebayimg.com/images/g/zSsAAOSwejtjv4RH/s-l1600.jpg',
         'meilleurVendeur': 'non',
         'bandeAnnonce': 'https://youtu.be/CoXtvSRpHgM'},
        
        {'nom': "Lendemain de veille", 
         'date': '10/02/2023', 
         'heure': '22:00', 
         'salle': '6', 
         'categorie': 'Comédie',
         'description': 'Trois amis se réveillent à Las Vegas après une soirée d\'enterrement de vie de garçon complètement hors de contrôle, sans aucun souvenir de la veille et avec un tigre dans leur suite.',
         'image': 'https://m.media-amazon.com/images/M/MV5BYmIyODg0N2EtYjg5NC00NjdlLWFkZTgtMmE0NzI4ZGM5ODk1XkEyXkFqcGc@._V1_.jpg',
         'meilleurVendeur': 'non',
         'bandeAnnonce': 'https://youtu.be/hHqR9Tq16_E'}
    ]}
    return render(request, "films.html", contexte)

def aproposView(request):
    return render(request, "apropos.html")