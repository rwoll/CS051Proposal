#! /usr/bin/env python
import os

# get student information to use with git config commands
name = raw_input("Enter your name: ")
email = raw_input("Enter the email configured to your GitHub Account: ")
username = raw_input("Enter your GitHub username: ")

# the remote that points the students sandboxed repository
submission_remote = "https://github.com/PomonaCS051/" + username + "_fa2015"

# add and rename remotes for clarity when pushing and pulling
os.system("git remote rename origin starter-code")
os.system("git remote add submission " + submission_remote)

# configure students info if it already been done through EGit
os.system("git config user.name " + name)
os.system("git config user.email " + email)

# create aliases to simplify the most frequently used commands with
# the designed architecture

# allows for students to pull in the new assignments with `git starterCode`
os.system("git config alias.starterCode '!git checkout master; git pull starter-code master'")

# allows students to begin working on the new assignment on a new
# branch with `git newLab labXX`
os.system("git config alias.newLab 'checkout -b'")

# allows student to push their assignment with `git submit`
os.system("git config alias.submit 'push -u submission'")
