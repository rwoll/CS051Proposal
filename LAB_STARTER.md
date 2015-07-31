Student Development Environment Setup
========

> NOTE: This guide assumes you already have a GitHub account. If you need to
> register for one, simply sign up [here](https://github.com).

1. Open Eclipse from the dock.
2. In the Git Repositories view, click the clone icon.
3. In the dialog box that appears, copy and paste the following 
   (after changing `<your-name>` to be your name) into the *URI* box:
```
https://github.com/PomonaCS051/<your-name>_fa2015
```
4. Type in your GitHub username where it says "User" and your GitHub
   password where it says "Password".
5. Click **Next >**.
6. Ensure the `master` branch is selected. Then click **Next >**.
7. In the *Directory* box, copy and paste the following:
```
~/CS051
```
8. Check the box next to *Import all existing Eclipse projects after clone
   finishes*. Then click **Finish**.
    > If Lab01 does not automatically appear in the package explorer,
    > expand the working directory in the Git Repositories pane 
    > and right-click to select *Import...*. Then hit next to accept the
    > default options.
9. Click the `Terminal` icon in the top menu bar.
8. Copy and paste the following into the window that appears
```
cd ~/CS051
```
Hit enter.

Then copy and paste the following:
```
python configure_git.py
```
Enter the information as it prompts you to and hit enter.
Once it says everything is complete, begin working on the lab!

