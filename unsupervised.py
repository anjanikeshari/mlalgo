import numpy as np
import math
from scipy.spatial.distance import cdist

Class Centroid:
    def k_means(X, K):
    #Keep track of history
        centroids_history = []
        labels_history = []
        rand_index = np.random.choice(X.shape[0], K)  
        centroids = X[rand_index]
        centroids_history.append(centroids)
        while True:
    # Euclidean distances are calculated for each point relative to centroids, 
    # #and then np.argmin returns the index location of the minimal distance - 
    # which cluster a point    is #assigned to
            labels = np.argmin(cdist(X, centroids), axis=1)
            labels_history.append(labels)
    #Take mean of points within clusters to find new centroids:
            new_centroids = np.array([X[labels == i].mean(axis=0)
                                    for i in range(K)])
            centroids_history.append(new_centroids)
            
            # If old centroids and new centroids no longer change, K-means is complete and end. Otherwise continue
            if np.all(centroids == new_centroids):
                break
            centroids = new_centroids
        
        return centroids, labels, centroids_history, labels_history

    centers, labels, centers_hist, labels_hist = k_means(X, 3)
