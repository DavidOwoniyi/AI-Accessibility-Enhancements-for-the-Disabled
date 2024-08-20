# Import necessary dependencies
import pickle  # For loading and saving serialized objects
import numpy as np  # For numerical operations and array handling
from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets
from sklearn.ensemble import RandomForestClassifier  # For building the classification model
from sklearn.metrics import accuracy_score  # For evaluating the model's accuracy

# Load the data from a pickle file
data_dict = pickle.load(open('./data.pickle', 'rb'))

# Determine the maximum sequence length in the data
max_len = max(len(x) for x in data_dict['data'])
print(f"Maximum sequence length: {max_len}")

# Pad the sequences in the data to ensure they all have the same length
padded_data = np.array([np.pad(x, (0, max_len - len(x)), 'constant') for x in data_dict['data']])

# Convert labels to a NumPy array for consistency
labels = np.asarray(data_dict['labels'])

# Split the data into training and testing sets (80% training, 20% testing)
x_train, x_test, y_train, y_test = train_test_split(padded_data, labels, test_size=0.2, shuffle=True, stratify=labels)

# Initialize a Random Forest Classifier model
model = RandomForestClassifier()

# Train the model on the training data
model.fit(x_train, y_train)

# Predict the labels for the test data
y_predict = model.predict(x_test)

# Calculate the accuracy of the model's predictions
score = accuracy_score(y_predict, y_test)

# Print the accuracy of the model
print('{}% of samples were classified correctly!'.format(score * 100))

# Save the trained model to a pickle file
f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
