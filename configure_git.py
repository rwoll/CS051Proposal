#! /usr/bin/env python
import os

name = raw_input("Enter your name: ")
email = raw_input("Enter the email configured to your GitHub Account: ")
username = raw_input("Enter your GitHub username: ")


submission_remote = "https://github.com/PomonaCS051/" + username + "_fa2015"

os.system("git remote rename origin starter-code")
os.system("git remote add submission " + submission_remote)

os.system("git config user.name " + name)
os.system("git config user.email " + email)

os.system("git config alias.starterCode '!git checkout master; git pull starter-code master'")
os.system("git config alias.newLab 'checkout -b'")
os.system("git config alias.submit 'push -u submission'")
