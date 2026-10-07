"""
LABORATOIRE 01 : Visualisation Dynamique des Transformations Linéaires 2D
MATHS MASTER - Leçons d'Élite pour Écoles d'Ingénieurs

Ce script permet de visualiser comment une matrice 2x2 déforme l'espace vectoriel :
- Rotation pure
- Cisaillement (Shear)
- Dilatation anisotrope (Scaling)
- Projection singulière (det = 0, perte de dimension)
"""

import numpy as np
import matplotlib.pyplot as plt

def creer_grille(lim=2, n_lignes=9):
    """Génère une grille 2D régulière pour observer les déformations."""
    valeurs = np.linspace(-lim, lim, n_lignes)
    lignes_h = []
    lignes_v = []
    
    # Lignes horizontales
    for y in valeurs:
        xs = np.linspace(-lim, lim, 100)
        ys = np.full_like(xs, y)
        lignes_h.append(np.vstack([xs, ys]))
        
    # Lignes verticales
    for x in valeurs:
        ys = np.linspace(-lim, lim, 100)
        xs = np.full_like(ys, x)
        lignes_v.append(np.vstack([xs, ys]))
        
    return lignes_h, lignes_v

def transformer_et_afficher(M, nom_transformation="Transformation"):
    """
    Affiche côte-à-côte l'espace initial et l'espace transformé par la matrice M.
    """
    lignes_h, lignes_v = creer_grille(lim=2, n_lignes=9)
    det = np.linalg.det(M)
    
    fig, (ax_in, ax_out) = plt.subplots(1, 2, figsize=(13, 6))
    fig.suptitle(f"Transformation : {nom_transformation} | det(M) = {det:.2f}", fontsize=14, fontweight='bold')
    
    # --- Espace Initial ---
    for lh in lignes_h:
        ax_in.plot(lh[0], lh[1], color='#cccccc', linewidth=1)
    for lv in lignes_v:
        ax_in.plot(lv[0], lv[1], color='#cccccc', linewidth=1)
        
    ax_in.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    ax_in.axvline(0, color='gray', linestyle='--', linewidth=0.8)
    
    # Vecteurs de base i et j
    ax_in.quiver(0, 0, 1, 0, angles='xy', scale_units='xy', scale=1, color='#1f77b4', linewidth=3, label=r'$\hat{i} = [1, 0]^T$')
    ax_in.quiver(0, 0, 0, 1, angles='xy', scale_units='xy', scale=1, color='#d62728', linewidth=3, label=r'$\hat{j} = [0, 1]^T$')
    
    ax_in.set_title(r"Espace Initial $\mathbb{R}^2$")
    ax_in.set_xlim(-4, 4)
    ax_in.set_ylim(-4, 4)
    ax_in.set_aspect('equal')
    ax_in.grid(True, linestyle=':', alpha=0.6)
    ax_in.legend(loc='upper left')

    # --- Espace Transformé par M ---
    for lh in lignes_h:
        lh_trans = M @ lh
        ax_out.plot(lh_trans[0], lh_trans[1], color='#3b82f6', linewidth=1, alpha=0.7)
    for lv in lignes_v:
        lv_trans = M @ lv
        ax_out.plot(lv_trans[0], lv_trans[1], color='#3b82f6', linewidth=1, alpha=0.7)
        
    ax_out.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    ax_out.axvline(0, color='gray', linestyle='--', linewidth=0.8)
    
    # Vecteurs images = colonnes de M
    col1 = M[:, 0]
    col2 = M[:, 1]
    ax_out.quiver(0, 0, col1[0], col1[1], angles='xy', scale_units='xy', scale=1, 
                  color='#1f77b4', linewidth=3, label=f'$M\\hat{{i}} = [{col1[0]:.1f}, {col1[1]:.1f}]^T$')
    ax_out.quiver(0, 0, col2[0], col2[1], angles='xy', scale_units='xy', scale=1, 
                  color='#d62728', linewidth=3, label=f'$M\\hat{{j}} = [{col2[0]:.1f}, {col2[1]:.1f}]^T$')
    
    ax_out.set_title(f"Espace Déformé (Aire relative = {abs(det):.2f})")
    ax_out.set_xlim(-4, 4)
    ax_out.set_ylim(-4, 4)
    ax_out.set_aspect('equal')
    ax_out.grid(True, linestyle=':', alpha=0.6)
    ax_out.legend(loc='upper left')
    
    plt.tight_layout()
    # Sauvegarde de la figure pour consultation immédiate
    output_path = "d:/vibecode/maths master/labs_python/demo_transformation_2d.png"
    plt.savefig(output_path, dpi=150)
    print(f"Visualisation générée avec succès dans : {output_path}")
    plt.close()

if __name__ == "__main__":
    print("=" * 60)
    print("MATHS MASTER : Laboratoire 01 - Déformation Matricielle 2D")
    print("=" * 60)
    
    # Exemple 1 : Cisaillement (Shear) + Dilatation
    M_shear = np.array([
        [1.2, 1.0],
        [0.3, 1.1]
    ])
    
    transformer_et_afficher(M_shear, nom_transformation="Cisaillement & Étalement")
    
    print("\n[Explication du Maître]")
    print(f"- Colonne 1 de M = {M_shear[:, 0]} : c'est l'atterrissage du vecteur i.")
    print(f"- Colonne 2 de M = {M_shear[:, 1]} : c'est l'atterrissage du vecteur j.")
    print(f"- Déterminant = {np.linalg.det(M_shear):.4f} : chaque surface unitaire est multipliée par ce ratio.")
    print("=" * 60)
