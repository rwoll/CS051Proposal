# Sandboxing Repositories

## What is a Sandboxed Repository?

A Sandboxed Repo is one to which only one student has access (along with the 
TAs and Professors).  It is private, owned by the `PomonaCS051` GitHub
organization, and here, will be used to house student submissions. 

## How does it work?

GitHub provides some excellent tools that allow you to do this rapidly. Most
notably, a rubygem called `teachers_pet`. Its `create_repos` function allows
you to create private, sandboxed repo for each student, by performing the
following actions (taken directly from [Github's 
Site](https://education.github.com/guide/sandboxing#individual-projects).

For each student:
  1. Create a repository in the organization based on the student's name.
  2. Create a team in the organization, matching the name of the repository.
  3. Set that team to have Push/Pull permissions.
  4. Add the student to that team.
  5. Give that team access to the corresponding repository.


