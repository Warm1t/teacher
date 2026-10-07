# 📚 Bibliothèque de Prompts Prêts à l'Emploi

> Copie, personnalise et colle ces prompts directement dans ton agent pour gagner un temps précieux.

---

### 1. Initialisation d'un nouveau projet
```markdown
Agis comme un Tech Lead Fullstack expérimenté. 
Je souhaite créer une application web appelée "[Nom du projet]".
Objectif du projet : [Ex: Plateforme de réservation de cours de guitare pour débutants].

Voici la stack technique souhaitée :
- Frontend : Vite + React + TypeScript + Tailwind CSS
- Icônes : Lucide-React
- State Management : Zustand (ou React Context si simple)

Étape 1 : Donne-moi les commandes exactes à lancer dans mon terminal pour initialiser ce projet avec une structure de dossiers propre (`src/components`, `src/pages`, `src/hooks`, `src/types`).
Ne génère pas encore de code complexe, préparons d'abord la base.
```

---

### 2. Ajout d'une fonctionnalité isolée
```markdown
En te basant sur le fichier `@src/pages/Dashboard.tsx` et sur les types dans `@src/types/index.ts` :

Je souhaite ajouter la fonctionnalité suivante :
- Créer un composant modal de confirmation de suppression (`DeleteConfirmModal.tsx`).
- Le composant doit recevoir en props : `isOpen`, `onClose`, `onConfirm`, `itemName`.
- Style : Utilise Tailwind CSS avec un fond sombre translucide (`bg-black/50`), des coins arrondis (`rounded-xl`), et un bouton rouge d'action.
- Accessibilité : La touche Echap (`Escape`) doit fermer la modale.

Crée uniquement le fichier nécessaire et montre-moi comment l'importer dans le Dashboard.
```

---

### 3. Résolution d'un bug complexe (Mode Enquête)
```markdown
J'ai un comportement anormal dans l'application :
- Comportement attendu : [Ex: Quand l'utilisateur clique sur "Valider", les données doivent être envoyées à l'API et l'utilisateur redirigé vers `/merci`].
- Comportement réel observé : [Ex: Le bouton charge indéfiniment et aucune requête réseau n'apparaît dans l'onglet Network].
- Fichiers concernés : `@src/components/CheckoutForm.tsx` et `@src/services/api.ts`.
- Logs / Console : [Coller les éventuelles erreurs ici].

Ne réécris pas tout le code à l'aveugle. 
1. Formule d'abord une hypothèse sur l'origine du blocage.
2. Propose des instructions de débogage (ex: `console.log` stratégiques) ou le correctif direct si la cause est évidente.
```

---

### 4. Revue de code & Sécurité avant livraison client
```markdown
Agis comme un auditeur de code senior. 
Fais une revue critique du code situé dans `@src/api/payment.ts`.

Vérifie spécifiquement :
1. Y a-t-il des failles de sécurité potentielles (injections, clés API exposées côté client) ?
2. La gestion des erreurs (`try/catch`) est-elle exhaustive pour éviter que l'application ne crash ?
3. Le code respecte-t-il les bonnes pratiques TypeScript (pas de `any` injustifié) ?
4. Liste les 3 améliorations prioritaires sous forme de bullet points.
```

---

### 5. Conception du Schéma de Base de Données
```markdown
Je conçois la base de données relationnelle pour [Description de l'application].
Entités principales :
- Utilisateurs (Clients / Prestataires)
- Réservations
- Avis / Commentaires

Génère le schéma SQL (compatible PostgreSQL / Supabase) avec :
- Clés primaires UUID
- Relations avec clés étrangères et `ON DELETE CASCADE` approprié
- Index sur les colonnes fréquemment recherchées
- Row Level Security (RLS) de base si pertinent
```
