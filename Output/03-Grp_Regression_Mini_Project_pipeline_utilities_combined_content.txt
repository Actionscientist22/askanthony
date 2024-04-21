from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

def preprocess_prod_data(prod_df):
    """
    Written for productivity data; will drop null values and 
    split into training and testing sets. Uses actual_productivity
    as the target column.
    """
    df = prod_df.dropna()
    X = pd.get_dummies(df.drop(columns='actual_productivity'))
    y = df['actual_productivity'].values.reshape(-1, 1)
    return train_test_split(X, y)

def r2_adj(x, y, model):
    """
    Calculates adjusted r-squared values given an X variable, 
    predicted y values, and the model used for the predictions.
    """
    r2 = model.score(x,y)
    n = x.shape[0]
    p = y.shape[1]
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)

def prod_model_generator(prod_df):
    """
    Defines a series of steps that will preprocess data,
    split data, and train a model for predicting actual productivity
    using linear regression. It will return the trained model
    and print the mean squared error, r-squared, and adjusted
    r-squared scores.
    """
    # Create a list of steps for a pipeline that will one hot encode and scale data
    # Each step should be a tuple with a name and a function
    steps = [("Scale", StandardScaler(with_mean=False)), 
             ("Linear Regression", LinearRegression())] 

    # Create a pipeline object
    pipeline = Pipeline(steps)

    # Apply the preprocess_rent_data step
    X_train, X_test, y_train, y_test = preprocess_prod_data(prod_df)

    # Fit the pipeline
    pipeline.fit(X_train, y_train)

    # Use the pipeline to make predictions
    y_pred = pipeline.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2_value = r2_score(y_test, y_pred)
    r2_adj_value = r2_adj(X_test, y_test, pipeline)

    # Print out the MSE, r-squared, and adjusted r-squared values
    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2_value}")
    print(f"Adjusted R-squared: {r2_adj_value}")
    if r2_adj_value < 0.4:
        print("WARNING: LOW ADJUSTED R-SQUARED VALUE")

    # Return the trained model
    return pipeline

if __name__ == "__main__":
    print("This script should not be run directly! Import these functions for use in another file.")

    




