#!/bin/bash
touch $1

#importing colorsheme
colorsheme=()
dir="$(cd $(dirname "$0"); pwd)"
scheme_file="${dir}/schemes/bootstrap.txt"
while read line; 
do colorsheme+=($line)
done<$scheme_file


echo "\documentclass[a4paper, 14pt]{article}" > $1
echo "\usepackage[dvipsnames]{xcolor}" >> $1
echo "\usepackage[top=70pt,bottom=70pt,left=48pt,right=46pt]{geometry}" >> $1
echo "\definecolor{header}{RGB}{${colorsheme[1]}}" >> $1
echo "\definecolor{defenition}{RGB}{${colorsheme[3]}}" >> $1
echo "\definecolor{main_title}{RGB}{${colorsheme[0]}}" >> $1
echo "\definecolor{sub_header}{RGB}{${colorsheme[2]}}" >> $1
echo "\usepackage[english, russian]{babel}" >> $1
echo "\usepackage[utf8]{inputenc}" >> $1
echo "\usepackage{amsmath}" >> $1
echo "\usepackage{listings}" >> $1
echo "\usepackage{graphicx}" >> $1
echo "\usepackage{amsmath}" >> $1

echo -e "Название работы: \c"
read work_name
echo "\title{\textcolor{main_title}{${work_name}}}" >> $1

echo "\author{Шмаков Владимир Евгеньевич - ФФКЭ гр. Б04-105}" >> $1
echo "" >> $1
echo "" >> $1
echo "" >> $1
echo "" >> $1
echo "" >> $1
echo "" >> $1
echo "\begin{document}" >> $1

echo "\maketitle" >> $1
echo "" >> $1
echo "" >> $1
echo "" >> $1
echo "\section*{\textcolor{header}{Цель работы}}" >> $1
echo "" >> $1
echo "" >> $1
echo "" >> $1
echo "\section*{\textcolor{header}{Теоретические сведения}}" >> $1
echo "Число A называется \textcolor{defenition}{пределом числовой последовательности}..." >> $1
echo "" >> $1
echo "" >> $1
echo "" >> $1
echo "\section*{\textcolor{header}{Методика}}" >> $1
echo "\subsection*{\textcolor{sub_header}{Оборудование}}" >> $1
echo "" >> $1
echo "" >> $1
echo "" >> $1
echo "\subsection*{\textcolor{sub_header}{Экспериментальная установка}}" >> $1
echo "" >> $1
echo "" >> $1
echo "" >> $1
echo "\section*{\textcolor{header}{Обработка экспериментальных данных}}" >> $1
echo "" >> $1
echo "" >> $1
echo "" >> $1
echo "\section*{\textcolor{header}{Вывод}}" >> $1
echo "" >> $1
echo "" >> $1
echo "" >> $1
echo "" >> $1
echo "" >> $1
echo "" >> $1


echo "\end{document}" >> $1

iconv -f UTF-8 $1 > out.tex
rm $1
mv out.tex $1
