# Hyperparameter Tuning

In this activity, you'll use `GridSearchCV()` and `RandomizedSearchCV()` to choose the parameters for a K Nearest Neighbors (KNN) model on the numeric columns of the bank dataset.

## Instructions

1. Use the provided starter code, train an untuned KNN model, and print the classification report.

2. Create a parameters grid dictionary for the `n_neighbors`, `weights`, and `leaf_size` parameters. You can use any values that you want to try, but the notebook comments include suggested values.

3. Create and train a `GridSearchCV()` with a KNN model.

4. Print the best parameters and the classification report for the tuned model.

5. Create a random parameters grid dictionary for the `n_neighbors`, `weights`, and `leaf_size` parameters. You can use any values that you want to try, but the notebook comments include suggested values.

6. Create and train a `RandomizedSearchCV()` with a KNN model.

7. Print the best parameters and the classification report for the tuned model.

8. Document your interpretations of the results. Make sure to specify what the best settings were for each hyperparameter tested and how much improvement the tuning grids made to the accuracy of the model, but feel free to include other metrics in your report.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
