#!/bin/bash
@echo on

#Constants

RED='\033[0;31m'
NC='\033[0m'
search=sktest

#temporary
replace=testname

#Setup

echo "Linux port of DrPvtSkittles' Basic Race Template setup script by Patchouli Fleur"

echo -e "${RED}╔══════════════════════════════════════════════════════╗"
echo          "║IT IS RECOMMENDED TO BACKUP YOUR MOD BEFORE CONTINUING║"
echo -e       "╚══════════════════════════════════════════════════════╝${NC}"

read -p "Enter the race's name: " replace

echo    "╔═════════════════════════════════════════════════════════╗"
echo    "║This could take several minuites depending on your system║"
echo -e "║                ${RED}DO NOT CLOSE THIS WINDOW${NC}                 ║"
echo    "╚═════════════════════════════════════════════════════════╝"

#Actual work

#change what is in files
find . -type f -not -name "*.sh" -not -path '*/\.*' -exec sed -i "s/$search/$replace/g" {} +

#change filenames
find . -type f -name "*$search*" | while read -r file; do
	dir="$(dirname $file)/"
	base="$(basename $file)"
	basereplace=$(echo "$base" | sed "s/$search/$replace/g")
	mv $dir$base $dir$basereplace
done

#change directories
find . -type d -name "*$search*" | while read -r file; do
	dirreplace=$(echo "$file" | sed "s/$search/$replace/g")
	mv $file $dirreplace
done
#change the annoying second level files
find . -type d -name "*$search*" | while read -r file; do
	dirreplace=$(echo "$file" | sed "s/$search/$replace/g")
	mv $file $dirreplace
done
