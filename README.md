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

An experimental CS051 Lab Section for Fall 2015, with the end goal
of adoption throughout all sections, that will integrate
GitHub and EGit to promote sustainable and easily-revisable code 
production that will benefit students, TAs, and professors. 

Students will learn an industry standard versioning tool that promotes 
incremental development and provides low-risk experimentation for more 
efficient programming. TAs and Professors will have their workload 
dramatically reduced, and grading will be held to a higher standard as
specific comments will be visible by the CS051 grading team.

A success in this experiment is defined by the incorporation of versioning
into the students general coding practice, as well as a decrease in overhead 
and increase in quality for the grading and code distribution processes.


## Overview: Why Consider GitHub in CS051?

In our internships this summer, we independently learned the valuable incremental
version-controlled code-production pattern employed by software companies who wish
to produce code with low technical debt. Looking back to our academic coding 
experiences we noted that our coding techniques and those of our peers were more
scatterbrained than methodical and incremental. Using a version control tool 
in complicated classes like CS052 or CS105 would promote a more sustainable
production experience, as it would allow an easy revert of a poorly thought-out
attempt to solve a problem.  From a more personal standpoint, having learned git
and its best-practices in school would have lowered some of the steep learning
curve that we found at our internships.

GitHub has become an industry-leader in cloud hosting code repositories and it
has propelled the popularity of Git as one of the most commonly used
distributed version control systems. With a large number of businesses and open
source communities utilizing the tool, incorporating it into the CS051
classroom could help students learn invaluable versioned development skills
that can be transferred to their personal projects, future classes,
and careers.

With editing and commenting from students, TAs, and professors captured online
by GitHub, students will have a history, in the Pull Requests tab, of their
development throughout the semester. This improves the previous model of digging
through email to find hard-to-follow PDFs.

> **NOTE:** With the GitHub (Free) Education plan, all student code will be
  hosted in private locations. Only TAs, professors, and an individual student
  will have access to viewing/editing their repositories.
  They will **NOT** be publicly visible.

From a TA or Professor's perspective, using GitHub could help maximize the
feedback students receive on their code by reducing the number of steps
in the grading process. It would simplify the collection of student projects
and facilitate the dissemination of feedback. Professors and TAs will also have
a more transparent view of student progression and TA feedback.

Another advantage of GitHub in the development of this new course material is
as a resource for TAs and Professors. Students and TAs can submit Pull Requests
with suggestions and changes to the git instructions that may be included for
future iterations of the course. TAs will also be able to easily view other TAs
grading strategies, promoting grading consistency across the department.

While in its simplest form, GitHub could act as little more than a glorified
online dropbox, there are many features of Git and GitHub that could
add greatly to the CS051 experience.

## *Git*-ing Into It

The difficulty with integrating git version control into a classroom setting is
leveling the learning curve.  We advocate the slow introduction of new git
strategies as the course progresses.  In the first lab, students would be
limited to simply `pull`ing, `commit`ting, and `push`ing their changes;
GitHub, at this point, would simply act as a dropbox. For subsequent labs, we
would suggest strategic checkpoints at which to `commit`. This fits in well
with the incremental development employed by the current write-ups. Later, the
idea of `branch`ing would be introduced to help encapsulate the development
process and the functional additions to each `class`.

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

+ What are the Pros and Cons of using GitHub and Git?
+ How setup the current lab folders to work with GitHub?
    + All that needs to be done, is to initialize a repository in the
      containing folder of the starter code, push it to the remote
      `PomonaCollege/cs051-FA201X` educational branch. When the starter code
      for each lab is to be published, the following commands will be run: 
```
git add LabXX-LabName
git commit -m “publish labXX”
git push
```
It would also be fairly straightforward to write a bash script to do this.
Something like the untested and script below:

```bash
publish_lab () {
    if [ -z $1  ]
    then
        echo “Parameter is of zero length”
    else
        git add ($1)*
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
+ Possible Workflow? (*This is a suggestion! There are many possible
  implementations of this model.*)
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

## The Good, the Bad, and the Merge Conflict

### Pros

+ Increased knowledge of industry workflow for beginning computer science students.
+ Simplified TA grading workflow
+ Reduced amount of folder naming complications
+ Inline code commenting feedback in the style of industry standard code review
+ Promote the development of sustainable, version-controlled code
+ Possibility for more collaborative projects
+ Easy for TA to provide feedback on student code outside lab sessions or mentoring hours without having to post to Piazza
+ Will reduced out Grade inflation
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

A couple of thoughts that we had, since this would only serve as an
introduction to Git, were to award extra credit points to students for
exceptional commit histories, or to make git usage a half or full point part
of the rubric to be taken away only in extreme circumstances of misuse.  

## References and Further Reading

+ [GitHub Cheat Sheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf)
+ [Employing Git in the Classroom](http://www.academia.edu/5968989/Employing_Git_in_the_Classroom)
+ [GitHub Official Education Guide](https://education.github.com/guide)
+ [`teachers_pet` Documentation](https://github.com/education/teachers_pet/#giving-others-access)
+ [GitHub + University: A Follow Up](https://joshldavis.com/2014/06/30/github-university-follow-up/)
+ [EGit (Eclipse Git) Documentation](http://www.eclipse.org/egit/documentation/)
+ [Difficulties of Using GitHub in the Classroom](https://github.com/education/teachers/issues/2)

[1](https://github.com/education/teachers_pet/#giving-others-access)
