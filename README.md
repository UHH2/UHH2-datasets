# UHH2-datasets

Repository for dataset XML files to be used in [UHH2](UHH2/UHH2).
This has been separated from the main UHH2 code, since we now have datasets that can be used across multiple branches, and we only want one centralised repository to handle these datasets.

Currently, this repository is only designed to be used for `RunII_102X_v*`, and `RunII_106X_v*` datasets.
Please only make Pull Requests for those ntuples.

## Installation

This has to be done once in your existing UHH2 repository.

First, fork the UHH2-datasets repository to your github (see https://help.github.com/en/github/getting-started-with-github/fork-a-repo if unsure what to do).

Then, starting in your `UHH2` directory:

```
cd common
git clone https://github.com/<your github username>/UHH2-datasets.git
cd UHH2-datasets
git remote add UHH2 https://github.com/UHH2/UHH2-datasets.git 
git fetch UHH2
git branch -u UHH2/master
```

Note that the last commands adds and tracks `master` branch of the central UHH2 copy of the repository. This means you can easily pull from it with `git pull`.

:exclamation: **Important** you should update your XML files to use the new `common/UHH2-datasets` directory, instead of the old `common/datasets`.

## Committing & Pull Requests

Datasets should be commit to the subdirectory of UHH2-datasets corresponding to the branch name used to create them.

To push changes to the main repository, you should push to a branch on your fork (i.e. `git push origin mybranch`), and then make a Pull Request against the main UHH2 repository.


--------------------------------------------------------------------------------

## Copying commits/pull requests from UHH2

Sometime you may need to copy a commit from the main UHH2 repo. 
Ideally this is done retaining the original committer/timetstamp/commit message.

The easiest way is to generate a git patch, and then use `git am`.

e.g. from Pull Request #1476:

```
wget https://patch-diff.githubusercontent.com/raw/UHH2/UHH2/pull/1476.patch
sed -i 's|common/datasets/||g' 1476.patch
git am 1476.patch
```

Note that the `sed` command is necessary to update the paths (since in UHH2 it will be in `common/datasets/RunII_...`, whilst for this repository is is just `RunII_...`)
