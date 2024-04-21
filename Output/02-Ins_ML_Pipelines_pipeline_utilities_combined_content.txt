from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

def preprocess_rent_data(rent_df):
    """
    Written for rent data; will drop null values and 
    split into training and testing sets. Uses price
    as the target column.
    """
    raw_num_df_rows = len(rent_df)
    rent_df = rent_df.dropna()
    remaining_num_df_rows = len(rent_df)
    percent_na = (
        (raw_num_df_rows - remaining_num_df_rows) / raw_num_df_rows * 100
    )
    print(f"Dropped {round(percent_na,2)}% rows")
    X = rent_df.drop(columns='price')
    y = rent_df['price'].values.reshape(-1, 1)
    return train_test_split(X, y)

def preprocess_rent_data_keep_na(rent_df):
    """
    Written for rent data; will split into training
    and testing sets. Uses price as the target column.
    """
    X = rent_df.drop(columns='price')
    y = rent_df['price'].values.reshape(-1, 1)
    return train_test_split(X, y)

def r2_adj(x, y, model):
    """
    Calculates adjusted r-squared values given X and y sets 
    and the model used for the predictions.
    """
    r2 = model.score(x,y)
    n_cols = x.shape[1]
    return 1 - (1 - r2) * (len(y) - 1) / (len(y) - n_cols - 1)

def check_metrics(X_test, y_test, model):
    """
    Calculates and displays MSE, r-squared, and adjusted 
    r-squared values, given X and y test sets, and the 
    model used for predictions.
    """
    # Use the pipeline to make predictions
    y_pred = model.predict(X_test)

    # Print out the MSE, r-squared, and adjusted r-squared values
    print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred)}")
    print(f"R-squared: {r2_score(y_test, y_pred)}")
    print(f"Adjusted R-squared: {r2_adj(X_test, y_test, model)}")

    return r2_adj(X_test, y_test, model)

def get_best_pipeline(pipeline, pipeline2, rent_df):
    """
    Accepts two pipelines and rent data.
    Uses two different preprocessing functions to 
    split the data for training the different 
    pipelines, then evaluates which pipeline performs
    best.
    """
    # Apply the preprocess_rent_data step


    # Fit the first pipeline


    print("Testing dropped NAs")
    # Print out the MSE, r-squared, and adjusted r-squared values
    # and collect the adjusted r-squared for the first pipeline


    # Apply the preprocess_rent_data_keep_na step


    # Fit the second pipeline


    print("Testing no dropped data")
    # Print out the MSE, r-squared, and adjusted r-squared values
    # and collect the adjusted r-squared for the second pipeline


    # Compare the adjusted r-squared for each pipeline and 
    # return the best model


def rent_model_generator(rent_df):
    """
    Defines a series of steps that will preprocess data,
    split data, and train models for predicting rent prices
    using linear regression. It will return the best trained model
    and print the mean squared error, r-squared, and adjusted
    r-squared scores.
    """
    # Create a list of steps for a pipeline that will one hot encode and scale data
    # Each step should be a tuple with a name and a function
    steps = [("One hot encode", OneHotEncoder(handle_unknown="ignore")), 
             ("Scale", StandardScaler(with_mean=False)), 
             ("Linear Regression", LinearRegression())] 

    # Create a pipeline object


    # Create a second pipeline object


    # Get the best pipeline


    # Return the trained model
    return 

if __name__ == "__main__":
    print("This script should not be run directly! Import these functions for use in another file.")

    




