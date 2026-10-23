@echo off
rem Compile le poly SANS la partie "Corrections des exercices" (ni les renvois "Solution p. x")
rem Produit poly_sans_corrections.pdf a cote de poly.pdf. Usage : double-clic ou  poly_sans_corrections.bat
cd /d "%~dp0"
latexmk -pdf -interaction=nonstopmode -jobname=poly_sans_corrections -usepretex="\def\sanscorrections{1}" poly.tex
