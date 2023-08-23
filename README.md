# Analysis of the competitions from CodaLab Platform.

1. In order to generate scores of utility of the competitions, one needs to run `leaderboard_cleaning.ipynb`, which consists mainly of two functions:

* `check_score(db)` outputs score_column - the column/feature to be used to calculate utility metric (ideally it should be the score used to rank participants on the leaderboard), score_function - indicates whether the score is to be maximised, minimised or neither.
* `score_db(folder)` returns two dataframes with the following features: 'link', 'utility_mean', 'utility_median'. It saves the two DataFrames as csv files in `data` folder. df_max is a partial copy of df with only completitions where the score is to be maximised.

2. Second file `codalab_3108.ipynb` is used for the analysis of the competitions. Mainly it consists of descriptive statistics, different graphs, correlation matrices and Feature importances with a forest of trees.

As it required a lot of manual checking, merging of utility metric to the main `CodaLab_3108` file was done manually. Some problematic cases from leaderboard data was save to `data/pb` folder. In orde to adresse the issues it is recommended to update `download_leaderboard.py` or other necessary files in `utilities` in order to fix the automatic recuperation of leaderboard data. Most common current issues with leaderboard: results of several tasks integrated in one leaderboard data.

As for the results of the analysis:

* no strong correlation between metric of utility (u_mean and u_median) and other features was revealed. 
* Feature importance however has showed that following features are significant: `reward_USD`, `participants`, `submissions`, `submission_per_participant`.

According to the latest data-centric approach (please check out Andrew Ng's talk https://www.youtube.com/watch?v=06-AZXmwHjo), maybe more attention should be braught to the quality of data. Even though the data set itself is relatively small (around 800 competitions), greater attention should be braught to the quality: additional data consistency check-up, implementation of some NLP to descriptive features, etc.

### Acknowledgements

The data collection and analysis was done by [Aleksandra Kruchinina](https://www.linkedin.com/in/aleksandra-kruchinina-36132246).
