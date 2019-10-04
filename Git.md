# Commiting files

#Committing changes

## git init

Creates a new respository

## git add

To save, or commit, files into your Git repository you first need to add them to the staging area. 

Git has three areas:
1.  a working directory
2. a staging area 
3. the repository itself. 

Users move, otherwise referred to as **promote**, changes from the working directory, to a staging area before committing them into the repository.

One of the key approaches with Git is that commits are focused, small and frequent. The staging area helps to maintain this workflow by allowing you to only promote certain files at a time instead of all the changes in your working directory.

```
git add <file|directory>
```

## git commit

Once a file has been added to the staging area it needs to be committed to the repository. 

The command git commit -m "commit message" 
1. moves files from staging to the repository 
2. records the time/date, author 
3. records a commit message that can be used to add additional context and reasoning to the changes such as a bug report number.

Only changes added to the staging area will be committed, any files in the working directory that have not been staged will not be included.
```
git commit -m "<commit message>"
```
## git ignore

Sometimes there are particular files or directories you never want to commit, such as local development configuration. To ignore these files you create a .gitignore file in the root of the repository.

```
.gitignore 
```
This kind of file allows you to define wildcards for the files you wish to ignore, for example *.tmp will ignore all files with the extension .tmp.

Any files matching a defined wildcard will not be displayed in a git status output and be ignored when attempting the git add command.

## git status

Allows us to view the changes in the working directory and staging area compared to the repository.

Given the current repository running git status displays that a change has been made in our working directory to a previously committed file, committed.js, but has not yet been moved to the staging area.

## git diff

Enables you to compare changes in the working directory against a previously committed version. By default the command compares the working directory and the HEAD commit.

If you wish to compare against an older version then provide the commit hash as a parameter, for example 

```
git diff <commit>
```
Comparing against commits will output the changes for all of the files modified. If you want to compare the changes to a single file then provide the name as an argument such as git diff committed.js.

## git add

In order to commit a change it must first be staged using git add command.

**Staged Files**

The command git diff no longer works once the file has been staged. 

To compare the changes in the staging area against the previous commit you provide the staged parameter 
```
git diff --staged
``` 
This enables you to ensure that you have correctly staged all your changes.

## git log

Allows you to view the history of the repository and the commit log. It tells you the commit author and message.

You can find the HASH in here too, used to detach HEAD.


## git show

To view the changes made in the commit you need to use the the command git show.

To review older changes, use:

```
show <commit-hash> 
```

# Working remotely

Remote repositories allow you to share changes from or to your repository. Remote locations are generally a build server, a team members machine or a centralised store such as Github.com. 

Remotes are added using the git remote command with a friendly name and the remote location, typically a HTTPS URL or a SSH connection.

The friendly name allows you to refer to the location in other commands. Your local repository can reference multiple different remote repositories depending on your scenario.

## git remote

**Sample Task**: This environment has a remote repository location of /s/remote-project/1. Using git remote, add this remote location with the name origin.

```bash
 git remote add origin /s/remote-project/1
```

## git push

When you're ready to share your commits you need to push them to a remote repository via git push. 

A typical Git workflow would be to perform multiple small commits as you complete a task and push to a remote at relevant points, such as when the task is complete, to ensure synchronisation of the code within the team.

The git push command is followed by two parameters. The first parameter is the friendly name of the remote repository we defined in the first step. The second parameter is the name of the branch. By default all git repositories have a master branch where the code is worked on.
```
git push origin master
```
## git pull

Where git push allows you to push your changes to a remote repository, git pull works in the reverse fashion. 

**git pull allows you to sync changes from a remote repository into your local version.**

The changes from the remote repository are automatically merge into the branch you're currently working on.

```
git pull origin master
```

## git log

You can use the git log command to see the history of the repository. The git show command will allow you to view the changes made in each commit.

In this example, the output from git log shows a new commit by "DifferentUser@JoinScrapbook.com" with the message "Fix for Bug #1234". The output of git show highlights the new lines added to the file in green.

## git fetch

