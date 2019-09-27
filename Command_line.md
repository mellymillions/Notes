**Command Line**

Congratulations! You’ve learned five commands commonly used to navigate the filesystem from the command line. What can we generalize so far?

The command line is a text interface for the computer’s operating system. 

To access the command line, we use the **terminal**.

A filesystem organizes a computer’s files and directories into a tree structure. It starts with the root directory. 

Each parent directory can contain more child directories and files.

## Basic Commands

From the command line, you can navigate through files and folders on your computer:

**pwd** outputs the name of the current working directory.

**ls** lists all files and directories in the working directory.

    ls -a 
    #lists all contents of a directory, including hidden files and directories

    ls -l 
    #lists all contents in long format
    
    ls -t 
    #orders files and directories by the time they were last modified

    ls -alt
    #List all contents, in long format, including the hidden files and directories, ordered by the date and time they were last modified.

**cd** switches you into the directory you specify.

    cd ../
    # brings you back to the previous directory
    
    cd ../../directory1/ 
    # brings you back to a specific directory two levels up. 

**mkdir** creates a new directory in the working directory.

**touch** creates a new file inside the working directory.



# Special Characters

**Grouping files**: The astericks is a 'wildcard' symbol that selects all files in a working directory.

    *   


# Advanced Commands

## Copy: **cp** copies a file.

    cp file1.txt

 Copy a file to a new directory:

    cp vine.txt ../pencils/color.txt

 Copy multiple files into the same new directory:

    cp directory1/file1.txt file2.txt directory2/

Copy a single file into a new directory:
    
    cp * directory/ 

Copy only files that start with a specific letter (in this case, 'm'):
    cp m*.txt scifi/

## Move: **mv** moves a file to another location.

    mv file1.txt directory1/ 

    mv file1.txt file2.txt directory2/ 

mv can also be used to rename. The example below will change file1.txt and rename it file2.txt

    mv file1.txt file2.txt 

## Remove: **rm** removes files and directories.

Remove a file:

    rm file1.txt 

Remove a directory:

    rm -r directory1 

