# UHH2-datasets

Repository for dataset XML files to be used in [UHH2](UHH2/UHH2).
Split from main UHH2 code, since we now have datasets that can be used across mutliple branches, and we only want one centralised repository to handle these.


## Installation

Starting in `UHH2`:

```
cd common
# if necessary, rename the existing datasets directory: 
# mv datasets datasets-old 
git clone https://github.com/UHH2/UHH2-datasets datasets
```

## Committing

Datasets should be commit to the subdirectory corresponding to the branch name used to create them.
