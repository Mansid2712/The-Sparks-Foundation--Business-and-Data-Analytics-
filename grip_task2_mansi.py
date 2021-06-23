# -*- coding: utf-8 -*-
"""GRIP_TASK2_MANSI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JNuieZ35dwx03MehlyyVJo9CbZtr7Xtn

## Task Two for GRIP - The Sparks Foundation
### Presented By
>Mansi Dinakar

### This project is the unsupervised classification of data from the iris dataset.

#### Dataset link
>https://bit.ly/3kXTdox
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist

get_ipython().run_line_magic('matplotlib','inline')

# Loading the iris dataset
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
iris_df.head(8)

##iris_df = pd.read_csv('Iris_data_sample.csv', header = None)

"""## To determine the optimal number of clusters for K-means, we will use 

---

the elbow method
"""

distortions = []
inertias = []
mapping1 = {} #to store values of distortion
mapping2 = {} #to store values of inertia
K = range(1, 10)
 
for k in K:
    # Building and fitting the model
    kmeanModel = KMeans(n_clusters=k).fit(iris_df)
    kmeanModel.fit(iris_df)
 
    distortions.append(sum(np.min(cdist(iris_df, kmeanModel.cluster_centers_,'euclidean'), axis=1)) / iris_df.shape[0])
    inertias.append(kmeanModel.inertia_)
 
    mapping1[k] = sum(np.min(cdist(iris_df, kmeanModel.cluster_centers_,'euclidean'), axis=1)) / iris_df.shape[0]
    mapping2[k] = kmeanModel.inertia_

"""## For various values of distortion obtained from the data

##### Data Distortion is the intentional or unintentional misrepresentation of a dataset
"""

for key, val in mapping1.items():
    print(f'{key} : {val}')

plt.plot(K, distortions, 'bx-', color = "cyan")
plt.xlabel('Values of K')
plt.ylabel('Distortion')
plt.title('The Elbow Method using Distortion', weight = "bold")
plt.show()

"""## For various values of inertia obtained from the data

#####  Inertia tells how far away the points within a cluster are. Therefore, a small of inertia is aimed for.
"""

for key, val in mapping2.items():
    print(f'{key} : {val}')

plt.plot(K, inertias, 'bx-', color = "red")
plt.xlabel('Values of K')
plt.ylabel('Inertia')
plt.title('The Elbow Method using Inertia', weight = "bold")
plt.show()

"""### From both cases of the elbow method, we come to conclusion that 3 is the optimal number of clusters for this dataset."""

model = KMeans(n_clusters=3)
model = model.fit_predict(iris_df)

"""## Visualization of Kmeans for 3 clusters on Iris dataset"""

x = iris_df.iloc[:, [0,1,2,3]].values
plt.scatter(x[ : , 0], x[ : , 1], c = model, cmap = 'rainbow', marker = '*')

