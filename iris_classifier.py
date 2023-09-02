import pickle  # Import the pickle module

# Load the trained model using pickle
with open("trained_model.pkl", "rb") as model_file:
    classifier = pickle.load(model_file)

def predict_species(sepal_length, sepal_width, petal_length, petal_width):
    # Make a prediction based on user input
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = classifier.predict(input_data)
    return prediction[0]
