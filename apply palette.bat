@echo off
:: Write your Irfan View directory bellow. Example: "iview_directory=C:\GAMES\SORRv5.1\tools\IrfanView\i_view32.exe"
set "i_view_directory=PUT THE DIRECTORY HERE"

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:: Checking for needed files.
for %%G in (
	i_view_palette.pal
	%i_view_directory%
) do (
	if not exist "%%G" (
		echo ERROR: file "%%G" not found!
		echo Please, open LBCutter.exe and choose "Generate palette file".
		pause
		exit
	)
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

echo Appling palette...
for %%G in (lifebar, extrabar, emptybar) do (
	if exist "%%G\*.bmp" (
		%i_view_directory%  "%~dp0\%%G\*.bmp" /import_pal="%~dp0\i_view_palette.pal" /transpcolor="None" /convert="%~dp0\%%G\*.bmp"
	)
)
echo DONE!
pause