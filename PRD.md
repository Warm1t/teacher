# 📑 PRD : MATHS MASTER — Chatbot Spécialisé de l'Ingénieur

> **Vision Produit** : Une plateforme d'ingénierie mathématique sobre, élégante en style **blanc/encre** (esthétique académique sans fioriture ni gamification), articulée autour d'un **Chatbot Pédagogique Spécialisé**, d'une arborescence rigoureuse de **Dossiers de Cours**, de **Dossiers de TD (Travaux Dirigés)** et d'un onglet dédié aux **Programmes de Révision**.  
> **Principe Cardinal** : L'espace démarre **entièrement vierge**. Aucun faux cours n'est pré-rempli tant que l'étudiant n'a pas importé ses propres matières.

---

## 1. Vue d'Ensemble du Projet

* **Nom du Produit** : **Maths Master**
* **Philosophie Visuelle** : **Encre & Papier** (fond ivoire/blanc pur `#faf9f6` / `#ffffff`, typographie encre profonde `#18181b`, bordures pierre douces, style polytechnique/édition scientifique).
* **Zéro Gamification** : Pas de points XP, pas de badges d'apprenti, pas de confettis. Une posture d'adulte, de rigueur et d'excellence intellectuelle.
* **Public Cible** : Élèves-ingénieurs et étudiants en CPGE souhaitant un tuteur IA dédié, capable d'assimiler leurs polycopiés et de corriger leurs exercices en respectant scrupuleusement les théorèmes et notations de leur école.

---

## 2. Architecture Fonctionnelle & Navigation

