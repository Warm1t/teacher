# 🤖 Leçon 4 : Maîtriser les Agents IA & les Workflows Autonomes

> **"Un chatbot répond à tes questions. Un Agent résout tes problèmes."**  
> Comprendre la mécanique des agents autonomes est la compétence la plus puissante pour démultiplier ta productivité de vibecoder.

---

## 1. Chatbot classique vs Agent IA : La vraie différence

Beaucoup de débutants confondent un simple modèle de chat (comme ChatGPT dans le navigateur) et un **Agent IA** (comme Antigravity, Claude Code, ou Devin) :

| Caractéristique | Chatbot classique | Agent IA Autonome |
| :--- | :--- | :--- |
| **Accès aux fichiers** | Copier-coller manuel uniquement | Lit, crée et modifie directement tes fichiers |
| **Terminal / Commandes** | Te donne une commande à copier | Exécute lui-même `npm install`, `git commit`, lance les tests |
| **Boucle d'action** | 1 question = 1 réponse | **ReAct** (Raisonnement ➔ Action ➔ Observation ➔ Décision) |
| **Débogage** | Attend que tu lui rapportes l'erreur | Lance le build, lit l'erreur, et corrige lui-même le fichier |
| **Outils externes** | Aucun | Peut naviguer sur le web, interroger une BDD via **MCP** |

---

## 2. La posture mentale : Devenir le "Lead Developer" de l'agent

Pense à l'agent comme à un **développeur junior surdoué mais distrait** :
* Il est hyper rapide, connaît des milliers de technologies, et ne dort jamais.
* Mais si tu ne lui donnes pas de directives claires ou de garde-fous, il peut facilement s'emballer, installer des librairies inutiles ou modifier des fichiers qu'il ne devrait pas toucher.

### Ta responsabilité en tant que vibecoder :
1. **Définir l'objectif clair** (Quoi faire et où s'arrêter).
2. **Fournir les règles du jeu** (ex: *"utilise Tailwind, pas de CSS custom"*).
3. **Surveiller les actions critiques** (création de migrations SQL, suppressions de fichiers, commandes destructives).
4. **Valider le résultat** dans ton navigateur ou ton application.

---

## 3. Le Protocole MCP (Model Context Protocol)

Le **MCP** est le standard universel qui permet à un agent IA de se connecter à n'importe quel service extérieur :
* **Base de données** : Se connecter directement à ta base PostgreSQL pour exécuter des requêtes ou inspecter les tables.
* **Navigateur (Puppeteer/Playwright)** : Permettre à l'agent d'ouvrir un navigateur réel, de cliquer sur ton site et de vérifier que tout fonctionne.
* **GitHub** : Créer automatiquement des Pull Requests, cloner des dépôts, ou gérer les issues.
* **Figma** : Lire directement les maquettes graphiques pour générer le code React pixel-perfect.

---

## 4. Multi-agents et Tâches en arrière-plan (Background Tasks)

Dans les environnements modernes comme Antigravity :
* **Sous-agents (Subagents)** : Tu peux confier une tâche de recherche ou de refactorisation à un sous-agent qui travaille en parallèle pendant que tu continues de coder avec ton agent principal.
* **Exécution en arrière-plan** : Des commandes longues (téléchargements, compilation, scraping) tournent en tâche de fond sans bloquer la conversation.
* **Tâches planifiées (Cron / Schedules)** : Possibilité de programmer des tâches de maintenance récurrentes (sauvegarde, audit de code, vérification de liens cassés).

---

## 5. Checklist de livraison d'un projet réalisé avec un Agent

Avant de considérer qu'une mission ou une application est terminée :
- [ ] **Build réussi** : Lancer la commande de build (`npm run build`) pour vérifier qu'aucune erreur TypeScript ou de syntaxe ne bloque la production.
- [ ] **Nettoyage des logs** : Supprimer les `console.log` de test inutiles.
- [ ] **Fichier `.env.example`** : Créer un fichier modèle sans valeurs sensibles pour que le client ou un autre développeur sache quelles variables configurer.
- [ ] **Documentation de démarrage (`README.md`)** : Inclure les étapes précises :
  1. Prérequis (Node version, Python version).
  2. Installation des dépendances.
  3. Lancement en local.
- [ ] **Commit Git propre** : Un dépôt propre avec un historique de commits lisible.
