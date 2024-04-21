# Setting Up Google Colab

In this activity, you will set up Google Colab and configure a notebook to use Prophet for time series forecasting.

**Hint:** You are encouraged to review the [Overview of Colaboratory Features](https://colab.research.google.com/notebooks/basic_features_overview.ipynb). This is a notebook created by Google as a quick start guide to Google Colab.

## Instructions

1. Open the [Google Colab URL](https://colab.research.google.com/) in your browser and create a new notebook.

2. Configure your Google Colab workspace to include the libraries that we will use in today's class. Copy the following Python code in four different code cells. When you are done, execute all the cells.

   Code cell 1:

    ```python
    # Install the required libraries
    !pip install prophet
    ```

   Code cell 2:

   ```python
   # Import the required libraries and dependencies
   import pandas as pd
   from prophet import Prophet
   import datetime as dt
   %matplotlib inline
   ```

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
