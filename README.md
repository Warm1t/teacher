# 🏛️ MATHS MASTER : L'Assistant Pédagogique d'Élite pour Écoles d'Ingénieurs

> **Environnement de travail épuré Blanc / Encre**  
> *Un chatbot spécialisé en mathématiques supérieures, adossé à vos dossiers de cours et feuilles de TD classés, avec un planificateur de révisions dédié.*

---

## 🎯 Philosophie & Conception

1. **Visuel Blanc & Encre** : Un environnement de travail sobre, calme et académique (fond papier, typographie noire d'imprimerie, zéro distraction visuelle).
2. **Zéro Gamification** : Aucune fioriture superficielle (pas d'XP, pas de badges). L'accent est mis à 100 % sur la rigueur conceptuelle, l'élégance de la démonstration et la maîtrise des outils de l'ingénieur.
3. **Espace Vierge à l'Ouverture** : L'application démarre **entièrement vide**. C'est votre classeur : vous y insérez vos propres polycopiés de cours et vos énoncés de TD.
4. **Chatbot Spécialisé** : Le tuteur IA adapte ses explications et ses corrections au **cours que vous activez**, en appliquant rigoureusement vos théorèmes et vos notations.

---

## 🧭 Les Espaces de Travail

* 💬 **Chatbot Spécialisé** : Dialogue avec le professeur d'élite, guidage socratique pas-à-pas, analyse rigoureuse de vos démarches, affichage des pages PDF sous forme d'images haute résolution et rendu $\LaTeX$ (KaTeX).
* 📚 **Dossiers de Cours** : Classement par matières et chapitres de vos notes théoriques, avec **rendu visuel fidèle des polycopiés PDF (Canvas)** pour préserver à 100 % les intégrales, matrices, tenseurs et schémas géométriques.
* 📝 **Dossiers de TD & Exercices** : Vos feuilles de TD triées en rendu visuel page par page, reliées directement au cours pour être résolues avec l'assistant.
* 📑 **Fiches & Exercices-Types Canoniques** : Résumés des pivots théoriques et exercices modèles corrigés adossés à vos cours, avec réflexes de concours et bouton d'archivage direct depuis le chat.
* 👁️ **Visionneuse Visuelle HD de Documents** : Modale intégrée pour feuilleter vos polycopiés page par page et envoyer une page précise au tuteur en un clic.
* 📄 **Glisser-Déposer (Drag & Drop) de PDF** : Déposez n'importe quel polycopié ou feuille d'exercices PDF sur la page pour rendu visuel et intégration instantanés.
* 💾 **Stockage Local HD (IndexedDB)** : Sauvegarde sans quota de polycopiés volumineux dans le navigateur.
* 📅 **Programmes de Révision** : Onglet dédié pour planifier votre assimilation en vue des partiels et concours.
* ☁️ **Cloud Supabase** : Synchronisation configurable avec votre projet dédié (projet `teacher`).

---

## 🚀 Accès & Démarrage

* **Accès Web Local** : [http://localhost:8080/](http://localhost:8080/)
* **Lancement Rapide** : Double-cliquez sur [`lancer_serveur.bat`](file:///d:/vibecode/maths%20master/lancer_serveur.bat) (démarre le serveur local et ouvre le navigateur).
* **Fichier Autonome** : Vous pouvez également ouvrir [`index.html`](file:///d:/vibecode/maths%20master/index.html) directement.

---

## 📁 Architecture des Fichiers

```
d:\vibecode\maths master\
├── 📄 PRD.md                 # Cahier des charges du chatbot et de l'architecture blanc/encre
├── 📄 README.md            # Présentation générale du projet
├── 📄 index.html             # Application web complète (Blanc / Encre + KaTeX + PDF + Supabase)
├── 📄 lancer_serveur.bat     # Serveur local sur le port 8080
├── 📄 supabase_setup.sql     # Script SQL pour votre projet Supabase "teacher"
└── 📁 ai_learning/           # Référentiel de formation et méthode vibecoding
```
