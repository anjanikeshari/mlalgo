# mlalgo
 Implementing ML package


 ## Documentation

### Simple and Easy Package

**--This is package for enabling basic ML algos--**

Unsupervised 
    - Kmeans
    - Kmedoids
    - Clustering Performance (Silhouette Score)
    - Hierarchical Clustering
        - Agglomerative
        - Divisive
    - DBSCAN
    - PCA
    - Auto Encoders
    - t-Distributed Stochastic Neighbor Embedding (t-SNE)
    - Topic Modeling
    - Latent Dirichlet Allocation
    - Market Basket Analysis (MBA)
        - Apriori
        - FP Tree
    - Hotspot Analysis
    - Kernel Density Estimation (KDE)


Supervised
    - Linear Regression
    - Polynomial Regression
    - Mutivariate Regression
    - Logistic Regression
    - SVD
    - Decision Tree
    - Random Forest
    - Bayesian 




<br><br>

</div>


This package aims to provide a simple and easy way to use the ML algos
<br>


## Installation
To install via `pip` use:
`pip install mlalgo`

## Basic Usage
The usage of the wrapper is very easy. Just import, initialize object and start coding:
```python
import mlalgo

kmeans_model = mlalgo.unsupervised.Kmeans(k=3,data=X)


