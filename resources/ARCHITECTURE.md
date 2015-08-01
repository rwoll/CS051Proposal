## General Architecture

There are four main pieces to this proposed architecture, the starter
code, the student’s code, the student’s submission, and the TA’s grading
repositories. 

> **NOTE:** The full `git` jargon and commands are used below to explain more precisely
> what is occuring. However, we have created **[ALIASES](/resources/EGIT_USE.md#terminal-or-gui)**
> for all the student commands to eliminate the need to remember and learn the Git
> lingo.

* * *
![ArchitecureImage](/resources/architecture_v.png)
* * *

> **Continued Use Workflow**
> 1. Professor `push`es new labs to a master repository (`pull`-only for students).
> 2. Students `pull` the lab into their local repository (and with it, into Eclipse).
> 3. Each student `push`es their lab to their private GitHub sandboxed repository.
> 4. The TA grading the section, (with a scripted command) `pulls` all the student changes
   in one command to their computer which has been configured to automatically
   show up in Eclipse at the start of the year.
   TA compiles each students code and leaves feedback directly through GitHub.

#### The Starter Code

The starter code and the lab assignments will be hosted on the
`PomonaCollege/cs-051` repository (*name subject to change*). This repository
will have pull-only access for students (and possibly TAs). Each `labXX` file
will contain a github-markdown `INSTRUCTIONS.md` file. The lab write-up can be
ported directly to this `INSTRUCTIONS.md` file with the lab write-up mostly
unchanged from its current state (The instructions will need to be modified to
contain git-related instructions.) This `labXX` file will also need to contain
an `example.jar` file that contains the fully-functional working example of the
lab. (Another option would be to embed the `example.jar` file into a
GitHub-Pages website or have it on the current CS Department website)
Students will then do a `git pull upstream master` to
get their new lab assignment.  Given that the TA and professors do not push
modifications of the previous lab assignments, this will go over without any
merge conflicts.

An example of the proposed starter code repository layout:

```
PomonaCollege/fa2015
├── README.md
├── .gitignore
│
├── lab01
│   ├── INSTRUCTIONS.MD
│   ├── example.jar
│   ├── bin
│   └── source
│
├── lab02
│   ├── INSTRUCTIONS.MD
│   ├── example.jar
│   ├── bin
│   └── source
.
/
.
└── lab10
    ├── INSTRUCTIONS.MD
    ├── example.jar
    ├── bin
    └── source
```

#### The Students’ Code

Once the Student has successfully run their `git pull upstream master` to get
their new code, they will create a local branch, called `labXX`, on which they
will develop their lab assignments as normal, using git’s version control. Once
they have completed the assignment or want some TA feedback, they will push to
`origin master`, the remote specified for submissions. 

#### The Student Submission

Github for Education allows for the creation of private repos assigned to
students for their submissions. This will be their `origin` remote. They will
have a master branch with all of their previous lab submissions. For each lab,
they will push their new branch to `origin` using the command
`git push origin labXX` (or the EGit GUI). Then, they will go to Github and
create a [pull request](https://help.github.com/articles/using-pull-requests/)
(PR) to merge their branch into master.

#### TAs Grading Repositories

The TA will then pull the new branch for each student down from `master`, and
the Eclipse Git Client then allows for easier import of repositories into the
workspace -- no more dragging and dropping (and overwriting) student source
folders; simply click on the repo in the EGit client and complete the
one-click import. 

The TA can then run the code in Eclipse and grade the functionality. This grade
will then be left in a comment on the PR submitted by the student. The TA can
then provide in-line comments directly onto the PR for style and efficiency
points. A final grade will then be left as a comment at the bottom of the PR. 

Once the grade has been recorded into the gradebook, the TA will merge the pull
request into their ever-growing `master` branch, which, at the end of the
semester, will be a repository of all of their lab assignments. For the TAs,
the initial setup will be somewhat tedious (requiring the initial cloning of
each student’s repository). However, git repository management programs, such
as `myrepos` and `git-town`,  will allow the TAs to easily update their cloned
repos once they have been established. (for example `myrepos` simply requires
the command `mr up` to pull from all registered remotes in any subdirectory).
