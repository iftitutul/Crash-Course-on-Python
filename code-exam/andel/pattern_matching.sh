#!/usr/bin/env bash

my_array=["Abc","Ccd","Efg","def","cDe"]
#readarray -t my_array </dev/stdin

# Input array is read and stored in to my_array variable. 
# You can view the code by pressing > button above. 

function match_uppercase() {
  typeset -a data=("$@")
  # Write your code here
  let count=0
  for x in ${my_array[*]}; do
    if [[ $x =~ [A-Z] ]]
    then 
        count=$((count+1))
    fi
  done  
}


match_uppercase "${my_array[@]}"
echo $count
exit 0