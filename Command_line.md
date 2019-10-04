**Command Line**


The command line is a text interface for the computer’s operating system. 

To access the command line, we use the **terminal**.

A filesystem organizes a computer’s files and directories into a tree structure. It starts with the root directory. 

Each parent directory can contain more child directories and files.

# Basic Commands

From the command line, you can navigate through files and folders on your computer:

## pwd

**pwd** outputs the name of the current working directory.

## ls

**ls** lists all files and directories in the working directory.

    ls -a 
    #lists all contents of a directory, including hidden files and directories

    ls -l 
    #lists all contents in long format
    
    ls -t 
    #orders files and directories by the time they were last modified

    ls -alt
    #List all contents, in long format, including the hidden files and directories, ordered by the date and time they were last modified.

## cd

**cd** switches you into the directory you specify.

    cd ../
    # brings you back to the previous directory
    
    cd ../../directory1/ 
    # brings you back to a specific directory two levels up. 

## mkdir

**mkdir** creates a new directory in the working directory.

## touch

**touch** creates a new file inside the working directory.


# Special Characters

**Grouping files**: The astericks is a 'wildcard' symbol that selects all files in a working directory.

    *   


# Advanced Commands

## cp

Copy: **cp** copies a file.

    cp file1.txt

 Copy a file to a new directory:

    cp vine.txt ../pencils/color.txt

 Copy multiple files into the same new directory:

    cp directory1/file1.txt file2.txt directory2/

Copy a single file into a new directory:
    
    cp * directory/ 

Copy only files that start with a specific letter (in this case, 'm'):
    cp m*.txt scifi/

## mv

Move: **mv** moves a file to another location.

    mv file1.txt directory1/ 

    mv file1.txt file2.txt directory2/ 

mv can also be used to rename. The example below will change file1.txt and rename it file2.txt

    mv file1.txt file2.txt 

## rm

Remove: **rm** removes files and directories.

Remove a file:

    rm file1.txt 

Remove a directory:

    rm -r directory1 

## echo

The echo command accepts the string “Hello” as standard input, and echoes the string “Hello” back to the terminal as standard output.

**standard input** - abbreviated as stdin, is information inputted into the terminal through the keyboard or input device.

**standard output** - abbreviated as stdout, is the information outputted after a process is run.

**standard error** - abbreviated as stderr, is an error message outputted by a failed process.

Redirection reroutes standard input, standard output, and standard error to or from a different location.

# Redirection
```bash
$ echo "Hello" > hello.txt
```
The > command redirects the standard output to a file. Here, "Hello" is entered as the standard input. The standard output "Hello" is redirected by > to the file hello.txt.

## cat

The cat command outputs the contents of a file to the terminal. When you type cat hello.txt, the contents of hello.txt are displayed.

```bash
cat hello.txt
```

## >

The '>' takes the standard output of the command on the left, and redirects it to the file on the right. Below, the standard output of cat oceans.txt is redirected to continents.txt.

```bash
$ cat oceans.txt > continents.txt
```

Note that > overwrites all original content in continents.txt. When you view the output data by typing cat on continents.txt, you will see only the contents of oceans.txt.

 ## >> 
 
The >> command below  takes the standard output of the command on the left and appends (adds) it to the file on the right. You can view the output data of the file with cat and the filename.

```bash
cat glaciers.txt >> rivers.txt 
cat rivers.txt

#output is a combination of both rivers and glaciers.
```

## pipe |

| is a “pipe”. The | takes the standard output of the command on the left, and pipes it as standard input to the command on the right. You can think of this as “command to command” redirection.

```bash
$ cat volcanoes.txt
17 26 204

$ cat volcanoes.txt | wc | cat > islands.txt 

#here, we took the volcanoes.txt file and piped it to the islands.txt. The output of then calling:

$ cat islands.txt
17 26 204
#now yeilds the same output as the original $ cat volcanoes.txt
```
Multiple |s can be chained together. Here the standard output of cat volcanoes.txt is “piped” to the wc command. The standard output of wc is then “piped” to cat. Finally, the standard output of cat is redirected to islands.txt.

