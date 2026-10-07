@echo off
chcp 65001 > nul
title Serveur Local & Cloud Supabase - Maths Master Cockpit

echo ======================================================================
echo          ⚡ MATHS MASTER : SERVEUR LOCAL & CLOUD SUPABASE
echo ======================================================================
echo.
echo [1/2] Démarrage du serveur Web sur http://localhost:8080 ...
echo [2/2] Connexion configurable au Cloud Supabase (Projet: Teacher)...
echo.
echo [INFO] Votre navigateur va s'ouvrir sur http://localhost:8080
echo [INFO] Gardez cette fenêtre ouverte pour maintenir le serveur actif.
echo [INFO] Pour fermer le serveur : fermez cette fenêtre ou faites Ctrl+C.
echo ======================================================================
echo.

:: Ouvre le navigateur sur le serveur local
start http://localhost:8080

:: Lance le serveur Python dans le dossier courant
python -m http.server 8080 --directory "%~dp0"

pause
