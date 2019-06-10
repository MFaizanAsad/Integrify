---
title: 04 - Git 1-on-1
root: '/modules/module-0'
tree: '00 - Prerequisites'
module: module-0
---

# 04. Git 1-on-1

## TASK:

Simulate through and run all the main commands in the GIT Pipeline. We are going to talk about the results tomorrow, Tuesday.

** What I need from each student**:
Proof that you have done the assignment, meaning the list of commands that you have used to test out all the learned GIT commands. Also attach screenshots from your GIT Console command history.

**Commands and operations to do** :
* Set up GIT account locally and remotely
* Configure GIT Terminal (git config)
* Create at least one GIT repository and 2 branches

**Commands to use**:
* add (one, multiple, all)
* commit
* checkout
* branch
* clone
* fetch
* Fork
* HEAD
* merge
* push (to remote)
* pull (updating local repository)
* add remote
* stash (stash changes)
* Tag
* Setting
* Log
* status

### Pycharm part : After you have finished all the operations in GIT Console, do all the same in *PyCharm* editor. Pycharm has inbuilt support for Version Control Systems (VCS).

------------------------------------------------------

Git is a version control system (VCS).

Ok, but **WHAT** actually is a VCS then and why would we need it?

> Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. So ideally, we can place any file in the computer on version control. It allows us to revert files back to a previous state, revert the entire project back to a previous state, review changes made over time, see who last modified something that might be causing a problem, who introduced an issue and when.

Git is a _distributed_ VCS so it doesn't rely on a central server but instead, every user "clones" a copy of a repository (a collection of files, usually means a project) and has the full history of the project on their own hard drive. This clone has all of the metadata of the original while the original itself is stored on a self-hosted server or a third party hosting service like GitHub and BitBucket.

## Git terms

Before jumping into command examples, let's have a look at the terms and their explanations Git uses.

### Branch

A version of the repository that diverges from the main working project. Branches can be a new version of a repository, experimental changes, etc.

### Checkout

The Git checkout command is used to switch branches in a repository. `Git checkout development` would take you to the development-branch whereas `Git checkout master` would take us back to the master branch.

### Cherry-picking

When cherry-picking a commit in Git, we're taking an older commit, and rerunning it at a defined location. Git copies the changes from the original commit, and then adds them to the current location. [Read more on stackoverflow](https://stackoverflow.com/questions/9339429/what-does-cherry-picking-a-commit-with-git-mean)

### Clone

