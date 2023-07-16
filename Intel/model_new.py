import pandas as pd
import matplotlib.pyplot as plt
from sklearnex import patch_sklearn
patch_sklearn()
from sklearn.cluster import KMeans
import pickle

#download dataset https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data
students= pd.read_csv("studentdata_new.csv")

# Fit KMeans model with optimal number of clusters
model = KMeans(n_clusters=5)  # Assuming 5 as the optimal number of clusters
model.fit(students[['raisedhands', 'VisITedResources', 'AnnouncementsView', 'Discussion', 'StudentAbsenceDays']])
students['class'] = model.labels_

# Calculate mean and find the potential dropout class
mi = 100000000
potential_dropout_class = 'x'
for i in range(model.n_clusters):
    df1 = students[students['class'] == i]
    temp = df1.mean().sum()
    print(temp, len(df1))
    if mi > temp:
        mi = temp
        potential_dropout_class = df1

dropout_class = potential_dropout_class['class'].mean()
print("Potential Dropout Class:", int(dropout_class))
print(potential_dropout_class)

# Save the model as a pickle file
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
