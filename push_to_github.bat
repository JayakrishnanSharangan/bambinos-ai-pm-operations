@echo off
echo ========================================================
echo   Bambinos.live AI PM Operations - Push to GitHub
echo ========================================================
echo.

set /p REPO_URL="Enter your GitHub Repository URL (e.g. https://github.com/username/bambinos-ops.git): "

if "%REPO_URL%"=="" (
    echo Error: No repository URL provided.
    pause
    exit /b
)

echo.
echo Adding remote origin: %REPO_URL%
git remote remove origin 2>nul
git remote add origin %REPO_URL%
git branch -M main

echo.
echo Pushing to GitHub main branch...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================================
    echo   SUCCESS! Your repository is now live on GitHub.
    echo   You can now submit your link to the Google Form!
    echo ========================================================
) else (
    echo.
    echo PUSH FAILED. Please ensure you are authenticated or check your URL.
)

echo.
pause

