       #EXercice 1
import csv
import matplotlib.pyplot as plt

#  Tâche 1 : Lecture du fichier CSV
def lire_csv(nom_fichier):
    """
    Lit un fichier CSV et retourne une liste de dictionnaires.
    """
    donnees = []
    with open(ebola_guinea, mode='r', encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier, delimiter=',')
        for ligne in lecteur:
            # Conversion des nombres en entiers
            ligne['Cas'] = int(ligne['Cas'])
            ligne['Dèces'] = int(ligne['Dèces'])
            donnees.append(ligne)
    return donnees

# Tâche 2 : Calculs statistiques
def calculer_statistiques(donnees):
    """
    Calcule les totaux et taux de mortalité par préfecture.
    Retourne un dictionnaire {préfecture: {cas, deces, taux}}.
    """
    stats = {}
    for entree in donnees:
        pref = entree['Préfecture']
        if pref not in stats:
            stats[pref] = {'cas': 0, 'deces': 0}
        stats[pref]['cas'] += entree['Cas']
        stats[pref]['deces'] += entree['Dèces']
    
    # Calcul du taux de mortalité
    for pref in stats:
        cas = stats[pref]['cas']
        deces = stats[pref]['deces']
        stats[pref]['taux'] = deces / cas if cas > 0 else 0.0
    return stats

# Tâche 3 : Visualisation
def visualiser_donnees(stats):
    """
    Génère deux diagrammes à barres : cas totaux et taux de mortalité.
    """
    prefectures = list(stats.keys())
    cas = [stats[pref]['cas'] for pref in prefectures]
    taux = [stats[pref]['taux'] for pref in prefectures]

    # Diagramme des cas
    plt.figure(figsize=(10, 5))
    plt.bar(prefectures, cas, color='skyblue')
    plt.title('Nombre total de cas par préfecture')
    plt.xlabel('Préfecture')
    plt.ylabel('Cas')

    # Diagramme du taux de mortalité
    plt.figure(figsize=(10, 5))
    plt.bar(prefectures, taux, color='salmon')
    plt.title('Taux de mortalité par préfecture')
    plt.xlabel('Préfecture')
    plt.ylabel('Taux (Décès/Cas)')
    plt.ylim(0, 1)  # Limite pour une meilleure lisibilité

    plt.show()

# Exécution principale
if __name__ == "__main__":
    donnees = lire_csv('ebola_guinea.csv')
    stats = calculer_statistiques(donnees)
    visualiser_donnees(stats)
# %%
 