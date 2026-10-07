@echo off
chcp 65001 > nul
title Maths Master Cockpit - Lancement

echo ========================================================
echo   ⚡ MATHS MASTER : L'Agent Professeur d'Élite
echo ========================================================
echo.
echo Ouverture de votre Cockpit interactif dans votre navigateur...
echo.

start "" "%~dp0index.html"

echo Cockpit lancé avec succès !
timeout /t 3 > nul
exit
