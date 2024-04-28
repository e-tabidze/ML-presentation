import pandas as pd
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load the dataset
data = pd.read_csv('network_traffic_data.csv')

# Encoding categorical variables
label_encoder = LabelEncoder()
data['protocol'] = label_encoder.fit_transform(data['protocol'])
data['source_ip'] = label_encoder.fit_transform(data['source_ip'])
data['destination_ip'] = label_encoder.fit_transform(data['destination_ip'])
data['label'] = label_encoder.fit_transform(data['label'])

# Splitting features and labels
X = data.drop(columns=['timestamp', 'label'])  # dropping timestamp and label columns
y = data['label']

# Splitting the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the One-Class SVM model
model = OneClassSVM(kernel='rbf', gamma='auto').fit(X_train[y_train == 0])  # fitting only on benign samples

# Predicting anomalies
y_pred = model.predict(X_test)

# Converting predictions to labels (1: normal, -1: anomaly)
y_pred[y_pred == 1] = 0  # normal
y_pred[y_pred == -1] = 1  # anomaly

# Evaluating the model
print(classification_report(y_test, y_pred, target_names=['Benign', 'Malicious']))

