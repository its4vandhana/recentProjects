#!/bin/bash
NAMES=( John Eric Jessica )
# write your code here
NUMBERS=(1 2 3)
STRINGS=('hello' 'world')
NumberOfNames=${#NAMES[@]} # returns 3
second_name=${NAMES[${#NAMES[@]}-2]} # retuns 'Eric'
echo $NumberOfNames
echo $second_name