-- ========================================================
-- ⚡ MATHS MASTER : SCRIPT SQL SUPABASE (PROJET TEACHER)
-- ========================================================
-- Copiez et collez ce script dans l'éditeur SQL de votre projet Supabase "teacher" :
-- Dashboard Supabase > Projet Teacher > SQL Editor > New query

-- 1. Création de la table dédiée maths_master_profiles
CREATE TABLE IF NOT EXISTS public.maths_master_profiles (
  user_id TEXT PRIMARY KEY,
  data JSONB NOT NULL DEFAULT '{}'::jsonb,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 2. Activation de la sécurité au niveau des lignes (RLS)
ALTER TABLE public.maths_master_profiles ENABLE ROW LEVEL SECURITY;

-- 3. Politique pour autoriser la lecture et l'écriture avec la clé anonyme (basée sur user_id)
DROP POLICY IF EXISTS "Accès public par user_id" ON public.maths_master_profiles;
CREATE POLICY "Accès public par user_id" ON public.maths_master_profiles
  FOR ALL
  USING (true)
  WITH CHECK (true);

-- 4. Commentaires explicatifs
COMMENT ON TABLE public.maths_master_profiles IS 'Stocke les cours, feuilles de TD, programmes de révision et conversations du projet Maths Master';
