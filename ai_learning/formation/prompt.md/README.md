# ✍️ Leçon 2 : L'Art du Prompting pour le Code & les Agents

> **"Un bon prompt donne un code parfait. Un mauvais prompt donne 3 heures de débogage."**  
> En vibecoding, ton prompt est ton code source. Cette leçon t'apprend la méthodologie exacte pour obtenir des réponses ultra-précises dès le premier coup.

---

## 1. La formule C.O.C.O.A (L'Anatomie du Prompt Parfait)

Chaque fois que tu formules une demande complexe à un agent ou un modèle, structure ta pensée avec ces 5 composantes :

| Élément | Signification | Exemple concret |
| :--- | :--- | :--- |
| **C - Contexte** | Quel est le projet, la stack et l'état actuel ? | *"Je développe une application React + Tailwind avec backend FastAPI..."* |
| **O - Objectif** | Que veux-tu accomplir exactement ? | *"Ajouter un composant de carte produit interactif..."* |
| **C - Contraintes** | Quelles sont les règles à respecter absolument ? | *"Ne modifie pas l'API existante, utilise Lucide Icons, design responsive mobile-first."* |
| **O - Output** | Quel format de réponse ou modification attends-tu ? | *"Crée un fichier `ProductCard.tsx` et mets à jour `ProductList.tsx`."* |
| **A - Acceptation** | Comment sauras-tu que c'est réussi (critères) ? | *"Au clic sur le bouton, une notification toast s'affiche et le panier s'incrémente."* |

---

## 2. Le Workflow de Contexte avec `@`

Ne colle pas des milliers de lignes de code manuellement dans le chat. Utilise les symboles de ciblage :
* **`@nom-du-fichier`** : Injecte le contenu exact du fichier dans le contexte de l'agent.
* **`@dossier`** : Permet à l'agent d'avoir une vision d'ensemble de l'arborescence.
* **`@git`** : Donne à l'agent le contexte des derniers commits ou des fichiers modifiés.
* **`@docs` ou `@url`** : Permet à l'agent de lire la documentation officielle d'une librairie au lieu d'inventer des fonctions qui n'existent pas.

> **Règle essentielle :** Donne uniquement les fichiers pertinents. Trop de contexte dilue l'attention de l'IA (ce qu'on appelle la *pollution de contexte*).

---

## 3. Les 4 Modes de Prompting Indispensables

### A. Le mode "Plan d'abord, Code ensuite" (Plan-and-Execute)
Avant d'écrire une seule ligne de code pour une grosse fonctionnalité :
> **Prompt type :** *"Ne commence pas à écrire de code tout de suite. Analyse mon code actuel dans `@src` et propose un plan étape par étape en 4 ou 5 étapes pour implémenter l'authentification avec Supabase. Attends ma validation avant de commencer."*

### B. Le protocole de débogage (One-Shot Debugging)
Quand une erreur survient, applique ce modèle strict :
```markdown
J'ai rencontré une erreur lors de l'exécution de la commande : `npm run dev`

1. Ce que j'essayais de faire : Lancer le serveur local après avoir ajouté `@src/auth.ts`.
2. L'erreur complète obtenue :
```
[Coller l'erreur brute complète ici, sans couper la stack trace]
```
3. Fichiers modifiés récemment : `@src/auth.ts`, `@src/App.tsx`.

Analyse la cause racine et propose la correction minimale nécessaire.
```

### C. Le mode "Refactor & Clean"
Pour garder une base de code propre que n'importe qui peut maintenir :
> **Prompt type :** *"Passe en revue `@src/components/Dashboard.tsx`. Découpe ce composant de 300 lignes en 3 sous-composants réutilisables plus petits dans le dossier `components/dashboard/`. Assure-toi que les props sont typées en TypeScript et conserve exactement le même comportement visuel."*

### D. Le mode "Documentation & Explication" (Pour apprendre)
Le vibecoding n'est pas seulement fait pour aller vite, c'est aussi un accélérateur d'apprentissage incroyable :
> **Prompt type :** *"Explique-moi pas à pas comment fonctionne la fonction `useCartStore` dans `@src/store.ts`. Utilise une analogie simple de la vie courante et détaille le rôle de chaque hook utilisé."*

---

## 4. Ce qu'il ne faut JAMAIS faire

❌ *"Fais marcher ça"* (Sans fournir ni l'erreur ni le comportement attendu)  
❌ *"Ajoute une IA à mon site"* (Beaucoup trop flou)  
❌ Donner une capture d'écran d'un paragraphe d'erreur au lieu de copier-coller le texte (le texte permet la recherche exacte de symboles)  
❌ Valider du code que tu n'as pas vu s'exécuter localement au moins une fois
