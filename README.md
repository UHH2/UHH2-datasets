# UHH2-datasets

Repository for dataset XML files to be used in [UHH2](UHH2/UHH2).
Split from main UHH2 code, since we now have datasets that can be used across mutliple branches, and we only want one centralised repository to handle these.

Currently, this repository is only designed to be used for `RunII_102X_v*`, and `RunII_106X_v*` datasets.

## Installation

First, fork the UHH2-datasets repository to your github.

Then, starting in `UHH2`:

```
cd common/datasets
git init
gname=$(git config --get user.github)  # or manually set it to your github name
git remote add origin "https://github.com/$gname/UHH2-datasets"
git remote add UHH https://github.com/UHH2/UHH2-datasets
git fetch origin
git reset --hard origin/master
```

Note that the `git reset` here just resets all the tracked files (i.e. all those in UHH2-datasets) to their state in the UHH2-datasets repository.
Note that any uncommitted changes may be lost!

At this point, if you do `git status`, you should see under "Untracked files" any files/changes that have not been committed to the UHH2-dataset repository.
You should commit them, and if applicable, make a Pull Request against the UHH2 repository centrally.

## Committing

Datasets should be commit to the subdirectory corresponding to the branch name used to create them.


## Porting commits/XML from UHH2

Ideally, we want to not only copy the XML files, but their history as well.
To get commits from UHH2, use the excellent git-filter-repo tool: https://github.com/newren/git-filter-repo

For a given UHH2 branch & XML directory, we can get only the relevant commits in UHH2, and merge them into here.

We create a copy of UHH2 on the relevant branch, then rewrite history to only get the relevant commits.

- Clone new copy of UHH2, since this is destructive, e.g.

```
git clone -b RunII_102X_v2 https://github.com/UHH2/UHH2.git UHH2-2
```

- Get commits that apply to directories, and rename the directory structure (since we don't want `common/datasets` here):

```
git filter-repo --path common/datasets/RunII_102X_v2/2016v3/ --path common/datasets/RunII_102X_v2/2017/ --path-rename 'common/datasets/RunII_102X_v2':'RunII_102X_v2'
```

note that we do all the individual subdirs, otherwise we also end up with common/datasets/RunII_102X_v1 for some reason

- Note that you may have to tidy up if commits modified other dirs, e.g.

```
git filter-repo --path core/ --invert-paths
```
- You should check git log/hist to make sure history doesn't include other commits


Now in UHH2-datasets:

- Add the UHH2 clone as a remote:

```
git remote add git remote add repo-A-branch <path>/<to>/UHH2-2
```

- Then pull the rewritten branch:

```
git pull repo-A-branch RunII_102X_v2 --allow-unrelated-histories
```

- Then tag the merge:

```
git tag -a "RunII_102X_v2" -m "Import RunII_102X_v2"
```
