### print a string to the console
	- ```bash
	  echo "Hello World!"
	  ```
- ### create a new file from the console
	- ```bash
	  touch newFile.txt         # will create a single file
	  touch {1..4}_filename.txt # will create 4 files named i.e. 1_filename.txt
	  ```
- ### print all the contents from a text file into the console
	- ```bash
	  cat newFile.txt
	  ```
- ### get an input from user and store it into a variable
	- ```bash
	  read FIRST_NAME
	  read LAST_NAME
	  echo $FIRST_NAME $LAST_NAME
	  ```
- ### add a positional argument
	- ```bash
	  #!/bin/bash
	  echo Hello $1 $2 $3
	  ```
	- now store this code snippet in a script.sh file
	- execute script file using "sh script.sh Rajib Chandra Das"
	- Output: "Hello Rajib Chandra Das"
- ### list all file in a specific directory, add filtering
	- ```bash
	  ls -l /usr/bin
	  ```
	- The output might look like as follows:
	- ```textile
	  total 93290
	  -rwxr-xr-x 1 rajib 197121   72418 Jul 13  2023 '[.exe'*
	  -rwxr-xr-x 1 rajib 197121    3075 Jul 13  2023  addgnupghome*
	  -rwxr-xr-x 1 rajib 197121    2217 Jul 13  2023  applygnupgdefaults*
	  -rwxr-xr-x 1 rajib 197121   35876 Jul 13  2023  arch.exe*
	  -rwxr-xr-x 1 rajib 197121     858 Jul 13  2023  astextplain*
	  -rwxr-xr-x 1 rajib 197121   27341 Jul 13  2023  autopoint*
	  -rwxr-xr-x 1 rajib 197121  627466 Jul 13  2023  awk.exe*
	  -rwxr-xr-x 1 rajib 197121   55390 Jul 13  2023  b2sum.exe*
	  -rwxr-xr-x 1 rajib 197121    7339 Jul 13  2023  backup*
	  -rwxr-xr-x 1 rajib 197121   41819 Jul 13  2023  base32.exe*
	  -rwxr-xr-x 1 rajib 197121   41819 Jul 13  2023  base64.exe*
	  -rwxr-xr-x 1 rajib 197121   34883 Jul 13  2023  basename.exe*
	  ------------------------------------------------------------
	  ------------------------------------------------------------
	  ------------------------------------------------------------
	  ```
	- ```bash
	  ls -l /usr/bin | grep "base"
	  ```
	- The output will shows only those files containing "base"
	- ```textile
	  -rwxr-xr-x 1 rajib 197121   41819 Jul 13  2023 base32.exe*
	  -rwxr-xr-x 1 rajib 197121   41819 Jul 13  2023 base64.exe*
	  -rwxr-xr-x 1 rajib 197121   34883 Jul 13  2023 basename.exe*
	  -rwxr-xr-x 1 rajib 197121   49499 Jul 13  2023 basenc.exe*
	  -rwxr-xr-x 1 rajib 197121   52962 Jul 13  2023 msys-heimbase-1.dll*
	  -rwxr-xr-x 1 rajib 197121  901362 Jul 13  2023 rebase.exe*
	  -rwxr-xr-x 1 rajib 197121    7151 Jul 13  2023 rebaseall*
	  ```
	-
- ### output redirection to another file
	- ```bash
	  # if we want to overwrite everyting use '>' single greater than sign
	  echo "Hello World" > hello.txt 
	  
	  # if we want to append new text use '>>' double greater than sign
	  echo "How are you" >> hello.txt
	  
	  # to see what is currently written in the file
	  cat hello.txt
	  ```
- ### how to write an if else statement?
	- ```bash
	  #!/bin/bash
	  # $1 means the positional argument
	  # $1,, means the positional argument and it's lowercase transformation
	  if [ ${1,,} = rajib ]; then
	  	echo "Hey, you are the boss here"
	  elif [ ${1,,} = help ]; then
	  	echo "Man! just hit your username"
	  else
	  	echo "I don't know you!"
	  fi
	  
	  ```
