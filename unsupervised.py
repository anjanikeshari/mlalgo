import numpy as np
import math
from scipy.spatial.distance import cdist


class Kmeans:

	def predict(self, K, data):
	
		# Randonly choose initial centroids
		# We will implement different strategies to choose initial centroids later	
		rand_ind = np.random.choice(data.shape[0], K)  
		centroids = data[rand_ind]
		
		while True:
	# Euclidean distances are calculated for each point wrt centroids, 
	# then we get centroid index with minimum dist to centroid, we assign
	# that centroid as label
			labels = np.argmin(cdist(data, centroids), axis=1)
	#Take mean of points within clusters to find new centroids:
			new_centroids = np.array([data[labels == i].mean(axis=0)
									for i in range(K)])
			
			# If old centroids and new centroids no longer change, K-means is complete and end. Otherwise continue
			if np.all(centroids == new_centroids):
				break
			centroids = new_centroids
		
		return centroids, labels

