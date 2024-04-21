# Import required modules
import pandas as pd
import tensorflow as tf

# Function to import and preprocess the data
def get_data():
    df = pd.read_csv("https://static.bc-edx.com/ai/ail-v-1-0/m18/lesson_3/datasets/ratings.txt",
                     sep=" ",
                     header=None,
                     names=["user_id", "movie_id", "rating"])
    df = df.drop_duplicates(subset=["user_id", "movie_id"], keep="last")

    return df

# Function to normalize the data
def normalize_data(df):
    # Create variable for normalization
    # Ratings are between 0-5
    normalization_factor = 5

    # Normalize the ratings
    normalized_ratings = df / normalization_factor

    return normalized_ratings

# Function to pivot the data
def pivot_data():
    df = get_data()
    # Pivot the DataFrame and fill NAs
    ratings_matrix = df.pivot(index="user_id", columns="movie_id", values="rating").fillna(0)

    return ratings_matrix

# Function to get the normalized data
def get_normalized_data():
    ratings_matrix = pivot_data()

    # Normalize the ratings
    normalized_ratings = normalize_data(ratings_matrix)

    return normalized_ratings

# Function to get the model's weights
def weights():
    # Read weights and convert back to Tensor
    weight_settings = pd.read_csv("rbm_weights.csv")
    weights_tensor = tf.constant(weight_settings.values, tf.float32)
    return weights_tensor

# Function to get the model's hidden layer biases
def hidden_bias():
    # Read hidden layer biases and convert back to Tensor
    hidden_bias_settings = pd.read_csv("hidden_layer_bias.csv")
    hidden_tensor = tf.constant(hidden_bias_settings.values, tf.float32)
    return hidden_tensor

# Function to get the model's visible layer biases
def visible_bias():
    # Read visible layer biases and convert back to Tensor
    visible_bias_settings = pd.read_csv("visible_layer_bias.csv")
    visible_tensor = tf.constant(visible_bias_settings.values, tf.float32)
    return visible_tensor

# Function to convert the user ratings to a Tensor
def user_tensor(user_ratings):
    user = tf.convert_to_tensor(user_ratings.values,"float32")

    return user

# Define a function to return only the generated hidden states
def hidden_layer(v0, W, hb):
    # probabilities of the hidden units
    h0 = tf.nn.sigmoid(tf.matmul([v0], W) + hb)
    return h0

# Define a function to return the reconstructed output
def reconstructed_output(h0, W, vb):
    v1 = tf.nn.sigmoid(tf.matmul(h0, tf.transpose(W)) + tf.transpose(vb))
    return v1

# Function to generate recommendation for a user
def generate_recommendation(user_ratings, W, vb, hb):
    v0 = user_tensor(user_ratings)

    hh0 = hidden_layer(v0, W, hb)

    vv1 = reconstructed_output(hh0, W, vb)

    rec = vv1
    return rec
