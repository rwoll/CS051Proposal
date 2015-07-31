Student Development Environment Setup
========

> NOTE: This guide assumes you already have a GitHub account. If you need to
> register for one, simply sign up [here](https://github.com).

1. Open Eclipse from the dock.
2. Clone the repository.
   1. Click on **File** *>* **Import** *>* **Git** *>* **Projects from Git**
   2. Click on **Clone URI** and **Next >**.
   3. In the **Source Git Repository** dialog box that appears, copy and paste
      the following into the *URI* box: 
      `https://github.com/PomonaCS051/fa2015.git`
   4. Type in your GitHub username where it says "User" and your GitHub
      password where it says "Password". Check the box next to "Store in Secure
      Store" and click **Next >**. 
   5. Ensure the `master` branch is selected. Then click **Next >**.
2. Copy the text in the *Directory* box. Paste it somewhere safe. Click **Next >**
3. Ensure the box next to Lab01 is checked. Then click **Finish**
    > If Lab01 does not automatically appear in the package explorer,
    > expand the working directory in the Git Repositories pane 
    > and right-click to select *Import...*. Then hit next to accept the
    > default options.
4. Click the `Terminal` icon !["terminal"](/eclipse_images/tm_icon.png) in the top menu bar.
5. Type `cd` + a space into the window that appears and copy the contents of
   you copied and saved in step 2.  It should look something like below. 
   ```
   cd /Users/cecilsagehen/git/fa2105
   ```  
   Hit return.  
   Then copy and paste the following:  
   ```
   sudo ython configure_git.py  
   ```
   Hit return.
   You will be prompted for your password.  Enter the password for the lab computer
   and hit return.
   Enter the remaining information as it prompts you to and hit return after each prompt.
6. Right click on the "Lab01 [fa2015 master]" project in the *Project Explorer*
   panel.  Then click on **Team** *>* **Show in Repositories View**.  The *Git
   Repositories* view should open.

**Once it says everything is complete, begin working on the lab!**
