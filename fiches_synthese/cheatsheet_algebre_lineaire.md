# ⚡ Fiche de Synthèse d'Élite : Algèbre Linéaire & Géométrie Matricielle
> *À conserver précieusement — Les 10 axiomes et théorèmes fondamentaux de l'ingénieur.*

---

## 1. La Transformation Matricielle
Toute matrice $A \in \mathbb{R}^{m \times n}$ représente une application linéaire de $\mathbb{R}^n$ vers $\mathbb{R}^m$.
* **Les colonnes de $A$** sont les images des vecteurs de la base canonique : $A\hat{e}_j = \text{Col}_j(A)$.
* **L'image $\text{Im}(A)$** est l'espace engendré par les colonnes de $A$ (Column Space).
* **Le noyau $\ker(A)$** est l'ensemble des vecteurs annulés par $A$ : $\{\vec{x} \in \mathbb{R}^n \mid A\vec{x} = \vec{0}\}$.

---

## 2. Le Théorème Fondamental de l'Algèbre Linéaire (Les 4 Sous-Espaces de Strang)
Pour toute matrice $A \in \mathbb{R}^{m \times n}$ de rang $r$ :

| Sous-espace | Notation | Dimension | Espace ambiant | Orthogonal à |
| :--- | :--- | :---: | :---: | :--- |
| **Espace des Colonnes** | $\mathcal{C}(A) = \text{Im}(A)$ | $r$ | $\mathbb{R}^m$ | Espace à gauche du noyau $\mathcal{N}(A^T)$ |
| **Espace des Lignes** | $\mathcal{C}(A^T) = \text{Row}(A)$ | $r$ | $\mathbb{R}^n$ | Noyau $\mathcal{N}(A)$ |
| **Noyau** | $\mathcal{N}(A) = \ker(A)$ | $n - r$ | $\mathbb{R}^n$ | Espace des lignes $\mathcal{C}(A^T)$ |
| **Noyau Gauche** | $\mathcal{N}(A^T) = \ker(A^T)$ | $m - r$ | $\mathbb{R}^m$ | Espace des colonnes $\mathcal{C}(A)$ |

$$\mathbb{R}^n = \mathcal{C}(A^T) \oplus \mathcal{N}(A) \quad \text{et} \quad \mathbb{R}^m = \mathcal{C}(A) \oplus \mathcal{N}(A^T)$$

---

## 3. Le Déterminant & La Trace
Pour $A \in \mathbb{R}^{n \times n}$ :
* **$\det(A)$** : Facteur d'amplification de l'hypervolume orienté sous l'effet de $A$.
  - $\det(AB) = \det(A)\det(B)$
  - $\det(A^{-1}) = \frac{1}{\det(A)}$
  - $\det(A) = \prod_{i=1}^n \lambda_i$ (produit des valeurs propres).
* **$\text{Tr}(A)$** : Somme des éléments diagonaux.
  - $\text{Tr}(AB) = \text{Tr}(BA)$ (invariance par permutation cyclique).
  - $\text{Tr}(A) = \sum_{i=1}^n \lambda_i$ (somme des valeurs propres).

---

## 4. Valeurs Propres & Vecteurs Propres
$$A\vec{v} = \lambda \vec{v} \iff (A - \lambda I)\vec{v} = \vec{0}$$
* $\vec{v} \neq \vec{0}$ est une direction invariante : la matrice y agit par simple dilatation scalaire.
* **Théorème Spectral** : Toute matrice symétrique réelle $S = S^T$ admet une base orthonormale de vecteurs propres et toutes ses valeurs propres sont réelles :
  $$S = Q \Lambda Q^T \quad \text{avec } Q^TQ = I$$

---

## 5. La SVD (Singular Value Decomposition)
La reine absolue des factorisations, valable pour **TOUTE** matrice rectangle $A \in \mathbb{R}^{m \times n}$ :
$$A = U \Sigma V^T = \sum_{i=1}^r \sigma_i \vec{u}_i \vec{v}_i^T$$
* $U \in \mathbb{R}^{m \times m}$ : Base orthonormée d'arrivée (vecteurs propres de $AA^T$).
* $V \in \mathbb{R}^{n \times n}$ : Base orthonormée de départ (vecteurs propres de $A^TA$).
* $\Sigma \in \mathbb{R}^{m \times n}$ : Valeurs singulières diagonales ordonnées $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$.
* **Théorème d'Eckart-Young** : La meilleure approximation de rang $k < r$ au sens de la norme de Frobenius est la troncature :
  $$A_k = \sum_{i=1}^k \sigma_i \vec{u}_i \vec{v}_i^T$$
  *(C'est la base de la compression d'images, de la réduction de dimension PCA et des embeddings IA).*
