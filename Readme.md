
Project for learning more advanced Git/Github.

Goals:
    - protecting main-branch.
    - CD/CI automated testing.
    - Pull requests to main from different branches.
    - Allow merging to main only if tests complete succesfully.
    - Create docker-container after tests complete succesfully.
    - Rebasing and appending to rewrite history to get rid of unnecessary commits.


- Added branch-protection for main-branch. Trying to push to main now...
- Pushing bypassed the protection... Turns out admins can bypass 
    branch protection rules if it has not been explicitly forbidden.

- Removed stupid updates.
- Added workflow for running stuff when pushing to main. Should happen only when merging via pull-request.
- Learned squashing small updates to one bigger by using git rebase -i HEAD~N
- Added github workflow for creating docker-image automatically when pushing to main.
- Added github workflow for sending docker-image to google artifact registery after creation.
