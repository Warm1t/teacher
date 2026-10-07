@echo off
chcp 65001 > nul
echo ========================================================
echo   ENVOI VERS GITHUB : REPOSITORY TEACHER
echo ========================================================
echo.
cd /d "%~dp0"

echo Verification du remote origin...
git remote -v
echo.

echo Synchronisation et push vers https://github.com/Warm1t/teacher.git...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================================
    echo   SUCCES : Le projet a ete publie sur GitHub !
    echo   https://github.com/Warm1t/teacher
    echo ========================================================
) else (
    echo.
    echo [INFO] Si une invite d'authentification s'affiche, validez la connexion GitHub dans votre navigateur.
)
echo.
pause