## sort

sort takes the standard input and orders it alphabetically for the standard output. Here, the lakes in sort lakes.txt are listed in alphabetical order.

```bash
$ sort lakes.txt 

$ cat lakes.txt | sort > sorted-lakes.txt 
#Here, the command takes the standard output from cat lakes.txt and “pipes” it to sort. The standard output of sort is redirected to sorted-lakes.txt.

$ cat sorted-lakes.txt
#You can view the output data by typing cat on the file sorted-lakes.txt.
```
## uniq

uniq stands for “unique” and filters out adjacent,duplicate lines in a file. 

Here uniq deserts.txt filters out duplicates of “Sahara Desert”, because the duplicate of ‘Sahara Desert’ directly follows the previous instance. The “Kalahari Desert” duplicates are not adjacent, and thus remain.

A more effective way to call uniq is to call sort to alphabetize a file, and “pipe” the standard output to uniq. Here by piping sort deserts.txt to uniq, all duplicate lines are alphabetized (and thereby made adjacent) and filtered out.
## sort 

```bash
$ uniq deserts.txt 

$ sort deserts.txt | uniq

$ sort deserts.txt | uniq > uniq-deserts.txt 
#More efficient, Here we simply send filtered contents to uniq-deserts.txt, which you can view with the cat command.
```
## grep

grep stands for “global regular expression print”. It searches files for lines that match a pattern and returns the results. It is also case sensitive. 

Here, grep searches for “Mount” in mountains.txt.

```bash
$ grep Mount mountains.txt 
```
**grep -i** 

enables the command to be case insensitive. Here, grep searches for capital or lowercase strings that match Mount in mountains.txt.

```bash
$ grep -i Mount mountains.txt
```

These commands are a great way to get started with grep. If you are familiar with regular expressions, you can use regular expressions to search for patterns in files.

grep can also be used to **search within a directory**, below:

**grep -R**

grep -R searches all files in a directory and outputs filenames and lines containing matched results. -R stands for “recursive". 

Here grep -R searches the /home/ccuser/workspace/geography directory for the string “Arctic” and outputs filenames and lines with matched results.


```bash
grep -R Arctic /home/ccuser/workspace/geography

#output includes two directories that include 'Arctic'
/home/ccuser/workspace/geography/deserts.txt: Arctic Desert
/home/ccuser/workspace/geography/oceans.txt: Arctic Ocean
```
**grep -Rl**

grep -Rl searches all files in a directory and outputs only filenames with matched results. -R stands for “recursive” and l stands for “files with matches”. 

Here,   grep -Rl searches the /home/ccuser/workspace/geography directory for the string “Arctic” and outputs filenames with matched results.

```bash
$ grep -Rl Arctic /home/ccuser/workspace/geography

#how exactly is grep -R and grep -Rl different?
```

## sed

sed stands for “stream editor”. It accepts standard input and modifies it based on an expression, before displaying it as output data. It is similar to “find and replace”.

Let’s look at the expression 's/snow/rain/':

```bash
$ sed 's/snow/rain/' forests.txt 
```
Let’s look at the expression 's/snow/rain/':

1. **s**: stands for “substitution”. it is always used when using sed for substitution.

2. **snow**: the search string, the text to find.

3. **rain**: the replacement string, the text to add in place.

In this case, sed searches forests.txt for the word “snow” and replaces it with “rain.” Importantly, the above command will **only replace the first instance of “snow” on a line**.

```bash
$ sed 's/snow/rain/g' forests.txt 
```
The above command uses the **g** expression, meaning “global”. Here sed searches forests.txt for the word “snow” and replaces it with “rain”, globally. **In this case, ALL instances of “snow” on a line will be turned to “rain”**.

