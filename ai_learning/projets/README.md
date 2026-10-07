# 💻 Espace Projets : L'Atelier Pratique

> C'est ici que tu passes de la théorie à la pratique ! Chaque sous-dossier de ce répertoire sera une véritable application que tu construis, testes et déploies.

---

## 🛠️ Comment lancer ton tout premier projet (Workflow en 5 étapes)

Quand tu as une idée de projet (ex: un outil SaaS, une to-do list intelligente, un clone d'application, un site vitrine) :

### 1. Crée un sous-dossier pour ton projet
Crée un nouveau dossier dans `projets/` avec le nom de ton application (ex: `projets/mon-premier-saas`).

### 2. Copie le modèle de PRD
Copie le fichier [template_prd.md](file:///d:/AI%20learning/formation/prd.md/template_prd.md) et colle-le dans ton nouveau dossier sous le nom `PRD.md`.  
Remplis les sections essentielles (ou utilise le prompt d'interview de la Leçon 3 pour le faire avec l'IA).

### 3. Initialise le projet et Git
Ouvre ton terminal dans le dossier du projet et initialise la stack (ex: Next.js + Tailwind) et Git :
```bash
git init
git add .
git commit -m "feat: initialisation du projet"
```

### 4. Code brique par brique avec l'Agent
Ouvre le panneau Antigravity et guide l'agent étape par étape en utilisant les prompts de la [Bibliothèque de Prompts](file:///d:/AI%20learning/formation/prompt.md/prompt_library.md).
* Fais un commit Git après chaque fonctionnalité terminée.

### 5. Déploie sur Vercel
Envoie ton code sur GitHub (`git push`) et connecte ton dépôt à Vercel en suivant la [Leçon 7 : Déploiement](file:///d:/AI%20learning/formation/deployment.md/README.md).

---

## 💡 3 Idées de projets idéaux pour débuter :
1. **Le "Markdown Note / Todo Tracker"** : Une application simple avec sauvegarde locale pour te familiariser avec les composants React et Tailwind CSS.
2. **Le "Générateur de Posts Réseaux Sociaux"** : Une app connectée à l'API Gemini / OpenAI qui génère des posts LinkedIn ou Twitter à partir d'un sujet donné.
3. **Le "Portfolio Personnel / Landing Page"** : Ton futur site de freelance pour présenter tes compétences et tes réalisations à tes futurs clients.
