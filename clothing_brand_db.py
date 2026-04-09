import sqlite3
conn = sqlite3.connect("/Users/quentin/Desktop/clothing_brand") #setup connexion
cursor = conn.cursor() #setup stylo 

#création tables 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS produits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        categorie TEXT,
        prix REAL
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produit_id INTEGER,
        quantite INTEGER,
        date_vente TEXT,
        chiffre_affaires REAL
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stocks (
        produit_id INTEGER PRIMARY KEY,
        quantite_stock INTEGER,
        seuil_min INTEGER, 
        FOREIGN KEY(produit_id) REFERENCES produits(id)
    )
""")


# Vérifie si les produits existent déjà
cursor.execute("SELECT COUNT(*) FROM produits")
produits_count = cursor.fetchone()[0]

# Vérifie si les ventes existent déjà
cursor.execute("SELECT COUNT(*) FROM ventes")
ventes_count = cursor.fetchone()[0]

# Vérifie si les stocks existent déjà
cursor.execute("SELECT COUNT(*) FROM stocks")
stocks_count = cursor.fetchone()[0]

#produits
if produits_count == 0:  # insère seulement si la table est vide 
    cursor.execute ("""
        INSERT INTO produits (nom, categorie, prix)
        VALUES (?, ?, ?)
    """, ("Veste", "Haut", 90))
    cursor.execute("""
        INSERT INTO produits (nom, categorie, prix)
        VALUES (?, ?, ?)
    """, ("Jean", "Bas", 85))
    cursor.execute("""
        INSERT INTO produits (nom, categorie, prix)
        VALUES (?, ?, ?)
    """, ("T-shirt", "Haut", 35))

#ventes
if ventes_count == 0:  
    cursor.execute("""
        INSERT INTO ventes (produit_id, quantite, date_vente, chiffre_affaires)
        VALUES (?, ?, ?, ?)
    """, (1, 17,"2025-04-16", 1530)) #format classique date SQL YYYY-MM-DD, Dans un vrai projet les données viennent d'un fichier CSV, d'une API ou d'un formulaire
    cursor.execute("""
        INSERT INTO ventes (produit_id, quantite, date_vente, chiffre_affaires)
        VALUES (?, ?, ?, ?)
    """, (2, 22,"2025-04-16",1870))
    cursor.execute("""
        INSERT INTO ventes (produit_id, quantite, date_vente, chiffre_affaires)
        VALUES (?, ?, ?, ?)
    """, (3, 40,"2025-04-16",1400))

#stocks
if stocks_count == 0: 
    cursor.execute("""
        INSERT INTO stocks (produit_id, quantite_stock, seuil_min)
        VALUES (?, ?, ?)
    """, (1, 25, 4))
    cursor.execute("""
        INSERT INTO stocks (produit_id, quantite_stock, seuil_min)
        VALUES (?, ?, ?)
    """, (2, 19, 4))
    cursor.execute("""
        INSERT INTO stocks (produit_id, quantite_stock, seuil_min)
        VALUES (?, ?, ?)
    """, (3, 50, 4))

#interrogation de la table 
cursor.execute("SELECT * FROM produits")
resultats = cursor.fetchall() #récupère tous les résultats de la requête sous forme de liste
for ligne in resultats:
    print(ligne)

#calcul du CA 
cursor.execute("SELECT SUM(chiffre_affaires) FROM ventes")
ca_total = cursor.fetchone()[0] # fetchone[0] récupère juste la première valeur au lieu d'une liste
print(f"Chiffre d'affaires total : {ca_total:.2f} €")

#produit le plus vendu
cursor.execute("""SELECT produits.nom, ventes.quantite FROM ventes JOIN produits ON ventes.produit_id = produits.id ORDER BY ventes.quantite DESC LIMIT 1""")
resultat = cursor.fetchone()
print(f"Produit le plus vendu : {resultat[0]} ({resultat[1]} unités)")

#alerte stock, n'affiche rien si la rupture de stock n'est pas proche 
cursor.execute("""SELECT produits.nom, stocks.seuil_min, stocks.quantite_stock FROM stocks JOIN produits ON stocks.produit_id = produits.id WHERE quantite_stock <= seuil_min""")
rupture_stock = cursor.fetchall()
if rupture_stock:
    for ligne in rupture_stock:
        print(f"Alerte stock : {ligne[0]} — {ligne[1]} unités restantes (seuil : {ligne[2]})")
else:
    print("Aucune alerte stock")

conn.commit()  # sauvegarde les changements
conn.close()   # ferme la connexion
