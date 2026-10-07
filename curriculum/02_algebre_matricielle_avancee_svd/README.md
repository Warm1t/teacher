# 🧬 Pilier 2, Leçon 1 : La SVD (Singular Value Decomposition)
## *L'Autopsie Universelle de n'importe quelle Matrice & La Réduction de Dimension*

> *"Si vous ne devez retenir qu'un seul théorème d'algèbre linéaire pour votre carrière d'ingénieur, que ce soit la SVD. Elle est la radiographie complète des matrices rectangulaires."*  
> — Le Professeur

---

## 📑 Sommaire
1. [L'Étincelle Intuitive : Pourquoi la diagonalisation $P D P^{-1}$ échoue dans la vraie vie](#1-létincelle-intuitive)
2. [Lentille 1 (Géométrie) : Le Théorème du Cercle et de l'Ellipse](#2-lentille-1-géométrie)
3. [Lentille 2 (Ingénierie) : Compression d'images, PCA & Modèles de Langage](#3-lentille-2-ingénierie)
4. [Lentille 3 (Code Python) : La SVD from Scratch avec NumPy](#4-lentille-3-code-python)
5. [Lentille 4 (Preuve Épurée) : Pourquoi les matrices $A^T A$ et $A A^T$ ont la clé](#5-lentille-4-preuve-épurée)

---

## 1. L'Étincelle Intuitive

En prépa, on passe des mois sur la diagonalisation :
$$A = P D P^{-1}$$
Mais dans la réalité industrielle, la diagonalisation a deux défauts majeurs :
1. Elle n'existe que pour les **matrices carrées** ($n \times n$). Or, un dataset de données est presque toujours **rectangle** ($m$ lignes d'échantillons $\times$ $n$ variables).
2. Même pour une matrice carrée, elle peut échouer si la matrice n'a pas assez de vecteurs propres indépendants (matrices non diagonalisables) ou si les vecteurs propres ne sont pas orthogonaux.

La **SVD** résout ce problème de manière magistrale. **Elle fonctionne pour TOUTE matrice, carrée ou rectangle, sans aucune exception.**

---

## 2. 👁️ Lentille 1 (Géométrie) : Le Théorème du Cercle et de l'Ellipse

Prenez le cercle unité dans $\mathbb{R}^2$ :
$$\{\vec{x} \in \mathbb{R}^2 \mid \|\vec{x}\| = 1\}$$
Appliquez n'importe quelle matrice $A \in \mathbb{R}^{2 \times 2}$. Le cercle est transformé en une **ellipse** !

```
     Espace de départ X                          Espace d'arrivée Y
    ┌──────────────────┐                        ┌──────────────────┐
    │        ▲         │                        │        ▲         │
    │        │ v2      │      Matrice A         │        │    u2   │
    │   ╭────┼────╮    │   ───────────────>     │     ╭──┼───╮     │  σ2
    │───┼────┼────┼───>│                        │─────┼──┼───┼────>│
    │   ╰────┼────╯    │                        │  u1 ╰──┼───╯     │  σ1
    │        │   v1    │                        │        ▼         │
    └──────────────────┘                        └──────────────────┘
     Cercle unité                                Ellipse orientée
     Base orthonormée V                          Axes principaux U, dilatés par Σ
```

La décomposition SVD traduit cette observation géométrique en équation :
$$A = U \Sigma V^T$$

1. $V^T$ effectue une **rotation** de l'espace de départ pour aligner les axes sur les directions optimales $\vec{v}_1, \vec{v}_2$.
2. $\Sigma$ effectue un **étirement** le long de ces axes par des facteurs $\sigma_1, \sigma_2 \ge 0$ (les valeurs singulières).
3. $U$ effectue une dernière **rotation** dans l'espace d'arrivée pour orienter les demi-axes de l'ellipse le long de $\vec{u}_1, \vec{u}_2$.

---

## 3. ⚙️ Lentille 2 (Ingénierie) : Les Moindres Carrés & Compression

### Théorème d'Eckart-Young (1936) :
Si vous voulez compresser une matrice de données géante $A \in \mathbb{R}^{m \times n}$ en ne conservant que $k$ termes ($k \ll \min(m, n)$), la meilleure matrice de rang $k$ au monde est donnée par la somme tronquée :
$$A_k = \sum_{i=1}^k \sigma_i \vec{u}_i \vec{v}_i^T$$

* **En compression JPEG / Image** : Une photo $1000 \times 1000$ contient 1 000 000 de coefficients. Avec les 30 premières valeurs singulières ($k=30$), on ne stocke que $(1000 \times 30) + 30 + (30 \times 1000) = 60\,030$ nombres (une réduction de 94 % du poids !) tout en conservant les traits visuels principaux.
* **En IA & NLP (Embeddings & LSA)** : C'est la SVD qui a fondé l'analyse sémantique latente (découverte automatique de thèmes dans des millions de textes).

---

## 4. 💻 Lentille 3 (Code Python : Démonstration Numérique)

```python
import numpy as np

# Matrice rectangulaire quelconque (3 mesures sur 2 capteurs)
A = np.array([
    [3.0, 1.0],
    [1.0, 3.0],
    [1.0, 1.0]
])

# Calcul direct de la SVD
U, s, Vt = np.linalg.svd(A, full_matrices=False)
Sigma = np.diag(s)

print("Matrice U (Colonnes orthonormées) :\n", U)
print("Valeurs singulières Sigma :\n", s)
print("Matrice V^T (Lignes orthonormées) :\n", Vt)

# Reconstruction exacte A = U @ Sigma @ Vt
A_reconstruite = U @ Sigma @ Vt
print("\nErreur de reconstruction :", np.linalg.norm(A - A_reconstruite))
```

---

## 5. 📐 Lentille 4 (Preuve Épurée en 4 Lignes)

1. Pour toute matrice $A \in \mathbb{R}^{m \times n}$, la matrice carrée $S = A^T A \in \mathbb{R}^{n \times n}$ est **symétrique** et **semi-définie positive** ($S^T = S$ et $\vec{x}^T S \vec{x} = \|A\vec{x}\|^2 \ge 0$).
2. Par le théorème spectral, $A^TA$ admet une base orthonormale de vecteurs propres $\vec{v}_1, \dots, \vec{v}_n$ associés à des valeurs propres réelles positives $\lambda_i \ge 0$.
3. On pose $\sigma_i = \sqrt{\lambda_i}$. Pour chaque $\sigma_i > 0$, on définit le vecteur unitaire d'arrivée :
   $$\vec{u}_i = \frac{1}{\sigma_i} A \vec{v}_i$$
4. On vérifie immédiatement que la famille des $\vec{u}_i$ est orthonormée :
   $$\vec{u}_i^T \vec{u}_j = \frac{1}{\sigma_i \sigma_j} \vec{v}_i^T A^T A \vec{v}_j = \frac{1}{\sigma_i \sigma_j} \vec{v}_i^T (\lambda_j \vec{v}_j) = \frac{\lambda_j}{\sigma_i \sigma_j} \delta_{ij} = \delta_{ij}$$
5. En assemblant les matrices sous forme matricielle : $A V = U \Sigma \implies A = U \Sigma V^T$. **C.Q.F.D.**
