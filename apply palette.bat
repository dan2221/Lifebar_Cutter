@echo off
:: Write your Irfan View directory bellow. Example: "iview_directory=C:\GAMES\SORRv5.1\tools\IrfanView\i_view32.exe"
set "i_view_directory=PUT THE DIRECTORY HERE"

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:: Checking for the pal file.
if not exist "i_view_palette.pal" (
	echo ERROR: file "i_view_palette.pal" not found!
	echo Please, open LBCutter.exe and choose "Generate palette file".
	pause
	exit
)

:: Checking for I_view directory.
if not exist "%i_view_directory%" (
	echo ERROR: Irfan View directory not found!
	pause
	exit
)

:: Checking for folders.
if not exist "lifebar\*.bmp" (
	if not exist "emptybar\*.bmp" (
		if not exist "extrabar\*.bmp" (
			echo ERROR: BMP files not found in folders "lifebar","emptybar" and "extrabar"!
			pause
			exit
		)
	)
)

for %%G in (lifebar, extrabar, emptybar) do (
	if exist "%%G\*.bmp" (
		echo Appling palette to %%G files...
		%i_view_directory%  "%~dp0\%%G\*.bmp" /import_pal="%~dp0\i_view_palette.pal" /transpcolor="None" /convert="%~dp0\%%G\*.bmp"
	)
)
echo DONE!
pause