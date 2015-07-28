GitHub + Eclipse: A CS051 Proposal
========

* * *
*This proposal has been compiled by [Ross W](mailto:ross.wollman@pomona.edu)
and [Eric C](mailto:eric.campbell@pomona.edu).*

The sample assignment repository can be found [here](https://github.com/rwoll/GitHubEclipse).

Additional reading on all the tools and processes explained can be found at
the bottom of the page.
* * *

## The Proposal

Create and run an experimental CS051 Lab Section for Fall 2015, with 
the end goal of adoption throughout all CS051 lab sections, that will 
integrate GitHub and EGit to promote sustainable and easily-revisable 
code production that will benefit students, TAs, and professors. 

Students will learn an industry standard versioning tool that promotes 
incremental development and provides low-risk experimentation for more 
efficient programming. TAs and Professors will have their workload 
dramatically reduced, and grading will be held to a higher standard as
specific comments will be visible by the CS051 grading team.

A success in this experiment is defined by the incorporation of versioning
into the students general coding practice, as well as a decrease in overhead 
and increase in quality for the grading and code distribution processes.

## Personal Motivation

In our internships this summer, we independently learned the valuable incremental
version-controlled code-production pattern employed by software companies who 
wish to produce code with low technical debt. We wish we had learned Git in school
to help lower the steep learning curve that we found at our internships -- we 
were expected to be competent. With the hope to minimize this speedbump for future
students, and to help them to have more success in their computer science education
we want to introduce this invaluable and ubiquitous tool into the CS051 lab 
infrastructure.

## Overview: Why Consider GitHub in CS051?

GitHub has become an industry-leader in cloud hosting code repositories and it
has propelled the popularity of Git as the de facto standard for
distributed version control systems. With a large number of businesses and open
source communities utilizing the tool, incorporating it into the CS051
classroom could help students learn invaluable versioned development skills
that can be transferred to their personal projects, future classes,
and careers.

Learning Git itself is a baseline skill for anyone working in the industry.
Students who are well versed in git will have a leg up both during their internships,
as well as once they leave college to continue on to graduate school or their careers.
Its use also promotes a better coding practice, and would force students to
complete their assignments in a incremental, feature-based manner.

Further, with code edits and comments from students, TAs, and professors captured online
by GitHub, course participants will have a history, in the Pull Requests tab, of their
development throughout the semester. This is a significant improvement on the previous 
model of digging through ancient emails to find hard-to-follow PDFs.

> **NOTE:** With the GitHub (Free) Education plan, all student code will be
  hosted in private locations. Only TAs, professors, and an individual student
  will have access to viewing/editing their repositories.
  They will **NOT** be publicly visible.

From a TA or Professor's perspective, using GitHub could help maximize the
feedback students receive on their code by reducing the number of steps
in the grading process. It would simplify the collection of student projects
and facilitate the dissemination of feedback. Professors and TAs will also have
a more transparent view of student progression and TA feedback, promoting grading 
consistency across the department.

Another advantage of GitHub in the development of this new course material is
as a resource for TAs and Professors. The professors will be able to version 
control the iterations of the course, simply creating a new fork of the 
repository for each semester. This would create a complete record of previous 
versions of the course and allow for simple, collaborative modifications, as 
changes are made to the course into the future.

While in its simplest form, GitHub could act as little more than a glorified
online dropbox that allows for more efficient distribution and collection of
assignments, there are many other features of Git and GitHub that could
add greatly to the CS051 experience.

## *Git*-ing Into It

The difficulty with integrating git version control into a classroom setting is
leveling the learning curve. We advocate the slow introduction of new git
strategies as the course progresses.  In the first lab, students would be
limited to simply `pull`ing, `commit`ting, and `push`ing their changes;
GitHub, at this point, would simply act as a dropbox. For subsequent labs, we
would suggest strategic checkpoints at which to `commit`. This fits in well
with the incremental development employed by the current write-ups. Later, the
idea of `branch`ing would be introduced to help encapsulate the development
process and the functional additions to each class.

## General Architecture

There are four main pieces to this new, proposed architecture, the starter
code, the student’s code, the student’s submission, and the TA’s grading
repositories. 

> N.B. All of the commands in this assignment can be performed using the EGit
  GUI interface. They are included as terminal commands below for ease of
  readability.

* * *
![ArchitecureImage](/architecture_v.png)
* * *

#### The Starter Code

The starter code and the lab assignments will be hosted on the
`PomonaCollege/cs-051` repository (*name subject to change*). This repository
will have pull-only access for students (and possibly TAs). Each `labXX` file
will contain a github-markdown `INSTRUCTIONS.md` file. The lab write-up can be
ported directly to this `INSTRUCTIONS.md` file with the lab write-up mostly
unchanged from its current state (The instructions will need to be modified to
contain git-related instructions.) This `labXX` file will also need to contain
a `example.jar` file that contains the fully-functional working example of the
lab. (Another option would be to embed the `example.jar` file into a
GitHub-Pages website.) Students will then do a `git pull upstream master` to
get their new lab assignment.  Given that the TA and professors do not push
modifications of the previous lab assignments, this will go over without any
merge conflicts.

An example of the proposed starter code repository layout:

```
HOME
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
folders; simply click on the repo in the EGit client and import. 

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

## Questions to Consider

+ How setup the current lab folders to work with GitHub?
    + All that needs to be done, is to initialize a repository, using Git or
      EGit, in the containing folder of the starter code, push it to the remote
      `PomonaCollege/cs051-FA201X` educational branch. When the starter code
      for each lab is to be published, the following commands will be run: 
```
git add LabXX-LabName
git commit -m “publish labXX”
git push
```
It would also be fairly straightforward to create a function in `.bash_profile`
to do this. Something like the script below. It is to be run in the repository, 
and expects the path to the lab directory as a parameter. It also assumes that 
the `origin` remote is desired destination repository.

```bash
publish_lab () {
    if [ -z $1  ]
    then
        echo “Parameter is of zero length”
    else
        git add $1
        git commit -m “publish $1”
        git push origin master
    fi
    return 0
}
```

+ How do Eclipse and Git Work together?
    + Through EGit, Eclipse can be setup to work smoothly with Git
      repositories. This plugin is helpful because it manages the complexly
      linked workspaces created by Eclipse. Creating repositories without its
      help is a bit more involved.
    + Once a repository is created using EGit, the bash Eclipse Terminal allows for
      manipulation of standard git commands. There is a choice to be made: GUI or 
      bash? We advocate the use of the Eclipse GUI for git, though some have
      suggested that it confounds core git concepts, because it minimizes students 
      accidentally executing unwanted or "unsafe" commands. Further, the
      terminal is intimidating for beginning computer science students.
      In the face of these two options, we advocate the use of the EGit GUI as
      the primary method of git usage for the course, because it provides a 
      pleasant distinction between unstaged, staged, and commited files, that
      is much more difficult to understand in the bash terminal.
+ What would the grading/feedback workflow look like?
    + Link to anchor in document.
+ Current Workflow
    1. Professor uploads Html Writeup to server.
    2. Professor adds Eclipse starter code to permissions-controlled dropbox
    3. Students drag-and-drop the starter code to their workspace
    4. Students import the project to Eclipse
    5. Save File, Export file [with proper naming convention], drag-and-drop
       back to dropbox
    6. TA opens the dropbox, to drag-and-drop each student directory into their
       home directory.
    7. Export each project into Eclipse to run it.
    8. TA copy-and-pastes each student’s code into a text document to be
       converted into a PDF for commenting (or uses existing script).
    9. TA creates a rubric `.txt` file as a baseline for each student’s lab.
    10. TA adds comments to each students PDF on specific lines of code and adds
        the rubric.
    11. TA emails the commented PDF and grade file to each student.
    12. Adds grade to a Google Spreadsheet.
+ Proposed Workflow
    1. Professor pushes Eclipse project (with Readme instructions and working
       example`.jar` file) to the `upstream` GitHub repo.
    2. Student clones repository and creates a new branch called `labXX`
    3. Student adds, commits, and pushes their completed assignment to
       `origin/labXX`
    4. Student creates a Pull Request.
    5. TA clones repos with [`teachers_pet`](1) (first time only, subsequent
       assignments would be retrieved using git maintenance software such as
       [`myrepos`](https://myrepos.branchable.com/) )
    8. TA provides inline comments on the pull request and a grade in the final
       comment of the PR.  Once it has been graded the TA merges the PR and
       records the grade in the grade book. 

+ What software needs to be installed on the lab computers?
    + [Eclipse with the EGit plugin](http://www.eclipse.org/downloads/packages/eclipse-ide-java-developers/marsr)
      (The linked version ships with EGit.)
    + Git. On Mavericks 10.9 and higher, simply type `git` into the command
      line.  Otherwise use the binary installer found [here]( http://git-scm.com/download/mac)
    + (recommended) A Git visualization client such as SourceTree or
      Github for Mac 

+ What could go wrong?
    + Merge conflicts could be difficult to resolve if encountered by students
      -- TAs would have to be versed in Git to resolve the conflicts. However,
      the strategy of separating assignments into different directories within
      the main repository will minimize merge conflicts to any of the master
      branches. They would only cause difficulty in poorly-executed version-
      branches of student assignments. The students, once given a tutorial on
      how to resolve merge conflicts, should be able to resolve these. 
      Otherwise TAs and Teachers can be of help. This is not a problem we
      foresee happening too often, because it would require a student to
      create a branch, commit to it, switch back to the assignment branch,
      commit to that, and then try and merge.
    + Students could theoretically tamper with the GitHub API and alter pull
      request and commit timestamps through an elaborate command line process
      -- this would make it seem like they’ve handed in their lab earlier than
      reality. If this becomes a concern, there are strategies to detect
      and address it through Webhooks.

## Configuration
### Initial Setup: Sandboxing with GitHub for Education and `teachers_pet`
To create the starter-code repository, push the locally-initalized repository of
lab assignments (initially empty) to a new repository created in `PomonaCS051`
GitHub orignization.  For the time being lets call this repository 
`PomonaCS051/fa2014`.  Then, the students need to be added to the
`PomonaCS051` organization.  Github allows you to control access permissions
through their use of Teams.  So, add the students to a Team called "Students",
and give them `pull`-only (i.e. read-only) access to `PomonaCS051/fa2014`.
Then we need to create the student submission repositories, call them 
`PomonaCS051/<studentname>_fa2014`.  Each such repository will be [sandboxed](https://education.github.com/guide/repository_setup#sandboxing),
which creates a private repository for each student (i.e. students cannot see
one anothers work). 

To create the repositories, use the rubygem `teachers_pet`.  The `create_repos`
command performs the following actions (taken directly from [Github's Site](https://education.github.com/guide/sandboxing#individual-projects)):

For each student:
  1. Create a repository in the organization based on the student's name.
  2. Create a team in the organization, matching the name of the repository.
  3. Set that team to have Push/Pull permissions.
  4. Add the student to that team.
  5. Give that team access to the corresponding repository.

### EGit Configuration Options
The following are some suggested `.gitconfig`s for the various groups involved.
All of these options can be done in the ***Eclipse*** *>* ***Preferences*** *>* 
***Team*** *>* ***Git*** *>* ***Configuration*** window.  Optionally, the student
`.gitconfig` can be included in the starter-code repository.
#### For Professors
#### For Students
To facilitate Eclipse terminal usage, students could define git `aliases` for the
more complicated and confusing commands.  The following `[alias]` portion of the
`.gitconfig` assumes that the `starter-code` remote points to the starter code
repository `PomonaCS051/fa2015`, and the `submission` remote points to the students
sandboxed repo `PomonaCS051/<studentname>_fa2015`.  
```
[alias]
  starter-code = pull starter-code master
  submit = push submission
```
This would make the student command for getting a new lab `git starter-code` and the
student command for submitting their work `git submit lab09`.

#### EGit Configuration For TAs


## The Good, the Bad, and the Merge Conflict

### Pros

+ Increased knowledge of industry workflow for beginning computer science students.
+ Simplified TA grading workflow
+ Reduced amount of folder naming complications
+ Inline code commenting feedback in the style of industry standard code review
+ Promote the development of sustainable, version-controlled code
+ Possibility for more collaborative projects
+ Easy for TA to provide feedback on student code outside lab sessions or mentoring hours without having to post to Piazza
+ Will increase performance of the students in the later, more complex labs.
+ TAs are more accountable for their feedback because comments on code and grades are easily viewable by the grading team-- more quality feedback 
+ Professors will have a clearer picture at student coding progression throughout the semester 
+ Easily switch working between lab and personal computers
+ TAs won’t overwrite student submissions.
+ Easier ability to catch academic dishonesty because there’s a clear picture of the development process
+ Easy ability to revert to older versions of code -- no more overwriting test programs hours before they are due!
+ Low-risk refactoring and experimentation (e.g. 0 index vs. 1 index)
+ Existing GUI tools allow for the avoidance of intimidating command-line use.

### Cons

+ Steeper learning curve -- The addition of Git lingo and concepts can be
  confusing at first
+ The command line is scary (but can be avoided!)
+ Merge conflicts 
+ The first lab would require additional setup for the students
+ Configuration of remotes (for the first lab setup) could be confusing.

## Branching Ideas: Related Thoughts

#### Grading
There are a few options regarding grading for the usage of git in the lab.
They are as follows:
  1. Git use would be in integral part of the grade, to be taken away from
      design or style, only to be deducted in cases of severe misuse (all in
      one commit, or 100 infinitesimal commits)
  2. Git use would be an additional point in the lab rubric.  So labs that were
      previously worth 10 points, would now be worth 11, with an additional
      point only to be deducted in cases of severe misuse (as above)
  3. Git use would not be a standard part of the lab rubric, but an additional
      extra credit point would be awarded for exceptional use (and would be 
      not given only in cases of extreme misuse).
  4. Git use is excluded entirely from the grading, and no points -- standard 
      or extra credit -- would be awarded or deducted.

We advocate option 2 or 3 for the experimental section, as git will provide 
an additional challenge for the students in this lab, and they should be 
awarded accordingly (though the additional skill set brought to them by this
program should be reward enough!)

#### Other applications of GitHub for PO-CS
Once students and familiar with the use of Git, they will be able to use it to
share resources and collaborate to promote knowledge of industry. A possible
example would be a Liasons-managed GitHub Respository that would contain cool
scripts, funny ~/.bash_profiles, tough interview questions, and other student 
resources.

#### Another side benefit
For the development of *this* project, students, TAs, and professors can submit
Pull Requests with suggestions and changes to the git instructions that may be 
included for future iterations of the course.

#### Unit Tests and Continuous Integration
One aspect that might be useful for students and TAs that could be incorporated 
in the future is Continuous Integration, or running a unit and integration 
test suite as soon as the code is pushed. This is done using GitHubs WebHooks 
capability. This would only be used in future iterations of the course.

## *Git*-ing on with it: Next Steps
  1. Create a Pomona College Github Organization and Sign up for [GitHub for Education](https://education.github.com/discount_requests/new) ASAP. 
      Approval takes up to 2 weeks.
  2. Configure Lab Computers. If the current version of Eclipse installed
       on the Lab computers does not have the EGit plugin, either
    1. download a 
        [version that  does](http://www.eclipse.org/downloads/packages/eclipse-ide-java-ee-developers/marsr).
    2. Add the EGit plugin to existing installations of Eclipse
    3. Use the older version JGit, which may have shipped with the 
        current version of Eclispe
    4. Do nothing, and we can walk the students through the EGit installation
        during their first lab period.
  3. Send the first few laboratory assignments to Ross and Eric so they can 
      convert them to GitHub-ready assignments. This involves 
    1. creating the repository
    2. converting the current write-ups from HTML to Markdown.
    3. adding the `.jar` file either to the existing repository or as a 
      [GitHub Page](https://pages.github.com/)
  4. Once the Github for Education is approved, create a `cs051-fa2015` repository
      belonging to the Pomona College organization, and push the first lab.
  5. On (or prior to) the first day of lab, students will need to sign up for GitHub
      and communicate their handles to the TAs. Then we will be able to use 
      `teachers_pet` to create their repos.

> The only tasks that need to be done by the department would be the native installation
of the EGit plugin to Eclipse (2.i-iii), and sending the first few labs (3).
The rest can be done by Eric and Ross.

## References and Further Reading

+ [GitHub Cheat Sheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf)
+ [Employing Git in the Classroom](http://www.academia.edu/5968989/Employing_Git_in_the_Classroom)
+ [GitHub Official Education Guide](https://education.github.com/guide)
+ [`teachers_pet` Documentation](https://github.com/education/teachers_pet/#giving-others-access)
+ [GitHub + University: A Follow Up](https://joshldavis.com/2014/06/30/github-university-follow-up/)
+ [EGit (Eclipse Git) Documentation](http://www.eclipse.org/egit/documentation/)
+ [Difficulties of Using GitHub in the Classroom](https://github.com/education/teachers/issues/2)

[1](https://github.com/education/teachers_pet/#giving-others-access)
