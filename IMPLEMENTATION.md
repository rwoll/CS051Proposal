# Implementation Details

## Architecture
See [here]() for a detailed description of the codeflow

## Modifications to existing Codebase
All that needs to be done, is to initialize a repository, using Git or
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
## Workflow Comparison
### Proposed Workflow
  1. Professor pushes Eclipse project (with Readme instructions and working
    example`.jar` file) to the `upstream` GitHub repo.
  2. Student `pull`s the updated repository and creates a new branch called `labXX`
  3. Student adds, commits, and pushes their completed assignment to
    `origin/labXX`
  4. Student creates a Pull Request.
  5. TA clones repos 
  6. TA provides inline comments on the pull request and a grade in the final
     comment of the PR.  Once it has been graded the TA merges the PR and
     records the grade in the grade book. 
### Current Workflow
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


#### Grading
A few ideas regarding possible grading scenarios:
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


