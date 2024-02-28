#!/bin/bash
touch $1
echo "\documentclass[a4paper]{article}" > $1
echo "\usepackage[dvipsnames]{xcolor}" >> $1
echo "\usepackage[top=70pt,bottom=70pt,left=48pt,right=46pt]{geometry}" >> $1
echo "\definecolor{header}{RGB}{254, 100, 11}" >> $1
echo "\definecolor{defenition}{RGB}{136, 57, 239}" >> $1
echo "\definecolor{main_title}{RGB}{30, 102, 245}" >> $1
echo "\definecolor{sub_header}{RGB}{32, 159, 181}" >> $1
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
echo "" >> $1
echo "" >> $1
echo "" >> $1
echo "\section*{\textcolor{header}{Методика}}" >> $1
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
