@echo off
setlocal

del "dist\LBCutter.exe"
pyinstaller --onefile --icon=appicon.ico LBCutter.py

echo Creating folder...

:: Get the current date in the format YYYY-MM-DD
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value ^| find "="') do set "currentDate=%%I"
set "formattedDate=%currentDate:~0,4%-%currentDate:~4,2%-%currentDate:~6,2%"

:: Set the name of the folder
set "folderName=LBCutter_%formattedDate%"

:: Create the folder
mkdir "%folderName%"

:: Copy the files to the new folder
copy "emptybar.png" "%folderName%"
copy "extrabar.png" "%folderName%"
copy "lifebar.png" "%folderName%"
copy "playerbar.png" "%folderName%"
mkdir "%folderName%\names"
copy "names\*.png" "%folderName%\names"
copy "Readme.md" "%folderName%\Readme.txt"
copy "dist\LBCutter.exe" "%folderName%"

echo Creating zip file...

:: Check if 7-Zip is intalled in the PATH variable
where 7z >nul 2>nul
if errorlevel 1 (
    echo 7-Zip is not installed in your PATH. Please, install 7-Zip and add it to your PATH.
    exit /b
)

:: Compress the folder in a zip file withe today's date
7z a "%folderName%.zip" "%folderName%\*"

:: Erase the created folder (optional)
rmdir /s /q "%folderName%"

echo zip file sucessfully created: %folderName%.zip
endlocal
