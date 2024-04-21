# Assessing Market Opportunities for Alpaca Wool Scarves: Time Series Forecasting

In this activity, you’ll use time series forecasting to analyze Google Trends data. The objective is to validate market opportunities that will assist the Aymara indigenous people in Bolivia in exporting alpaca wool scarves to various countries or regions.

While continuing your collaboration with the International Cooperative Alliance, you'll employ Prophet to validate potential market opportunities

## Instructions

1. Open [Google Colab](https://colab.research.google.com/), and import the provided notebook.

2. Run the initial code cells to set up and prepare the data.

3. Create two Prophet models, one for each country.

4. Fit the Prophet models.

5. Use the `make_future_dataframe` function to forecast one year of trend dates.

   **Hint:** Google Trends data is collected weekly, so set the `freq` parameter to `W`, and set `periods=52` (because 1 year has 52 weeks).

6. Predict the future trends data by using the `predict` function for both the Canada and Uruguay models.

---

© 2023 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