The command git pull is a combination of two different commands, git fetch and git merge.

Fetch downloads the changes from the remote repository into a separate branch named 
```
remotes/<remote-name>/<remote-branch-name>
```
The branch or specific commit can be accessed using **git checkout**.

```
git fetch

git checkout remotes/origin/master
```

Using git fetch is a great way to review the changes without affecting your current branch. The naming format of branches is flexible enough that you can have multiple remotes and branches with the same name and easily switch between them.

The following command will merge the fetched changes into master.

```bash
git merge remotes/<remote-name>/<remote-branch-name> master

#more on merging later
```

# git branching

```
git branch
```
## git checkout

git checkout changes your location between a branch and master to set up for a merge. (more on this in the **branch and merge lab** later)

```bash
git checkout

git checkout -b #add a filename here to branch and checkout in one line!
```

## git merge

Now we need to learn some kind of way of combining the work from two different branches together. This will allow us to branch off, develop a new feature, and then combine it back in.

The first method to combine work that we will examine is git merge. Merging in Git creates a special commit that has two unique parents. 

A commit with two parents essentially means "I want to include all the work from this parent over here and this one over here, and the set of all their parents."

**Example**: Here we have two branches; each has one commit that's unique. This means that neither branch includes the entire set of "work" in the repository that we have done. Let's fix that with merge.

We will **merge** the **branch** bugFix into **master**

## HEAD

HEAD is the symbolic name for the currently checked out commit -- it's essentially what commit you're working on top of.

HEAD always points to the most recent commit which is reflected in the working tree. Most git commands which make changes to the working tree will start by changing HEAD.

Normally HEAD points to a branch name (like bugFix). When you commit, the status of bugFix is altered and this change is visible through HEAD.

**detaching HEAD**

Detaching HEAD just means attaching it to a commit instead of a branch. This is what it looks like beforehand:

HEAD -> master -> Hash

to

HEAD -> hash

```bash
git checkout master
git checkout #hash

#you can use git log to find the hash!
```

# Rebase

The second way of combining work between branches is **rebasing**. Rebasing essentially takes a set of commits, "copies" them, and plops them down somewhere else.

While this sounds confusing, the advantage of rebasing is that it can be used to make a nice linear sequence of commits. 

The commit log / history of the repository will be a lot cleaner if only rebasing is allowed.

```
git rebase
```




# Pro tips

If you rename or delete files then you need to specify these files in the add command for them to be tracked. Alternatives you can use 
```
git mv 

git rm 
```
for git to perform the action and include update the staging area.

## Find an error

Use the command git log --grep="#1234" to find all the commits containing #1234

## Make the git log easier to read

```
git log --pretty=oneline

git log --pretty=short
```

# Labs

## Branch and Merge practice:

To complete this level, do the following steps:

1. Make a new branch called bugFix
```bash
git branch bugFix
```
2. Checkout the bugFix branch with git checkout bugFix
```bash
git checkout bugFix
#move to the bugFix branch from the master branch
```
3. Commit once
```bash
git commit
#commit the bugFix branch and move it forward
```
4. Go back to master with git checkout
```bash
git checkout master
#move back to the master 
```
5. Commit another time
```bash
git commit
#move forward on the master branch
```
6. Merge the branch bugFix into master with git merge
```bash
git commit bugFix
#merge to the master 
```
**The end!**

## Rebase Lab

To complete this level, do the following:

1. Checkout a new branch named bugFix
```bash
git checkout -b bugFix
#creates and moves to a new branch
```
2. Commit once
```bash
git commit
# branches the bugFix branch off the master
```
3. Go back to master and commit again
```bash
git checkout master
#moves back to the master branch

git commit
#branches the master into a separate branch from bugFix
```
4. Check out bugFix again and rebase onto master
```bash
git checkout bugFix
#jump back to the bugFix branch

git rebase master
# paralell merge it into the master 
```

# Commit Git

1. git status
2. git add . (or the name of file)
3. git status  (to check that its been staged)
4. git commit -m "Commit Message"
5. git push
