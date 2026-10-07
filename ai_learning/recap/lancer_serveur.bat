@echo off
chcp 65001 >nul
title Serveur Local - Vibecoding Mastery Hub
echo ======================================================================
echo          🚀 VIBECODING MASTERY - SERVEUR LOCAL (PORT 8000)
echo ======================================================================
echo.
echo [1/2] Actualisation automatique des leçons et des rétrospectives...
python "%~dp0build_site.py"
echo.
echo [2/2] Démarrage du serveur sur http://localhost:8000 ...
echo.
echo [INFO] Le site web va s'ouvrir automatiquement dans votre navigateur.
echo [INFO] Gardez cette fenêtre ouverte tant que vous consultez le Hub.
echo [INFO] Pour arrêter le serveur : fermez cette fenêtre ou appuyez sur Ctrl+C.
echo ======================================================================
echo.

:: Ouvre directement la page de la rétrospective du projet Fluent dans le navigateur
start http://localhost:8000#recap-fluent

:: Lance le serveur Python dans le dossier courant
python -m http.server 8000 --directory "%~dp0"

pause
