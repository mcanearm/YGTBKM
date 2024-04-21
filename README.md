# Project Outline

## Explanatory

* Caffeine
* Age
* Income (poverty level)
* Demographics (race/ethnicity)
* Occupation
* Work Physicality
* Exercise
* Diet
  * Soft Drinks
  * High Caffeine softdrinks
* Vices

## Response

1) Have you ever passed a kidney stone?

## Reproducing

### Setup

First, you’ll need to create a new conda environment from the requirements.txt file, by running 
```
conda create –name ygtbkm –file requirements.txt
```

After creating the proper environment with dependencies, first run `python paper/data/collect.py` script to
collect the NHANES data automatically. This will produce a file called `./data/full data.csv`. Then run the
script `python ./paper/data/prepare.py`, which will automatically prepare the dataset into a human readable form.
The final file will be called "prepared data.csv". This file is required for the EDA, random forest, and GAM
notebooks.

### Results

To reproduce the plots for the EDA run the `paper/eda/eda.ipynb`. To reproduce the random forest, its
associated plots, and its cross validation score see `paper/models/RF.ipynb`. To reproduce the GAM and its
associated plots and peformance scores, see `paper/models/pygam.ipynb`.
There is a certain amount of randomness to the GAM and RF in particular, but the results should be
similar from run to run.