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
	  !/bin/bash
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
- output redirection to another file
	- ```bash
	  # if we want to overwrite everyting use '>' single greater than sign
	  echo "Hello World" > hello.txt 
	  
	  # if we want to append new text use '>>' double greater than sign
	  echo "How are you" >> hello.txt
	  
	  # to see what is currently written in the file
	  cat hello.txt
	  ```