# TP1 - Interface Web - Cinéma le Scénario

**Date de remise :** 2026-02-27 (23:59)  
**Pondération :** 15%

---

## 📋 Liste des tâches à compléter

### 🎯 Page Maîtresse (maitre.html)

#### En-tête (Header)
- ✅ Nom du cinéma "Cinéma le Scénario"
- ✅ Image d'arrière-plan adaptée (wallpaper.png)
- ✅ Couleur d'arrière-plan

#### Menu (menu.html)
- ✅ Menu présent sur toutes les pages
- ✅ Liens vers Accueil, Films, Documentation, À propos
- ✅ Navigation Bootstrap

#### Pied de page (Footer)
- ✅ Footer présent
- ✅ Adresse du cinéma de La Pocatière
- ✅ Date du jour formatée ({% now "j F Y" %})
- ✅ Courriel pour information
- ✅ Nom des responsables (Mathias et Trystan)

#### Structure générale
- ✅ Blocks prédéfinis (header, menu, contenu, footer)
- ✅ Bootstrap installé et fonctionnel
- ✅ CSS personnalisé (style.css)
- ❌ En-tête + Menu + Footer ne dépassent pas 30% de la page
- ✅ Zones ne se chevauchent pas

---

### 🏠 Page Accueil (accueil.html)

- ✅ Titre de page "Cinéma - Accueil"
- ❌ **Disposition sur DEUX colonnes** (actuellement 1 colonne)
- ❌ Description du travail (copier description de la page 1 de l'énoncé)
- ❌ Image du cinéma
- ✅ Contenu dans la zone appropriée
- ❌ Styles appliqués pour deux colonnes

**Améliorations possibles :**
- Meilleure mise en page (documenter si fait)

---

### ℹ️ Page À Propos (apropos.html)

- ✅ Titre de page "Cinéma - À propos"
- ❌ **Disposition sur DEUX colonnes**
- ❌ Description environnement de développement :
  - Version Python
  - Version Django
  - Version Visual Studio Code ou PyCharm
- ❌ Informations des concepteurs :
  - Nom
  - Numéro d'étudiant
  - Cours
  - Travail demandé
  - Date de remise
  - Cégep
- ✅ Contenu dans la zone appropriée

**Améliorations possibles :**
- Mise en page différente de la page Accueil
- Utilisation de variables Django avec filtres (pipe filters)

---

### 📚 Page Documentation (documentation.html)

- ✅ Titre de page "Cinéma - Documentation"
- ❌ Liste des améliorations apportées au site
- ❌ Pour chaque amélioration :
  - Titre significatif
  - Brève description (petit paragraphe)
- ❌ Informations réparties sur la largeur de la page
- ⚠️ Si aucune amélioration : indiquer "Aucune amélioration apportée"

**Améliorations possibles :**
- Liens URL vers pages de détails des ajouts
- Système de retour vers page Documentation

---

### 🎬 Page Films (films.html)

- ✅ Titre de page "Cinéma - Films"
- ❌ **Liste de minimum 6 films** (actuellement 0)
- ❌ **Affichage sur TROIS colonnes**
- ❌ Pour chaque film, afficher :
  - Nom
  - Date
  - Heure
  - Salle
  - Catégorie
  - Description
  - Image
  - MeilleurVendeur
- ❌ Données provenant de "LesFilms.txt" (2 films fournis)
- ❌ Ajouter 4 films supplémentaires

**Améliorations possibles :**
- Zone contenu déroulable (pied de page toujours visible)
- Lien du titre vers bande annonce (externe)

---

## 🎨 Styles et Responsive

- ✅ Bootstrap 5.3.8 installé
- ✅ Fichier style.css créé et lié
- ✅ Styles appliqués sur les pages
- ✅ Image de fond header (wallpaper.png)
- ✅ Configuration langue française (fr-ca)
- ❌ Adaptation en fonction du format d'affichage
- ❌ Adaptation en fonction de la résolution
- ❌ Design responsive mobile/tablette

---

## 📁 Fichiers à remettre

- ❌ Dossier compressé de l'application
- ❌ Fichier `eval_coequipier.txt` avec :
  - Nom du coéquipier
  - Note sur 5 (ex: "Louis Gaudreau 4/5")
  - Commentaires (optionnel)

---

## 📊 Critères d'évaluation

| Critère | Pondération | Statut |
|---------|-------------|--------|
| Utilisation appropriée du langage de balisage | 20% | � Partiellement fait |
| Création et utilisation des feuilles de styles | 5% | 🟢 Partiellement fait |
| Intégration correcte des images | 10% | 🟡 En cours |
| Adaptation format d'affichage et résolution | 5% | 🔴 À faire |
| Interactions interface web - utilisateur | 30% | 🟢 Partiellement fait |
| Qualité de l'application | 20% | 🟡 En cours |
| Documentation | 10% | 🔴 À faire |

---

## 🎯 Évaluation finale

- Travail remis : **60%**
- Compréhension du travail (revue de code) : **35%**
- Évaluation des pairs : **5%**

⚠️ **Attention :** Pénalité de 1% par faute de français (max 10%)

---

## ✅ Résumé - Ce qui est fait

1. ✅ Structure de base Django
2. ✅ Page maîtresse avec header, menu, footer
3. ✅ Navigation entre les 4 pages
4. ✅ Bootstrap installé
5. ✅ CSS personnalisé
6. ✅ Titres de pages appropriés
7. ✅ Séparation propre header/menu/footer
8. ✅ Image wallpaper en background du header
9. ✅ Footer complet (adresse, date dynamique, courriel, responsables)
10. ✅ Date en français avec Django (fr-ca)
11. ✅ Lorem ipsum ajouté dans toutes les pages

## 🔴 Priorités - Ce qui reste à faire

### 🔥 Priorité HAUTE
1. **Page Films** - Affichage 6 films sur 3 colonnes
2. **Page Accueil** - 2 colonnes (description + image)
3. **Page À Propos** - 2 colonnes (environnement + concepteurs)

### 🟡 Priorité MOYENNE
4. Images dans les pages de contenu
5. Responsive design
6. Page Documentation avec améliorations

### ⚪ Priorité BASSE
7. Améliorations bonus
8. Fichier eval_coequipier.txt
9. Compression du dossier pour remise

---

**Bon travail ! 🚀**
