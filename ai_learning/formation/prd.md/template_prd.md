# 📑 Modèle de PRD (Product Requirement Document)

> *Copie ce fichier dans la racine de ton nouveau projet sous le nom `PRD.md` et remplis chaque section.*

---

## 1. Vue d'ensemble du Projet
* **Nom du Projet** : [Nom de ton app]
* **Pitch en 1 phrase** : [Une description simple et percutante]
* **Public Cible** : [Ex: Développeurs freelances, restaurateurs, étudiants]
* **Problème résolu** : [Quel problème pénible ce produit élimine-t-il ?]

---

## 2. Objectifs & Périmètre (Scope)

### ✅ Inclus dans la V1 (MVP indispensable) :
- [ ] Fonctionnalité 1 (ex: Inscription & Connexion par email)
- [ ] Fonctionnalité 2 (ex: Création et édition d'un élément)
- [ ] Fonctionnalité 3 (ex: Tableau de bord récapitulatif)

### ❌ Exclu de la V1 (Pour plus tard) :
- Système d'abonnement / Facturation
- Thème clair/sombre personnalisable
- Notifications push mobiles
- Internationalisation (multi-langues)

---

## 3. Stack Technique Choisie
* **Frontend** : React / Next.js (App Router), TypeScript
* **Styling & UI** : Tailwind CSS, Lucide Icons, shadcn/ui
* **Backend & API** : Server Actions / Routes API REST
* **Base de données** : PostgreSQL via Supabase (ou SQLite local pour le dev)
* **Authentification** : Supabase Auth (Email / Mot de passe)
* **Hébergement / Déploiement** : Vercel

---

## 4. Modèle de Données (Entities & Schemas)

```typescript
// Exemple de structures attendues :
interface User {
  id: string; // UUID
  email: string;
  name: string;
  createdAt: Date;
}

interface Item {
  id: string;
  userId: string; // Clé étrangère vers User
  title: string;
  status: 'pending' | 'in_progress' | 'completed';
  dueDate?: Date;
}
```

---

## 5. Parcours & Écrans Utilisateur (UI/UX)
1. **Écran d'accueil / Landing (`/`)** : Présentation du service avec un bouton "Commencer".
2. **Page d'authentification (`/login`)** : Formulaire simple (Email, Mot de passe).
3. **Tableau de bord (`/dashboard`)** :
   - Barre latérale avec navigation.
   - Liste des éléments avec filtres (Tous, En cours, Terminés).
   - Bouton flottant pour ajouter un élément via une modale.

---

## 6. Règles Métier & Cas Limites (Edge Cases)
* Un utilisateur ne doit jamais pouvoir voir ou modifier les données d'un autre utilisateur.
* Le formulaire doit refuser les titres de moins de 3 caractères avec un message d'erreur clair.
* En cas d'erreur réseau, afficher une notification toast discrète avec option de réessai.
