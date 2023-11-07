import git
import os

repo = git.Repo('.')
branches = repo.branches
for branch in branches:
    if branch.name != 'HEAD':
        repo.git.checkout(branch.name)
        if os.path.exists('dell'):
            print(branch.name)