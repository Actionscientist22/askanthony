# Bank Targets and Metrics

## Introduction

In this activity you will start by discussing the implications of the chosen target column for the Bank Marketing dataset. Then, you'll discuss several potential metrics that could be used to evaluate the model, along with the implications of choosing each metric.

## Instructions

Discuss each of the following topics with your classmates.

### Target Column

1. What is the target column of the dataset actually measuring? Use the [UCI page](https://archive.ics.uci.edu/dataset/222/bank+marketing) for this dataset to find information about the target column and how the data was collected.

2. If a model becomes well trained in predicting this target, which of these statements can be made and which cannot?

    * The model can predict which clients will subscribe before any marketing efforts have been made.

    * The model can predict which clients currently in the marketing pipeline will eventually subscribe.

    * The model can predict which clients currently in the marketing pipeline have already subscribed.

3. Imagine you are meeting with the board of the bank. Given your answers to the previous question, how would you describe the use case of a model that is well trained on this dataset? Remember, your answers should be understandable by non-technical people.

### Metric Selection

1. Is the dataset balanced or imbalanced?

2. Given the use case described in the previous section, what is the risk associated with a false positive prediction? How about with a false negative prediction? Is the cost of one of the errors higher than that of the other?

3. What metrics would be best suited for this project given the answers to the previous questions?

4. Assume balanced accuracy is chosen by the managers of the project. Are there any caveats or risks you would make them aware of given that choice?

## References

Moro, S., Rita, P. & Cortez, P. 2012. *Bank marketing* [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/222/bank+marketing [2023, October 17]. *Note that this data set has been modified/cleaned/shortened for the purpose of this activity. You can access the modified data in the CSV file provided.* ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode))

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
