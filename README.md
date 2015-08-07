GitHub + Eclipse: A CS051 Proposal
========

* * *
*This proposal has been compiled by [Ross W](mailto:ross.wollman@pomona.edu)
and [Eric C](mailto:eric.campbell@pomona.edu).*

Additional reading and implementation details are linked throughout the document.
To access these materials directly, browse the [resources](/resources) directory.
* * *

## The Proposal

Trial an experimental lab workflow that uses GitHub and [EGit](http://www.eclipse.org/egit/?replytocom=14044)
to optimize the lab **distribution-submission-feedback** (DSF) cycle for students,
TAs, and professors in one CS051 Lab section.

Git use in the CS051 lab cycle would improve student academic and career success by introducing them to the de facto industry-standard versioning tool; promote incremental and efficent programming, ameliorating the quality of their code; enrich the academic interaction between students, TAs, and professors by allowing for peer-reviewed, clear, and concise feeback; and reduce overhead by streamlining the DSF cycle.

With the [GitHub Education plan (Free)](https://education.github.com/discount_requests/new), 
all student code will be hosted in private repos. Only TAs, professors,  and 
the student will have access to view/edit their repository.
They will **NOT** be publicly visible nor will they be visible by other students.

A success in this experiment is defined by a decrease in overhead, an increase
in the quality of grading, and positive course evaluations. Upon success, we 
envision rolling this out across all lab CS051 sections.

## Personal Motivation

In our internships this summer, we learned the valuable, incremental
version-controlled code-production pattern employed by software companies who 
wish to produce code with low technical debt.  Namely Git version-control.
We hope to leverage elements of these workflows to optimize the CS051 lab cycle 
and share a baseline knowledge of an invaluable and ubiquitous tool.

Looking ahead, today's students will become tomorrow's TAs. Our goal is to create
a sustainable low-maintaince coding environment built on a foundation of high-quality 
collaboration between students, TAs, and professors.

## Overview: Why Consider GitHub?

### Simplicity: More Coding and More Feedback

Simply put, the ***entire*** distribution-submission-feedback cycle would be
optimized and reduced to **5** basic steps:

| Who              | Action                  | Description                   |
|:----------------:|:-----------------------:|:------------------------------|
| **Professor**    | `publish_lab lab47`     | *makes lab 47 available to all students* |
| **Student**      | `git starterCode && git newLab lab47`| *brings the latest assignment and starter code into the student's Eclipse environment and creates a branch for their work*|
| **Student**      | `git submit lab47`      | *pushes the student's work to GitHub for the TA to evaluate* |
| **TA**           | `get_student_code`      | *pulls an entire section's latest submissions from GitHub into the Eclipse environment* |
| **TA**           | [GitHub Commenting][1]  | *allows TA to comment directly on specific lines of student code and leave valuable feedback that the professors can also review and easily add to* |

> **NOTE:** All the student steps can be completed without leaving Eclipse.
> The actions are possible due to git aliasing. See the [explanation](/resources/EGIT_USE.md) or
> [this configuration file](/resources/configure_git.py) for further information.

From a TA or Professor's perspective, using GitHub could help **maximize the
feedback students receive** on their code by reducing the number of steps
in the grading process. It would simplify the collection of student projects
and facilitate the dissemination of feedback.

### Let us show you a quick demo

The `.gif` below shows a compilation of all of the overhead that will go into
the **distribution-submission-feedback** cycle for CS051.

!["example_gif"](/resources/cs051.gif)


### Transparency

With comments from students, TAs, and professors captured online by GitHub, 
course participants will have a history of their development throughout
the semester. This would eliminate the trail of hard-to-follow PDF code emails.

Professors can provide **quality assurance** by reviewing TA comments across the
lab sections, and TAs can view eachother's comments to ensure consistency.

Professors will have a clear view into the types of problems TAs find in student
code, allowing them to identify and address specific issues. An easily-accessible
history of student code and TA feedback will provide insight into student 
progress and developed habits throughout the semester.

### Dynamic Lab Materials

Another advantage of using GitHub in the development of this new workflow is
its role as a resource for TAs and professors. The source-controlled nature
of the `starter-code/master` repository allows TAs and professors to maintain and 
improve the documention on the use of Git and GitHub as a workflow ***simplification
and optimization tool***.

### The tl;dr: GitHub is Great

While in its simplest form, GitHub could serve as an
online dropbox that allows for more efficient distribution and collection of
assignments, there are many other features of Git and GitHub that could
enhance the CS051 distribution-submission-feedback cycle.

## *Git*-ing Into It: How Would this Work?

At the begining of the semester, the TAs would [setup private, sandboxed repositories](/resources/SANDBOXING.md)
for each student to which students would push their completed assignments. [Eclipse would
be configured with EGit](/resources/EGIT_USE.md), so **students can complete the entire process without leaving the
IDE.**

At the start of the first lab, students would have to follow something similar to
our [sample guide](/resources/LAB_STARTER.md) to get everything up and running.
After the initial setup, there are very few steps involved.

### General Architecture: The Repositories

![ArchitectureImage](/resources/architecture_v.png)

1. **Starter Code Repository** (GitHub): Professors would push new lab assignments to this
   repository that will be pull-only for students. This will end up becoming a
   collection of all the lab materials--setup instructions, exemplars, and starter-code.
   When an assignment is added, students will be able to easily
   and efficiently pull in the new updates directly into their Eclipse environment.
2. **Student Working Repositories** (Local): Each student will have a repository that
   contains their work on the assignments. This will be configured with Eclipse's
   EGit plugin to make the pushing and pulling updates out of Eclipse seamless.
   With a specifically designed remote scheme inspired by [this schools setup](https://joshldavis.com/2014/06/30/github-university-follow-up/), this repository will be able
   to easily pull in updates and new assignments from the Starter Code Repository.
   At the start of the semester students will follow [instructions](/resources/LAB_STARTER.md) to setup this
   repository and configure it with [this handy script](/resources/configure_git.py).
3. **Submission Repositories** (GitHub): These repositories are GitHub hosted duplicates*
   of the student working repositories. Each student will have a private, sandboxed
   repository. Since they are hosted on GitHub, students, TAs, and professors
   can take advantage of GitHub's commenting tools and [Pull Requests](https://help.github.com/articles/commenting-on-the-diff-of-a-pull-request/) as well
   as view their development online.
4. **TA Clones** (Local): TAs, for their first time grading, will clone the
   student GitHub repositories into EGit in Eclipse. This will allow for the grader to
   easily switch between compiling and running different student's code without
   the need to drag-and-drop source code.
   With one command they will be able to pull an entire lab sections submissions!

For more details on the inner workings of this architecture design, [view this section](/resources/ARCHITECTURE.md).

## EGit

EGit is an Eclipse Git plug-in that allows for the easy integration of a Git workflow into
the IDE and adds a GUI. It ships with the newer releases of [Eclipse](http://www.eclipse.org/downloads/packages/eclipse-ide-java-ee-developers/marsr)

With EGit, you can `ctrl`-click and import a single project or an entire repository
filled with multiple projects into Eclipse's standard Package Explorer.
Visual aids will also appear in the Package Explorer to depict a clear picture of
the Git status of each project asset.

When it's time to commit changes and push them to the grading repository, EGit provides
a simple dialog box to confirm which files are being added and to include a simple commit
message.

For more on the configuration of EGit in the proposed design, [view this section](/resources/EGIT_USE.md).

## Adaptations: Working with the Existent Assignments

The current labs (including write-ups, exemplars, and starter code) would simply need
to be published to the starter code repository each week for students to pull into their
workspaces and complete. The write-ups would be modified slightly to include instructions
that specify the Git related actions; these write-ups can be left in Html or rewritten
as Markdown for which GitHub has sleek rendering.

For more information on modifying the existing code base, view [this document](/resources/IMPLEMENTATION.md#modifications-to-existing-codebase).

## Case Studies

### [School of Engineering and Design, Institute of Technology (Ireland)](http://www.academia.edu/5968989/Employing_Git_in_the_Classroom)

#### Motivation

> "Additionally, within the classroom, there is increasing  pressure on contact
  time with students prompting a refocus on more efficient means of
  communication from lecturer [or TA] to student - and from student to lecturer
  [or TA]. In parallel, a move towards the ‘flipped model’ of student learning
  benefits from a quick, efficient mechanism to round-trip student and lecturer
  exercises back and forth."
> *- John Kelleher*

#### Academic Honesty

> "The issue of substantiating any allegation of plagiarism is fraught. Ideally
  an interview will secure evidence of plagiarism  but may not be practicable
  or cost-effective. However, when work completed by the student is regularly
  pushed to the hosting service, the activity is clearly visualised. Indeed,
  the sudden appearance of an established solution as a single commit served
  to draw attention to the submission, effectively acting as a
  plagiarism alert."
> *- John Kelleher*

#### Drawbacks of GUIs

> "The GUI tools held much promise but were not well received. From feedback
  from students, it appeared that though visually attractive, the range of
  features served to their confound their nascent understanding."
> *- John Kelleher*

### [Iowa State University: Principles of Programming Languages Course](https://joshldavis.com/2014/06/30/github-university-follow-up/)

#### Distributing Assignments

> "Releasing new homeworks was dead simple. One of the TA’s or the instructor
  would just add a new folder containing the homework files to the main repo."
> *- Josh Davis*

#### Resolving Issues 

> "The great thing is that while the questions were plentiful during Homework
  0, by the time of the first real homework a small percentage of students
  still had issues."
> *- Josh Davis*

#### Overall Thoughts

> "If I had to be a TA again, I would pick to use GitHub in a heartbeat. It
  saved us a ton of time in not only releasing homeworks but grading them."
> *- Josh Davis*

## What Could Go Wrong?

#### Merge Conflicts

With the design of the starter code repository and the instructions for how to use
Git, we hope to avoid as many merge conflicts as possible. However, they may arise
and when they do, students may be uncomfortable resolving them, so TAs and professors
might need to provide assistance.

Fortunately, EGit provides a GUI merge conflict resolution
[tool](http://wiki.eclipse.org/EGit/User_Guide#Resolving_a_merge_conflict)
that will facilitate the process.

As long as students commit code and push it to GitHub, TAs and professors could help
resolve these remotely and have students pull in the changes or reclone the remote
repository.

#### Student Assests Don't Make It Into Eclipse

On projects where students include graphics or audio for extra credit, they will have
to make sure the additional assets get copied into their working directory.

#### Students Could Tamper with Commit Timestamps

Students could fake commit histories to make it look like they've handed something in
prior to their actual submission time. A simple solution is for TAs to clone student 
code soon after the lab deadline so the commit history is protected.

#### Personal Machine Support

Setting everthing up on Macs would be easy since the lab computer instructions will
apply. On Windows machines, the setup would require a few more steps to get Git up
and running. 

#### *Git*-ing Distracted

If not carefully explained in instructions, using Git in the workflow could distract from
the CS051 curriculum. In an effort to avoid this and provide a level of abstraction between
Git and our use-case, we have written custom [aliases](/resources/EGIT_USE.md#terminal-or-gui) so students
don't have to spend time learning Git.

#### Where's My Code?

Students may forget to push code to GitHub for grading and leave it local. To mitigate this,
students would be instructed to log on to GitHub after they have submitted an assignment to
ensure that it is all there. If they have an issue, they can open an issue right from GitHub
and tag the grading team to have them be notified and take a look.

## Implementation Details

This section contains links to tested scripts and documents that we have compiled
to explain all the details of implementation.
+ [Architecure Details](/resources/ARCHITECTURE.md)
+ [EGit Use](/resources/EGIT_USE.md)
+ [Sandboxing with `teachers_pet`](/resources/SANDBOXING.md)
+ [Student Lab Configuration](/resources/LAB_STARTER.md)
+ [Repository Remote and Alias Configuration Script](/resources/configure_git.py)
+ [Screenshots](/resources/SCREENSHOTS.md)

## The Good, the Bad, and the Merge Conflict
+ [Pros and Cons Comparison](/resources/PROS_CONS.md)
+ [Current vs. Proposaed Workflow Comparison](/resources/IMPLEMENTATION.md#proposed-workflow)

## *Git*-ing It Ready: Necessary Steps

> If the CS051 faculty are interested in implementing the proposed workflow to part or 
> all of a lab section, Ross and Eric would be happy to set up a demo and refine the
> documentation further.
> 
> We have tested the general architecture in a local environment
> and are confident, through research and partial testing, that the local simulation
> will scale as desired.

1. Create a Pomona College GitHub organization and apply for the GitHub Education offer.
   (Approval takes 1-2 weeks.)
2. Configure lab computers by installing a distribution of Eclipse that has EGit
   bundled in, or install the EGit plug-in seperately.
3. Once the Github for Education is approved, create a `cs051-fa2015` repository belonging 
   to the Pomona College organization, and push the first lab.
4. On or prior to the first day of lab, have participating students register for a GitHub account,
   and collect their GitHub usernames. Once these are collected, the sandboxed repositories can be 
   set up with `teachers_pet`.

> Eric and Ross would be able to complete step 3 and part of step 4 (setting up the sandboxed repos).

* * *

## References and Further Reading
+ [Employing Git in the Classroom](http://www.academia.edu/5968989/Employing_Git_in_the_Classroom)
+ [GitHub Official Education Guide](https://education.github.com/guide)
+ [`teachers_pet` Documentation](https://github.com/education/teachers_pet/#giving-others-access)
+ [GitHub + University: A Follow Up](https://joshldavis.com/2014/06/30/github-university-follow-up/)
+ [EGit (Eclipse Git) Documentation](http://www.eclipse.org/egit/documentation/)
+ [Difficulties of Using GitHub in the Classroom](https://github.com/education/teachers/issues/2)
+ [GitHub Cheat Sheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf)
+ [Eclipse IDE Download with EGit](http://www.eclipse.org/downloads/packages/eclipse-ide-java-ee-developers/marsr)
 
[1]: https://help.github.com/articles/commenting-on-the-diff-of-a-pull-request/

