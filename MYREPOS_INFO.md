# Using `myrepos` for TAs

## What is `myrepos`?

`myrepos`, or `mr` for short, is a repository-managment tool that allows users
to manage and update all of the repositories on their machine with only a few
easy commands.

> To install `myrepo`, use homebrew by running `brew install myrepos`.

### Configure and Manage Grading Repositories.
Now that `mr` is installed, `cd` into the directory containing your grading 
repos. In each one, enter the command `mr register`.  Then in the parent
directory, run `mr up`.  This will update each registered repo with its remote
copy (default `origin`, but this can be configured). Then, in EGit, just 
import each remote into the workspace, as described [here](EGIT_USE.md). For 
each subsequent assignment, simply run mr `up` in any parent directory.  If for
some reason a specific repo cannot be updated, it will fail for that repo (and
that repo only), and the user will manually update that repo.

### How does it work?
`myrepos` keeps a registry of each git repository and its remote in the
`$HOME/.mrconfig` file. Then, for each of these, it calls `git pull --all`,
which fetches all remotes and merges the current branch's upstream.  This
can, of course, be configured to run any set of git commands.  For more info,
visit the [myrepos page](https://myrepos.branchable.com/).
