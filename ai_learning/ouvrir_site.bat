@echo off
chcp 65001 >nul
title Ouvrir le Hub Vibecoding Mastery
echo ========================================================
echo   🌟 Vibecoding Mastery - Ouverture de la plateforme
echo ========================================================
echo.
python "%~dp0build_site.py"
echo Ouverture de la rétrospective dans votre navigateur par défaut...
start "" "%~dp0index.html#recap-fluent"
exit
