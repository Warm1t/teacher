# 🚀 Leçon 7 : Mettre en Ligne & Déployer son Projet

> **"Un projet qui ne tourne que sur `localhost` n'existe pas pour tes utilisateurs ou tes clients."**  
> Déployer une application moderne ne nécessite plus de gérer des serveurs compliqués. En 2026, mettre une application en ligne prend 3 minutes et ne coûte rien au démarrage.

---

## 1. La Sainte Trinité du Déploiement Gratuit

Pour héberger une application complète à 0 € de coût fixe :

```
┌─────────────────────────┐          ┌─────────────────────────┐
│     Code Source         │          │     Hébergement Web     │
│       GitHub            │ ───────> │         Vercel          │
│  (Sauvegarde du code)   │  (Sync)  │  (Frontend & Next.js)   │
└─────────────────────────┘          └─────────────────────────┘
                                                  │
                                                  ▼
                                     ┌─────────────────────────┐
                                     │     Base de Données     │
                                     │        Supabase         │
                                     │  (Postgres, Auth, Files)│
                                     └─────────────────────────┘
```

* **GitHub** : Héberge ton code et déclenche la mise en ligne automatique dès que tu fais un `git push`.
* **Vercel** : Construit et héberge ton application web, distribue ton site sur un CDN mondial et gère le HTTPS automatiquement.
* **Supabase** : Fournit une vraie base de données PostgreSQL dans le cloud, avec authentification et stockage de fichiers.

---

## 2. Déployer sur Vercel en 4 Étapes Chrono

1. **Rends-toi sur [Vercel.com](https://vercel.com)** et connecte-toi avec ton compte **GitHub**.
2. Clique sur **"Add New..."** > **"Project"**.
3. Sélectionne ton dépôt GitHub dans la liste et clique sur **"Import"**.
4. **Très Important (Variables d'environnement)** :
   - Déroule la section **"Environment Variables"**.
   - Copie-colle toutes les variables de ton fichier `.env` local (ex: clés Supabase, clés Stripe).
5. Clique sur **"Deploy"** !
6. En moins de 2 minutes, Vercel te donne une URL sécurisée (ex: `https://mon-application.vercel.app`) accessible au monde entier.

> **Le superpouvoir de Vercel :** Chaque fois que tu feras `git push` pour ajouter une fonctionnalité, Vercel redéploiera automatiquement ton site à jour en arrière-plan sans aucune coupure de service.

---

## 3. Connecter un Nom de Domaine Personnalisé

Pour un projet professionnel ou une mission client (ex: `monprojet.fr` au lieu de `monprojet.vercel.app`) :
1. Achète un nom de domaine sur un registrar réputé (ex: **Namecheap**, **Cloudflare**, ou **OVH**) pour environ 8 à 12 € / an.
2. Dans Vercel, va dans **Settings** > **Domains** > Ajoute ton domaine.
3. Vercel t'indiquera deux lignes à copier dans la zone DNS de ton registrar :
   - Un enregistrement **A** pointant vers l'IP de Vercel (`76.76.21.21`).
   - Un enregistrement **CNAME** pour le sous-domaine `www` (`cname.vercel-dns.com`).
4. Vercel génère automatiquement un certificat SSL (cadenas vert HTTPS) sans configuration manuelle.

---

## 4. Checklist Pré-Lancement & Livraison Client

Avant de partager le lien final à un client ou à tes premiers utilisateurs, vérifie ces 6 points :

- [ ] **Test Mobile** : Ouvre le site sur ton smartphone (ou via l'inspecteur F12 en mode mobile). Les textes se lisent-ils bien ? Les boutons sont-ils facilement cliquables ?
- [ ] **Variables d'environnement** : Toutes les clés API de production sont-elles bien renseignées dans Vercel ?
- [ ] **Favicon & Titre d'onglet** : Remplace le logo par défaut (ex: le logo React ou Vercel) par ton propre logo et vérifie le titre de la page dans le navigateur.
- [ ] **Formulaires & Boutons** : Envoie un message de test ou crée un compte pour t'assurer que les données arrivent bien en base.
- [ ] **Page 404** : Vérifie qu'une fausse URL (ex: `site.com/azerty`) affiche une page d'erreur conviviale avec un bouton de retour à l'accueil.
- [ ] **Vitesse de chargement** : Teste ton lien sur [pagespeed.web.dev](https://pagespeed.web.dev) pour t'assurer que le site charge rapidement.
