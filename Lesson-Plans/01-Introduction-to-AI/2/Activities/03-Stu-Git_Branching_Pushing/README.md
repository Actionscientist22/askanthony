# Student Do: Git Branching and Pushing

## Introduction

In this activity, we will create a new branch, implement a feature, and then submit a pull request back into the main branch. We will also cover reviewing pull requests and merging them into the main branch.

## Instructions

### Part I: Branching and Submitting a Pull Request

In this section, we will create a branch, add a feature, and submit a pull request.

1. Clone the project repo onto your computer and use the `cd` (change directory) command to get into it.

2. Run the following command in your terminal to create and checkout to a new branch:

  `git checkout -b new-branch`

3. You should now be on a new branch named "new-branch." In order to verify that this worked, run the following command in your terminal:

  `git branch`

4. You should see two branches listed: `main` and `new-branch`. The `new-branch` branch should have an asterisk to the left of it. This indicates that this is the branch you're currently on.

5. At the root of the repo, create a new file named `README.md`. Inside this file, add some general text about creating a branch, and save.

6. In your terminal, add and commit the changes. Then push up your file by running the following in your terminal:

  `git push origin new-branch`

7. This should push up your file to GitHub on a branch with the same name (`new-branch`).

8. Go to the main repo page at github.com and you should see a button that says "Compare & pull request." Click this.

	![A button says "Compare & pull request](https://static.bc-edx.com/ai/ail-v-1-0/m1/lesson_2/img/pr-pushed.png)

9. On the next screen, add a description of the work that was done in the text area and click the "Pull Request" button.

	![Add a description of the work that was done in the text area.](https://static.bc-edx.com/ai/ail-v-1-0/m1/lesson_2/img/create-pull-request.png)


10. If completed successfully, you should see the pull request listed under the repo's "Pull request" tab.

### Part II: Reviewing a Pull Request

In this section, we will review the pull request from Part I and merge it into the main.

1. Clone the repo to your computer if you haven't already done so, and use the `cd` command to get into it.

2. First, you will want to test the changes introduced by the `new-branch` branch locally. To examine the new branch on your local machine, run the following commands in your terminal:

  `git fetch --all`

  `git checkout new-branch`

3. This code should bring the copy of the `new-branch` branch that is on GitHub onto your computer.

  * Make sure this worked by verifying that there's a `README.md` file in your local repo.

  * Typically, you would run the code here to make sure everything works properly.

4. Check back out to your local `main` branch by running the following in your terminal:

  `git checkout main`

5. Now go to your GitHub repo's main page and go to the "Pull request" section. Select the `new-branch` pull request from the list.

	![Select a the new branch pull request](https://static.bc-edx.com/ai/ail-v-1-0/m1/lesson_2/img/pr-list.png)

6. On the next page, select the option to see the "Files changed."

	![Select the files that have changed.](https://static.bc-edx.com/ai/ail-v-1-0/m1/lesson_2/img/changed-files.png)

7. You should be presented with all of the files that were changed in this PR, along with line numbers for any code added or removed.

	![All the files that have changed.](https://static.bc-edx.com/ai/ail-v-1-0/m1/lesson_2/img/review-pr.png)

8. If there are any changes you would like made, you can click the line number to leave a comment the PR author will see and should address before approval. Otherwise click "Review changes" and approve the PR. You should be taken to a screen with an option to "Merge pull request." Click this button.

	![Approving the PR](https://static.bc-edx.com/ai/ail-v-1-0/m1/lesson_2/img/approve-pr.png)

9. Once complete, you can delete the feature branch from your machine by running the following in your terminal:

  `git branch -D new-branch`

Ask an instructor or TA if you get stuck or have any questions!

---


© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