A clone is a copy of a repository. When cloning a repository into another branch, the new branch becomes a remote-tracking branch that can talk [upstream](#upstream) to its origin branch (via [pushes](#push), [pulls](#pull), and [fetches](#fetch)).

### Fetch

By performing a Git fetch, we're downloading and copying that branch’s files to our workstation. Multiple branches can be fetched at once, and one can rename the branches when running the command to suit ones needs.

### Fork

Creates a copy of a repository. Usually done in hosting service (cloud).

### HEAD

HEAD is a reference variable used to denote the most current commit of the repository in which we're working. When we add a new commit, HEAD will then become that new commit.

### Index

The working - or staging - area of Git. Files that have been changed, added and deleted will be staged within the index until we're ready to commit the files. To see what is set in out Git index, we should run Git status within our repository. The green files are staged and ready to commit, whereas the red files have not yet been added to staging for the next commit.

### Master

The primary branch of all repositories. All committed and accepted changes should be on the master branch. One can work directly from the master branch, or create other branches which is the preferred way.

### Merge

Taking the changes from one branch and adding them into another branch. These commits are usually first requested via pull request before being merged by a project maintainer / PR reviewer.

### Origin

The conventional name for the primary version of a repository. Git also uses origin as a system alias for pushing and fetching data to and from the primary branch. For example, `Git push origin master`, when run on a remote, will push the changes to the master branch of the primary repository database.

### Pull Request / PR

If someone has changed code on a separate branch of a project and wants it to be reviewed to add to the master branch, that someone can put in a pull request. Pull requests ask the repo maintainers to review the commits made, and then, if acceptable, merge the changes upstream.

### Push

Updates a remote branch with the commits made to the current branch. A literal "push" will happen onto the remote.

### Rebase

When rebasing a Git commit, one can split the commit, move it, squash it if unwanted, or effectively combine two branches that have diverged from one another.

### Remote

A copy of the original branch. When cloning a branch, that new branch is a remote or a clone. Remotes can talk to the origin branch as well as other remotes for the repository, to make communication between working branches easier.

### Repository ("Repo")

In many ways, one can think of a Git repository as a directory that stores all the files, folders, and content needed for a project. What it actually is, is the object database of the project, storing everything from the files themselves, to the versions of those files, commits, deletions, et cetera. Repositories are not limited by user, and can be shared and copied (see: [form](#fork)).

### Stash

While working with Git, one may need to make multiple changes to files, but maybe not all changes should to go in one commit. If we want to pause the changes we're working on now in favor of working on another issue or improvement, we can "stash" our changes, essentially clearing them from the staging area until the changes are called again. We can only stash one set of changes at a time. To stash our staging area we'll use `Git stash [files]`; to retrieve the stashed files, we'll run `Git stash pop`. We can also clear the stashed files with `Git stash drop`.

### Tag

Tags are used to define which portions of a project’s Git history is most important. Often this is used to note point releases of a project. Tags can be added to the commit we're working with or added after-the-fact when needed.

### Upstream

While there is not necessarily a default "upstream" or "downstream" for Git projects, upstream can be considered where one pushes Git changes — this is often the master branch of the project within the origin.

## Basic Git-workflow

Before intialization or cloning anything, we need to configure Git to use our name and email address. This is important because every Git commit uses this information automatically to track down who made the changes and when.

```bash
$ Git config --global user.name "My Name"
$ Git config --global user.email myname@example.com
```

There's much more which can be configured as the above was the absolute minimun. More configuration options can be found [here](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).

### Starting from scratch

If starting from scratch, we'll introduce `Git init` command in our project folder which creates a hidden `.Git` folder. This folder is the place where Git stores all of its internal tracking data. Any changes made to any files within the original folder will now be possible to track.

### Existing project / repo

Getting an existing project to our local filesystem is as easy as introducing a "clone" command, which downloads all the files and metadata and one can start to make changes right away.

Our local repository now consists of three "trees" maintained by Git:
1. **Working Directory**, which holds the actual files
2. **Index**, which acts as a staging area
3. **HEAD**, which points to the last commit we've made.

### Add / modify files

After adding new / modifying files, we need to add them to **Index** by running

```bash
$ git add <filename> # this adds just the exact file
```

or

```bash
$ git add * # this adds every modified file
```

Now the new / modified files are in index, but not _committed_ to **HEAD** yet. To fix this, let's create a _commit_:

```bash
$ git commit -m "Introduces two new files: foo.py and bar.py" # The -m switch means message and it should be a self-explanatory about what this commit does.
```

### Pushing to remote

After committing, the files are now in **HEAD**. To let other collaborators interact with the code, we need to push them to _remote_.

If we _cloned_ an existing repository, the next step can be skipped, but if we started from scratch Git doesn't know yet where does the remote live and needs to be instructed:

```bash
$ git remote add origin <server_address> # Attach a remote-server to this repo. server_address can be obtained after creating a repo on hosting service.
```

Now we can _push_ the local changes to the remote by running

```bash
$ git push origin master # this pushed our "master" branch to the remote. If we added our changes to some other branch, we'd need to change the master to the name of our branch. To push all branches we'd use the --all (all local branches) instead of the branch name.
```

### Branches

**Branches** are used to develop features isolated from each other. The master branch is the "default" branch when a new repo is created. We use other branches for development and merge them back to the master branch upon completion usually via **Pull Requests**.

Let's create a new branch. Branch is created from the current branch we're in, so in this case it'd be "master"

```bash
$ git checkout -b feature/descriptive-feature-name # Create (-b) and checkout a branch named "feature/descriptive-feature-name"
```

To navigate between existing branches we simply need to type

```bash
$ git checkout <branchname> # Note the checkout without -b switch.
```

A list of branches can be viewed with

```bash
$ git branch # If we'd like to view all branches (remote & local) we'd add the -a (all) swicth to the command
$ git branch -a
```

### Update

After committing and pushing to remote, we expect also some other contributors to make changes. Updating our local repo with the changes is done with

```bash
$ git pull # pull fetches the changes from remote and merges them to our local repo
```

### Merge

After our `feature/descriptive-feature-name` is done (and preferrably we've created a pull-request which was approved by other contributors) it gets merged (usually to master). To make the merge, let's first navigate to our _master_ branch and after that make the merge

```bash
$ git checkout master # we're now on the master-branch
$ git merge feature/descriptive-feature-name # merge merges always to active branch
```

### Tagging

After the feature has been merged to the master it's time to create a release. Release is done by _tagging_ the current state

```bash
$ git tag 0.1.0 # tag with version 0.1.0
$ git push origin --tags # push all tags to remote
```

Note that [Semantic versioning](https://semver.org/) is commonly used pattern on versioning.

It's also possible to tag commits done by earlier. Previous command is appended with the commit-checksum which can be obtained with

```bash
$ git log --pretty=oneline # display the commit log
9f00c501fd70c63f27b4665d6bd06c5abe889fe9 Vars, Ints & REPL
f1d7189cfdf7d5671720ae4e60ec70fb20f491a1 Update Jupyter Labs
5a3c4deab48f1f3c7a8112798de4f16e59856f8b Update install python & tools
bfdc6edc98c78a663a519c7bc6ab3ba0f5e2135a Add basic instruction to what is python
933e242cb0588c4e29accead7017da49a01f8008 Installing Python & Pipenv
7e87de782b19f78ee82e28e71059ac0b687da10e Add module-0 & module-1 titles
```

Now, if we'd want to tag the commit _"Add basic instruction to what is python"_ we'd need to use the checksum (the weird part before every commit message) with the tag command:

```bash
$ git tag 0.2.0 bfdc6edc98c78a663a519c7bc6ab3ba0f5e2135a # Tag a specific commit with version-tag 0.2.0
```

### Log

To see a list of what happened in the repo, Git has a `log` command

```bash
$ git log # Output a full log
$ git log --pretty=oneline # Output a minimized version of the log, showing only the checksum and commit message
$ git log --author=<username> # Output commits made by <username>
```

### Status

To see the current status (modified file, new files, etc.), `git status` provides information we need:

```bash
$ git status # Output a full status
$ git status -s # Output simplified status which shows only the bare minimun
$ git status -b <branch_name> # Output status of different branch without checkout
```

### Blame

Sometimes it's useful to see who made a change to file and when so we can actually "blame" them for doing it :)

```bash
$ git blame <filename> # See all the changes made to <filename> per author
```

## Conclusion

Git is a powerful tool and it takes a while to master it. Above instructions will get us started and points to the right direction. If we're unsure what a command does or which configuration properties it offers, it's always good to use `git <commandname> --help` to see instructions.

It's also possible to use Git with GUI (Graphical User Interface) tools, such as [SourceTree](https://www.sourcetreeapp.com/) or [GitKraken](https://www.gitkraken.com/) but before jumping into these, let's make sure we know how to use Git with plain command-line.
