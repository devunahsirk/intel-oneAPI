#ALREADY PREPARED
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearnex import patch_sklearn
patch_sklearn()
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
import pickle

# Reading the data
students = pd.read_csv('studentdata.csv')
students = students.drop(['gender', 'NationalITy', 'PlaceofBirth', 'StageID', 'SectionID', 'Topic', 'Relation', 'Relation', 'Relation', 'ParentAnsweringSurvey', 'ParentschoolSatisfaction', 'ParentschoolSatisfaction', 'GradeID', 'Semester', 'Class'], axis=1)

# Data preprocessing
def absent(e):
    if e == 'Under-4':
        return np.random.randint(0, 4)
    else:
        return np.random.randint(4, 8)

students.StudentAbsenceDays = students.StudentAbsenceDays.apply(absent)

def hands(e):
    if e['StudentAbsenceDays'] == 7:
        return 0
    else:
        return e['raisedhands']

students.raisedhands = students.apply(hands, axis=1)

def discussion(e):
    if e['StudentAbsenceDays'] == 7:
        return 0
    else:
        return e['Discussion']

students.Discussion = students.apply(discussion, axis=1)

students.to_csv("students_final.csv", index=False)

# Finding optimal number of clusters using the Elbow Method
x = []
for k in range(1, 50):
    km = KMeans(n_clusters=k)
    km.fit_predict(students[['raisedhands', 'VisITedResources', 'AnnouncementsView', 'Discussion', 'StudentAbsenceDays']])
    x.append(km.inertia_)
    print(km.inertia_)

plt.plot(range(1, 50), x)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.savefig("./elbow_k")
