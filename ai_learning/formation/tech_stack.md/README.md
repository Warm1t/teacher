# 🛠️ Leçon 6 : La Stack Technique Idéale du Vibecoder

> **"Toutes les technologies ne sont pas égales face à l'IA. Choisir les bons outils multiplie la vitesse et la précision de l'agent par 10."**  
> Cette leçon t'aide à choisir les briques logicielles les plus efficaces pour tes projets et à comprendre la structure d'une application moderne.

---

## 1. Qu'est-ce qu'une "Stack AI-Friendly" ?

Les modèles d'IA récents (Gemini, Claude, GPT) ont été entraînés sur des millions de dépôts GitHub. Plus une technologie est populaire, moderne et documentée, plus l'IA sera performante pour générer du code sans bug.

| Critère | ✅ À privilégier (AI-Friendly) | ❌ À éviter pour débuter en vibecoding |
| :--- | :--- | :--- |
| **Design / CSS** | **Tailwind CSS** (l'IA génère du design magnifique en une seule ligne) | CSS pur avec 15 fichiers `.css` séparés (dur à synchroniser) |
| **Composants UI** | **shadcn/ui**, **Lucide Icons** (composants accessibles et modernes) | Librairies vieillissantes ou avec composants obscurs |
| **Frontend** | **React / Next.js** ou **Vite + React** (énorme volume de données d'entraînement) | Frameworks exotiques ou trop récents |
| **Base de données** | **Supabase** (PostgreSQL + Auth + Stockage avec interface visuelle) | Configurer un serveur SQL manuellement en local |
| **Backend & API** | **Next.js Route Handlers** ou **FastAPI (Python)** | Architectures complexes en microservices |

---

## 2. Les 3 Stacks de Référence selon ton Projet

### 🅰️ La Stack n°1 : Le Couteau Suisse Web & SaaS (Recommandée à 80 %)
*Pour : Créer une plateforme, un outil SaaS avec connexion utilisateur, un tableau de bord ou une marketplace.*
* **Framework** : **Next.js** (App Router) ou **Vite + React + TypeScript**
* **Style** : **Tailwind CSS** + **shadcn/ui**
* **Icônes** : **lucide-react**
* **Base de données & Auth** : **Supabase** (gratuit, prêt en 2 minutes)
* **Paiement (si payant)** : **Stripe** (Checkout)
* **Hébergement** : **Vercel**

### 🅱️ La Stack n°2 : Backend, Automatisations & Agents IA
*Pour : Un bot WhatsApp/Telegram, un script de scraping, une API de traitement de texte ou de données.*
* **Langage** : **Python 3.11+**
* **Framework API** : **FastAPI** (génère la documentation Swagger automatiquement)
* **Validation de données** : **Pydantic**
* **Base de données** : **SQLite** (débutant) ou **PostgreSQL**
* **Hébergement** : **Render** ou **Railway**

### 🅲️ La Stack n°3 : Landing Page Ultra-Rapide
*Pour : Un site vitrine, une page de vente ou un portfolio sans base de données complexe.*
* **Framework** : **Astro** ou **HTML + Tailwind CSS**
* **Formulaire de contact** : **Resend** ou **Formspree**

---

## 3. L'anatomie d'un projet moderne (Comprendre les dossiers)

Quand un agent crée un projet, voici à quoi servent les dossiers principaux :

```
mon-projet/
├── public/              # Fichiers statiques (images, logo.svg, favicon)
├── src/                 # Tout le code source de ton application
│   ├── app/ (ou pages/) # Les différentes pages / routes de ton site (ex: /login, /dashboard)
│   ├── components/      # Les blocs réutilisables (Bouton, Carte, Navbar, Footer)
│   ├── hooks/           # Fonctions utilitaires React personnalisées (ex: useAuth)
│   ├── lib/             # Configurations des services tiers (ex: client Supabase, Stripe)
│   └── types/           # Définitions TypeScript pour sécuriser les données
├── .env.local           # Tes variables secrètes locales (clés d'API)
├── .gitignore           # Liste des fichiers que Git ne doit jamais envoyer sur GitHub
├── package.json         # Carte d'identité du projet et liste des librairies installées
└── tailwind.config.js   # Configuration graphique (couleurs personnalisées, polices)
```

---

## 4. Gérer les variables d'environnement (`.env`)

Toutes les applications réelles ont besoin de clés secrètes :
1. **En local sur ton PC** : Range-les dans un fichier `.env.local` (ou `.env`).
2. **Comment l'application les lit ?**
   - Côté Next.js / Node : `process.env.OPENAI_API_KEY`
   - Côté Vite : `import.meta.env.VITE_API_URL`
   - Côté Python : `os.getenv("OPENAI_API_KEY")`
3. **Sécurité vitale** : Une variable préfixée par `NEXT_PUBLIC_` ou `VITE_` sera visible dans le navigateur de n'importe quel visiteur. Ne mets jamais une clé privée avec ce préfixe !
