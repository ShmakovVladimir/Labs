#!/bin/bash
default_name="Очень интересная работа"
template_path="/home/vladimir/BOTAY!/Labs/LaTeX_Template/template/template.tex"
now_path="$(pwd)/$1"
read -p "Текст: " name
cp "$template_path" "$now_path"
sed -i "s/$default_name/$name/g" "$now_path"