L'application est découpée en **espaces clairs** :

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  ⚡ MATHS MASTER       [💬 Chatbot]   [📚 Cours]   [📝 TD & Exos]   [📅 Révisions]   ☁️│
├────────────────────────────┬───────────────────────────────────────────────────────────┤
│ 📁 EXPLORATEUR LATÉRAL     │ 🏛️ ESPACE CENTRAL DÉDIÉ                                   │
│                            │                                                           │
│ 📚 DOSSIERS DE COURS       │  • Mode Chatbot :                                         │
│   (Vide par défaut)        │    Discussion avec le Professeur d'Élite                 │
│   [+ Nouveau Cours]        │    Contexte dynamique du cours/TD sélectionné             │
│                            │    Rendu mathématique rigoureux KaTeX                     │
│ 📝 DOSSIERS DE TD          │                                                           │
│   (Vide par défaut)        │  • Mode Cours / TD :                                      │
│   [+ Nouveau TD]           │    Édition & consultation des polycopiés de l'élève       │
│                            │                                                           │
│ 🎯 Contexte actif :        │  • Mode Programmes de Révision :                          │
│   [Aucun cours chargé]     │    Calendrier de révision et fiches d'ancrage             │
└────────────────────────────┴───────────────────────────────────────────────────────────┘
```

---

## 3. Les Modules Détaillés

### 💬 Module 1 : Le Chatbot Spécialisé d'Élite
* **Le Tuteur Rigoureux** : Incarne le meilleur pédagogue d'école d'ingénieur (style Feynman / Strang).
* **Ancrage Strict sur le Cours de l'Élève** :
  * Si aucun cours n'est chargé : Le chatbot invite l'élève à renseigner son premier cours ou TD, ou répond aux questions générales de méthode.
  * Si un cours est sélectionné : Le chatbot utilise **exclusivement** les définitions, hypothèses et notations du cours actif pour corriger et guider.
* **Rendu Mathématique $\LaTeX$ Instantané** : Formules propres intégrées avec KaTeX ($...$ et $$...$$).
* **Actions Rapides de Travail** :
  - `🎯 Corriger ma démarche` : Analyse chirurgicale de la copie de l'élève (justesse, rigueur des hypothèses, clarté).
  - `💡 Indice sans solution` : Donne l'impulsion géométrique ou physique pour débloquer le calcul sans gâcher la recherche.
  - `🔍 Point de méthode` : Rappelle la colonne vertébrale du théorème appliqué.

---

### 📚 Module 2 : Gestionnaire des Dossiers de Cours & Visionneuse Visuelle
* **État Initial** : **100% Vierge**. Aucun cours imposé.
* **Lecture & Rendu Visuel HD des Polycopiés PDF (Canvas)** :
  - **Fidélité Totale aux Notations Mathématiques** : Les formules, matrices, intégrales multiples, tenseurs et graphiques géométriques ne sont plus découpés en chaînes de texte brut illisibles. Chaque page est rendue en **haute résolution sur `<canvas>`** à l'échelle optimale avec un fond blanc contrasté.
  - **Stockage Local Haute Capacité (IndexedDB)** : Sauvegarde fluide de polycopiés de plusieurs dizaines de pages dans une base locale `MathsMasterDB`, sans dépasser les quotas de `localStorage`.
  - **Aperçu Miniature Page 1** : Chaque carte de cours affiche la miniature fidèle de sa première page avec le badge du nombre de pages HD.
  - **Visionneuse Visuelle Intégrée (Modal)** : Permet de feuilleter les pages du document avec boutons de navigation `← Page précédente` / `Page suivante →`.
  - **Bouton d'envoi vers le Chat** : « 💬 Travailler cette page avec le Prof » envoie directement l'image de la page en cours au tuteur IA.
* **Création Manuelle & Organisation** :
  - Bouton `+ Ajouter Manuellement` pour saisir directement des théorèmes en Markdown + $\LaTeX$.
  - Détection automatique de la discipline (Algèbre linéaire, Analyse, Probabilités, etc.) basée sur le contenu.

---

### 📝 Module 3 : Gestionnaire des Dossiers de TD & Exercices
* **État Initial** : **100% Vierge**.
* **Importation Directe de Feuilles de TD en PDF Visuel** :
  - Bouton `📄 Importer un PDF de TD` ou Glisser-Déposer direct d'une feuille de TD `.pdf`.
  - Rendu visuel immédiat page par page.
  - Consultation dans la visionneuse HD ou agrandissement plein écran dans la lightbox.
  - **Liaison Immédiate avec le Chatbot** : Un clic sur **« 💬 Résoudre avec le Prof »** transmet la page avec ses énoncés et figures directement dans la conversation.
* **Création Manuelle de Feuilles de TD** :
  - Bouton `+ Ajouter Manuellement` pour taper ses énoncés en $\LaTeX$.

---

### 📅 Module 4 : Programmes de Révision (Onglet Dédié)
* **Objectif** : Transformer les cours et TD enregistrés en une feuille de route d'assimilation méthodique (préparation de partiels, concours ou entretiens quantitatifs).
* **Composants** :
  - Programme de révision par semaine ou par bloc thématique.
  - Suivi d'état : *À travailler* / *En cours d'assimilation* / *Maîtrisé*.
  - Génération automatique du programme dès que l'étudiant ajoute ses cours.

---

### ☁️ Module 5 : Persistance & Synchronisation Cloud Supabase
* **Technologie** : Base de données Cloud PostgreSQL Supabase (Projet dédié `teacher`).
* **Clé de synchronisation** : Clé privée de l'étudiant (défaut `warm1t`).
* **Sauvegarde Silencieuse** : Tout ajout de cours, de TD ou de message dans le chat est immédiatement persisté en local (`localStorage`) et synchronisé sur le projet Supabase teacher pour un accès multi-appareils (PC de travail, ordinateur portable, tablette).

---

## 4. Spécifications Graphiques & UI (Blanc / Encre)

* **Couleurs** :
  - Fond principal : `#fbfbf9` (papier d'art / parchemin clair) et `#ffffff` (surfaces d'écriture).
  - Encre : `#18181b` (noir d'encre typographique) et `#52525b` (gris encre estompée pour les métadonnées).
  - Bordures : `#e4e4e7` (lignes très fines de 1px, sobres et précises).
  - Accentuation discrète : `#1e293b` (bleu nuit sobre) et `#047857` (vert validation épuré).
* **Typographie** : Polices de caractères modernes à haute lisibilité, mise en valeur des équations KaTeX comme dans un livre chez Hermann, Springer ou Calvage & Mounet.

---

## 5. Critères d'Acceptation
- [x] Zéro élément ludique (pas d'XP, pas de badges, pas de sons ni confettis).
- [x] Design épuré blanc/encre.
- [x] L'espace est complètement vide par défaut à l'ouverture, prêt à accueillir les vrais cours de l'utilisateur.
- [x] Chatbot spécialisé avec sélection contextuelle du cours et du TD.
- [x] Onglets clairs : Chatbot, Cours, TD, Programmes de Révision.
- [x] Persistance locale et synchronisation Cloud Supabase fonctionnelle.
