# EGit Use

## What is EGit?
The EGit project is implementing Eclipse tooling on top of the JGit Java 
implementation of Git EGit is a great tool that allows for an efficient 
management and use of git commands within Eclipse. Eclipse projects produce a 
lot of overhead that allow Eclipse to be a great tool for working with Java. 
However, this can cause problems with complicated `.gitignore` and `.git/config`
files. The solution to this problem is EGit, which creates a git repository that
contains the sym-linked to the relevant files in your Eclipse workspace. All of 
the GUI commands then run on this sym-linked repo.  

EGit Also provides a bash terminal that is available at the click of a button. 
Here, git commands run for the appropriate sym-linked directory.

## Terminal or GUI?
Once a repository is created using EGit, the EGit bash shell allows for 
manipulation of standard git commands. There is a choice to be made: GUI or bash? 
We advocate the use of the Eclipse GUI for git, though some have suggested that 
it confounds core git concepts, because it minimizes students accidentally 
executing unwanted or "unsafe" commands. Further, the terminal is intimidating for 
beginning computer science students. In the face of these two options, we advocate 
the use of the EGit GUI as the primary method of git usage for the course, because 
it provides a pleasant distinction between unstaged, staged, and commited files, 
that is much more difficult to understand in the bash terminal. It will also reduce 
the amount of time needed to talk about Git keeping the focus on the concepts 
discussed in lecture and the actual CS051 curriculum.

Nonetheless, some command line interaction will be necessary, primarily for
`pull`ing and `branch`ing.  So, to facilitate this process for the students,
we created [this python script](configure_git.py) to create a simple, readable command line
interface.  It is as follows

| Alias               | Command                        | Effect                               |
|:-------------------:|:------------------------------:|:------------------------------------:|
| `git starterCode`   | `git pull starter-code master` | *gets the starter Code for new lab*  |
| `git newLab labXX`  | `git checkout -b labXX`        | *creates a new branch for the labXX* |
| `git submit labXX`  | `git push -u submission`       | *pushes a new, tracked remote branch for the labXX* |

The student would then use the Git GUI to `add`, and `commit`. This friendly git
interface could be entered directly into the Eclipse bash shell allowing
students to focus on core concepts.
