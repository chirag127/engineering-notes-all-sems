# Git/GitHub

Git is a distributed version control system that allows you to track and manage the changes in your source code. GitHub is a code hosting platform that uses Git for version control and collaboration. In this tutorial, you will learn the basics of Git and GitHub, such as:

- What is a repository, a branch, a commit, and a pull request
- How to create and clone a repository on GitHub
- How to make changes and commit them to your local and remote repository
- How to create and merge branches
- How to create and review pull requests
- How to collaborate with others on GitHub

## Repository

A repository is a collection of files and folders that are related to a project. A repository can be hosted on GitHub or on your local computer. You can create a new repository on GitHub by clicking the "New" button on the top right corner of your dashboard. You can also clone an existing repository from GitHub to your local computer by using the `git clone` command.

## Branch

A branch is a parallel version of a repository that allows you to work on different features or tasks without affecting the main branch, which is usually called `master` or `main`. You can create a new branch by using the `git branch` command, and switch to a different branch by using the `git checkout` command. You can also create and switch to a new branch in one step by using the `git checkout -b` command.

## Commit

A commit is a snapshot of the changes you have made to your files in a branch. You can make a commit by using the `git commit` command, which will prompt you to enter a message describing the changes. You can also use the `git commit -m` command to enter the message directly. You can view the history of your commits by using the `git log` command.

## Pull request

A pull request is a request to merge the changes from one branch to another branch. You can create a pull request on GitHub by clicking the "Pull request" button on the repository page. You can then choose the base branch and the compare branch, and write a title and a description for the pull request. You can also add reviewers, assignees, labels, and projects to the pull request. Once the pull request is created, you and others can review the changes, leave comments, and approve or reject the pull request. You can merge the pull request by clicking the "Merge pull request" button on GitHub, or by using the `git merge` command on your local computer.

## Collaboration

GitHub allows you to collaborate with others on your projects by using features such as:

- Forking: You can fork a repository from another user or organization to create a copy of it on your own account. You can then make changes to the forked repository and create a pull request to the original repository.
- Issues: You can use issues to report bugs, request features, or ask questions about a repository. You can create a new issue by clicking the "Issues" tab on the repository page and then clicking the "New issue" button. You can also add labels, assignees, projects, and milestones to the issue.
- Discussions: You can use discussions to have conversations with other users about a repository. You can create a new discussion by clicking the "Discussions" tab on the repository page and then clicking the "New discussion" button. You can also choose a category, a title, and a body for the discussion. You can also reply to other discussions, react to comments, and mark comments as answers.
- Actions: You can use actions to automate tasks such as testing, building, and deploying your code. You can create a new action by clicking the "Actions" tab on the repository page and then clicking the "New workflow" button. You can then choose a template or create your own workflow file using YAML syntax. You can also view the status and logs of your actions by clicking the "Actions" tab.