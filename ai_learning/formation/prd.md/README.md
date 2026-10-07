# 📄 Leçon 3 : Le PRD (Product Requirement Document)

> **"1 heure passée sur un bon PRD t'économise 15 heures de code jeté à la poubelle."**  
> Le PRD est le document fondateur de tout projet sérieux. En vibecoding, il sert de « contrat de vérité » pour l'IA.

---

## 1. Pourquoi le PRD est l'arme secrète du Vibecoder ?

Quand un débutant a une idée, son réflexe est souvent d'ouvrir son éditeur et d'écrire : *"Fais-moi une application de gestion de stock pour restaurant"*.
* **Problème :** L'IA va inventer 80 % des règles métier à ta place : quel système d'authentification ? Quelles devises ? Y a-t-il des alertes de péremption ? Qui a le droit de supprimer un stock ?
* **Conséquence :** Après 2 heures de génération de code, rien ne correspond à ce que tu imaginais vraiment, et le projet devient un sac de nœuds.

Le **PRD (Product Requirement Document)** est un document court (1 à 3 pages) en markdown qui fixe les règles du jeu **avant** d'écrire la moindre ligne de code.

---

## 2. Les 7 sections d'un PRD taillé pour l'IA

Un bon PRD destiné à une IA doit contenir :

1. **Pitch & Vision** : Quel problème résout cette application, pour qui, et quelle est la proposition de valeur ?
2. **User Stories (Cas d'usage)** : *"En tant qu'utilisateur, je veux pouvoir..."*
3. **Périmètre (Scope) & Non-Scope** :
   - ✅ Ce que le MVP **doit** faire absolument (indispensable).
   - ❌ Ce qui est **hors-sujet** pour l'instant (ex: pas d'envoi de SMS, pas d'export PDF en v1).
4. **Stack Technique & Choix d'Architecture** :
   - Langages, frameworks, bibliothèques UI, base de données, services tiers (Stripe, Resend, Supabase).
5. **Modèle de Données (Data Schema)** :
   - Les entités (ex: `User`, `Project`, `Task`) et leurs champs clés.
6. **Parcours Utilisateur & Écrans (UI/UX)** :
   - Liste des pages (Accueil, Connexion, Dashboard, Profil) et ce qu'elles contiennent.
7. **Critères d'Acceptation & Cas Limites (Edge Cases)** :
   - Que se passe-t-il si la connexion coupe ? Si l'utilisateur saisit un mot de passe trop court ?

---

## 3. L'astuce pro : Faire écrire le PRD par l'IA (La technique de l'interview)

Tu n'as pas besoin de rédiger tout le document seul à la main ! Tu peux utiliser l'IA comme un Chef de Produit senior qui va t'interviewer.

> **Prompt d'interview à copier :**  
> *"Je veux créer une application de [ton idée en 2 phrases].  
> Agis comme un Product Manager d'élite. Pose-moi 5 questions ciblées, une par une, sur le fonctionnement métier, les utilisateurs cibles, et les contraintes techniques.  
> À la fin de mes réponses, tu me rédigeras un PRD complet au format Markdown prêt pour le développement."*

---

## 4. Comment utiliser ton PRD pendant le développement ?

Une fois ton fichier `PRD.md` placé à la racine de ton projet :
* **Dans tes prompts :** Réfère-toi systématiquement au fichier :  
  `"En te basant sur la section 3 du @PRD.md, créons la première brique..."`
* **Si l'IA s'égare :** Rappelle-lui la source :  
  `"Attention, dans le @PRD.md nous avions convenu que le paiement se ferait via Stripe Checkout et non une intégration custom."`
* **Pour faire le point :**  
  `"Compare le code actuel dans @src avec le @PRD.md et dresse la liste des fonctionnalités restantes pour terminer le MVP."`
