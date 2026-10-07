# 🐙 Leçon 5 : Git & GitHub – Le Filet de Sécurité du Vibecoder

> **"Un vibecoder sans Git est un funambule sans filet de sécurité."**  
> Avec l'IA, tu vas modifier des centaines de lignes de code en quelques secondes. Savoir sauvegarder et annuler instantanément une mauvaise manipulation est ta compétence de survie numéro 1.

---

## 1. Pourquoi Git est indispensable pour le Vibecoding ?

Quand un agent d'IA écrit du code :
* **90 % du temps** : Il produit un travail remarquable et rapide.
* **10 % du temps** : Il tente de résoudre un problème, s'égare, commence à modifier des fichiers sans rapport et casse des fonctionnalités qui marchaient 5 minutes plus tôt.

Si tu n'utilises pas Git, tu te retrouves à faire `Ctrl + Z` désespérément dans 12 onglets différents.  
Avec Git, **un simple clic ou une seule commande te ramène à la seconde exacte où tout fonctionnait**.

---

## 2. Les 7 Commandes Git à connaître par cœur

| Commande | À quoi ça sert ? | Quand l'utiliser ? |
| :--- | :--- | :--- |
| `git status` | Voir l'état actuel | Savoir quels fichiers ont été créés ou modifiés par l'agent. |
| `git add .` | Préparer la sauvegarde | Ajouter toutes les modifications prêtes à être sauvegardées. |
| `git commit -m "mon message"` | Créer un point de sauvegarde | Dès qu'une fonctionnalité marche (ex: *"feat: bouton login fonctionnel"*). |
| `git log --oneline` | Voir l'historique | Visualiser la liste de tes points de sauvegarde récents. |
| `git restore .` | **Annulation d'urgence (Fichiers)** | L'agent a fait n'importe quoi sur des fichiers non commités ? Cette commande efface ses bêtises et remet tout à propre ! |
| `git push` | Envoyer sur GitHub | Sauvegarder ton code dans le cloud et déclencher le déploiement. |
| `git pull` | Récupérer les nouveautés | Synchroniser le code depuis GitHub sur ton ordinateur. |

---

## 3. Le scénario d'urgence : L'IA a tout cassé, que faire ?

### Scénario A : Tu n'as pas encore fait de commit
L'agent vient d'effectuer des modifications qui ne fonctionnent pas du tout :
```bash
# Annule toutes les modifications non sauvegardées sur les fichiers existants
git restore .

# Supprime les nouveaux fichiers créés inutilement par l'agent
git clean -fd
```
*Magie : Ton projet revient instantanément à son état initial parfait.*

### Scénario B : Tu as déjà fait un commit foireux
Tu veux revenir au commit précédent :
```bash
# Revenir en arrière d'un commit en effaçant les modifications
git reset --hard HEAD~1
```

---

## 4. La règle absolue : Le fichier `.gitignore` et les secrets

Ne mets **JAMAIS** tes clés d'API (OpenAI, Stripe, Supabase, etc.) sur GitHub.

1. Range toutes tes clés dans un fichier nommé **`.env`** ou **`.env.local`** :
   ```env
   SUPABASE_KEY=eyJh...
   OPENAI_API_KEY=sk-proj-...
   ```
2. Crée un fichier nommé **`.gitignore`** à la racine de ton projet et écris-y :
   ```gitignore
   node_modules/
   .env
   .env.local
   .env.*.local
   dist/
   build/
   .DS_Store
   ```
3. Crée un fichier **`.env.example`** sans tes vraies clés pour documenter ce qui est requis :
   ```env
   SUPABASE_KEY=votre_cle_ici
   OPENAI_API_KEY=votre_cle_ici
   ```

---

## 5. Comment créer et lier ton projet à GitHub (Pas à pas)

1. Initialise Git dans ton dossier local :
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```
2. Va sur [github.com](https://github.com) et crée un nouveau dépôt vide (nommé par exemple `mon-projet`).
3. Lie ton dossier local et envoie ton code :
   ```bash
   git branch -M main
   git remote add origin https://github.com/ton-profil/mon-projet.git
   git push -u origin main
   ```
4. Ton projet est désormais en sécurité dans le cloud et prêt pour être déployé !