- ### how to write case statement?
	- ```bash
	  #!/bin/bash
	  
	  case ${1,,} in
	      rajib | admin)
	          echo "Hey, you are the boss here"
	          ;;
	      help)
	          echo "Just enter your username"
	          ;;
	      *)
	          echo "I don't know you!"
	  esac
	  ```
- ### how to write for loop in bash?
	- ```bash
	  #!/bin/bash
	  
	  # an example of for loop
	  arr=("apple" "banana" "cherry")
	  for item in ${arr[@]}; do
	      word_length=$(echo $item | wc -c)
	      echo $item $word_length
	  done
	  
	  # Output:
	  # apple 6
	  # banana 7
	  # cherry 7
	  ```
- ### how to preapare array of elements in bash?
	- ```bash
	  #!/bin/bash
	  
	  # an example of array
	  
	  declare -a arr=("apple" "banana" "cherry")
	  echo "All values: ${arr[@]}"
	  echo "Specific value: ${arr[1]}"
	  
	  # Output:
	  # All values: apple banana cherry
	  # Specific value: banana
	  
	  ```
- ### how to write functions in bash?
	- ```bash
	  #!/bin/bash
	  
	  # an example of function
	  function greet() {
	      echo "Hello, $1 $2"
	  }
	  
	  sum_of_two_numbers() {
	      local sum=$(($1 + $2))
	      return $sum
	  }
	  
	  # function without return value
	  greet "Rajib" "Das"
	  
	  # function with return value
	  sum_of_two_numbers 10 20
	  ans=$?
	  echo "Sum of two numbers: $ans"
	  
	  # Output:
	  # Hello, Rajib Das
	  # Sum of two numbers: 30
	  
	  ```
- ### how 'awk' works?
	- ```bash
	  #!/bin/bash
	  
	  # an example of awk
	  
	  echo one two three > temp.txt
	  awk '{print $1}' temp.txt
	  awk '{print $2}' temp.txt
	  
	  echo "Just get this word: Hello" | awk '{print $5}'
	  echo "Just get this word: Hello" | awk -F: '{print $1}'
	  echo "Just get this word: Hello" | awk -F: '{print $2}'
	  echo "Just get this word: Hello" | awk -F: '{print $2}' | cut -d' ' -f2
	  
	  # Output:
	  # one
	  # two
	  # Hello
	  # Just get this word
	  #  Hello
	  # Hello
	  ```
- ### how 'sed' works?
	- ```bash
	  #!/bin/bash
	  
	  # Replace Text (Substitution)
	  echo "Hello World" | sed 's/World/Bash/'
	  # Output: Hello Bash
	  
	  # Replace All Occurrences of a Pattern
	  echo "apple orange apple" | sed 's/apple/banana/g'
	  # Output: banana orange banana
	  
	  # Modify a File Directly (In-Place Editing)
	  sed -i 's/old/new/g' file.txt
	  # Replace all occurrences of 'old' with 'new' in file.txt
	  # -i modifies the file directly without creating a backup.
	  
	  # Delete specific line in a text file
	  sed -i '3d' file.txt
	  # Delete the 3rd line in file.txt
	  
	  # remove all empty lines in a text file
	  sed -i '/^$/d' file.txt
	  
	  # remove everything after line 10 in a text file
	  sed -i '10,$d' file.txt
	  ```
- ### some more advanced 'sed' commands:
	- ```bash
	  # Multiple Replacements in One Command
	  sed 's/World/Bash/g; s/apple/banana/g' file.txt
	  # Output: Hello Bash orange banana
	  
	  # Case-Insensitive Search and Replace
	  sed 's/World/Bash/Ig' file.txt
	  
	  # If you want a backup before modifying:
	  sed -i.bak 's/World/Bash/g' file.txt
	  
	  # Extract text between <start> and <end> tags:
	  sed -n '/<start>/,/<end>/p' file.txt
	  
	  # examples of combing sed with grep
	  grep "error" log.txt | sed 's/error/ERROR/g'
	  grep "error" log.txt | sed 's/error/ERROR/g' > error_log.txt
	  grep "error" log.txt | sed 's/error/ERROR/g' | sed 's/warning/WARNING/g' > error_log.txt
	  grep "error" log.txt | sed 's/error/ERROR/g; s/warning/WARNING/g' > error_log.txt
	  ```
-