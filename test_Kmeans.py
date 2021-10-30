import unsupervised
from sklearn.metrics import confusion_matrix

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
import math

# Generate data to form original clusters
X, y = make_blobs(n_samples=1000, centers=2,
n_features=2, random_state=800)

plt.scatter(X[:, 0], X[:, 1], s=50, cmap='tab20b')
plt.show()

kmeans_model = unsupervised.Kmeans()
centroids, labels = kmeans_model.predict(K=2, data=X)

# Get Confusion Matrix metrics
# True Negative, False Pos, False neg, True pos
tn, fp, fn, tp = confusion_matrix(y, labels).ravel()

print("Accuracy: ", (tp+tn)/(tp+tn+fp+fn)*100)

