# 🎧 Leçon 1 : Le Guide Ultime du Vibecoding

> **"Tu ne tapes plus le code, tu diriges l'orchestre."**  
> Ce document est ta boussole pour comprendre la philosophie du *vibecoding*, éviter les erreurs classiques des débutants et construire des applications fiables rapidement.

---

## 1. Qu'est-ce que le Vibecoding ?

Le terme **Vibecoding** (popularisé par Andrej Karpathy, ex-Directeur IA chez Tesla et cofondateur d'OpenAI) décrit une nouvelle manière de concevoir du logiciel :
* **Avant** : Le développeur passait 80 % de son temps à chercher la syntaxe, écrire du code caractère par caractère et déboguer des points-virgules.
* **Aujourd'hui (Vibecoder)** : L'IA écrit le code. Toi, tu agis en tant que **Chef de Produit (Product Manager)** et **Architecte Technique**. Tu exprimes une vision claire, tu structures le projet, tu testes le résultat, et tu corriges la trajectoire de l'agent.

---

## 2. Les 6 Règles d'Or du Vibecoder

### Règle n°1 : Le principe des petits pas (Micro-itérations)
> **Erreur n°1 du débutant :** Demander *"Crée-moi un clone complet d'Airbnb avec paiement Stripe, messagerie instantanée et calendrier"* en un seul prompt.
* **Résultat garanti :** L'IA va créer des dizaines de fichiers à moitié finis, avec du code inventé, des bugs partout et un projet impossible à réparer.
* **La bonne méthode :** Découpe tout en étapes de 5 à 15 minutes :
  1. *Étape 1 :* Initialiser le projet et la page d'accueil avec un design épuré.
  2. *Étape 2 :* Créer les composants de cartes d'annonces avec des fausses données (mock data).
  3. *Étape 3 :* Ajouter le filtrage de recherche.
  4. *Étape 4 :* Connecter la base de données.

### Règle n°2 : Git est ton point de sauvegarde (Quick Save)
Considère Git comme la sauvegarde automatique d'un jeu vidéo difficile :
* Dès qu'une fonctionnalité **marche** (ex: le bouton fonctionne, le formulaire s'affiche bien) : fais un commit Git (`git commit -m "feat: formulaire de connexion fonctionnel"`).
* Si au prompt suivant l'IA casse tout et part dans une boucle infernale : **ne panique pas**. Tu peux revenir en 1 clic à ton dernier commit propre (`git reset --hard`).

### Règle n°3 : Choisis une stack "AI-friendly"
Toutes les technologies ne se valent pas pour le vibecoding. Choisis des technologies ultra-populaires pour lesquelles les modèles d'IA ont ingéré des milliards d'exemples :
* **Frontend** : React / Next.js, Vite + React, ou Tailwind CSS (l'IA excelle en Tailwind).
* **Backend** : Node.js (Express / Fastify) ou Python (FastAPI).
* **Base de données & Auth** : Supabase, Firebase ou SQLite/PostgreSQL avec Prisma ou Drizzle ORM.
* **Composants UI préfaits** : shadcn/ui, Lucide Icons.

### Règle n°4 : Ne jamais laisser l'IA deviner le contexte
L'IA n'est pas télépathe. Si tu lui dis juste *"ajoute le bouton de partage"*, elle ne sait pas où le placer, quel style appliquer, ni quelle action déclencher.
* Mentionne toujours les fichiers concernés (ex: `@Button.tsx`, `@Header.tsx`).
* Indique le comportement attendu et les cas limites.

### Règle n°5 : Savoir lire une erreur sans paniquer
En tant que débutant, quand un écran rouge s'affiche, applique cette routine :
1. Copie l'intégralité du message d'erreur du terminal ou de la console du navigateur (F12).
2. Fournis-le à l'IA en précisant ce que tu venais de faire.
3. Ne dis jamais simplement *"ça marche pas"*. Dis : *"J'ai cliqué sur le bouton X, j'attendais Y, mais j'ai obtenu cette erreur dans la console : [coller l'erreur]"*.

### Règle n°6 : La "Règle des 3 essais" (Kill the loop)
Si tu demandes à l'IA de corriger un bug et qu'au bout de 3 échanges le bug persiste ou empire :
* **Arrête la conversation.**
* Fais un `git restore` pour revenir à l'état propre.
* Repense ton explication ou donne-lui plus de détails (logs console, état des variables).
* Recommence dans un nouveau chat ou avec un prompt reformulé.

---

## 3. Le cycle de vie d'un projet Vibecoding

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│   1. Idée   │ ──> │    2. PRD    │ ──> │ 3. Maquette │ ──> │ 4. Découpage │
│ (Quoi & Pourquoi)  │ (Cahier des charges)│ (Visuel/UI) │     │ (Checklist)  │
└─────────────┘     └──────────────┘     └─────────────┘     └──────────────┘
                                                                    │
                                                                    ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│  8. Déployer│ <── │ 7. Sauver    │ <── │  6. Tester  │ <── │ 5. Coder     │
│  (Vercel/...) │     │ (Git Commit) │     │ (En local)  │     │ (Par brique) │
└─────────────┘     └──────────────┘     └─────────────┘     └──────────────┘
```

---

## 4. Conseils pour monétiser et répondre à des missions clients

Quand tu réalises des projets pour des clients ou en freelance :
1. **Ne vends pas ton temps, vends un résultat** : Grâce à l'IA, tu peux créer une landing page ou un MVP en 4 heures là où une agence met 3 semaines. Facture au forfait et à la valeur apportée.
2. **La sécurité d'abord (Secrets & Clés API)** : Ne commit **JAMAIS** de clés API privées (OpenAI, Stripe, Supabase) dans un repo Git public. Utilise toujours des fichiers `.env` et ajoute `.env` dans ton `.gitignore`.
3. **Livrables propres** : Fournis toujours un fichier `README.md` expliquant comment lancer le projet en 2 commandes (`npm install`, `npm run dev`).
4. **Garde le contrôle du code** : Même si tu ne l'as pas écrit à la main, fais-toi expliquer par l'agent le rôle des composants principaux pour pouvoir répondre sereinement aux questions du client.
