# Bank Marketing Random Resampling

In this activity, you will use sampling techniques to balance the imbalanced bank marketing data.

## Instructions

Use the unsolved notebook to try at least two resampling techniques. You can use any resampling that we've learned, but remember to compare the final results of both methods to those of the original data!

1. Read the CSV file into a pandas DataFrame.

2. Separate the features `X` from the target `y`.

3. Encode the categorical variables from the features data using `get_dummies`.

4. Separate the data into training and testing sets.

5. Scale the data using `StandardScaler`.

6. Create and fit a `RandomForestClassifier` to the scaled training data.

7. Make predictions using the scaled testing data.

8. Import a sampler from `imblearn`.

9. Create and fit the sampler to the training data.

10. Check the `value_counts` for the resampled target.

11. Create and fit a `RandomForestClassifier` to the resampled training data.

12. Make predictions using the scaled testing data.

13. Generate and compare classification reports for the original data and the sampled data.

14. Repeat Steps 8 through 13 with a different sampler.

## Reference

Moro, S., Rita, P. & Cortez, P. 2012. *Bank marketing* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/222/bank+marketing [2023, October 17]. *Note that this data set has been modified/cleaned/shortened for the purpose of this activity. You can access the modified data in the CSV file provided.* ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
