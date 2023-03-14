## Unit 3 - Dimensionality Reduction

Dimensionality reduction is the process of transforming data from a high-dimensional space into a low-dimensional space so that the low-dimensional representation retains some meaningful properties of the original data, ideally close to its intrinsic dimension. 

Some reasons for performing dimensionality reduction are:

- To avoid the curse of dimensionality, which refers to the problems that arise when working with data in higher dimensions, such as sparsity, overfitting, and computational complexity.  
- To reduce the noise and redundancy in the data, which can improve the accuracy and performance of the learning algorithms. 
- To facilitate data visualization, which can help to understand the patterns and relationships in the data. 
- To enable the use of algorithms that are not suitable for high-dimensional data, such as distance-based methods. 

There are two main approaches to dimensionality reduction: feature selection and feature extraction. 

- Feature selection is the process of identifying and selecting a subset of the original features that are relevant and informative for the task. Feature selection methods can be divided into three categories: filter, wrapper, and embedded methods. Filter methods use some criteria to rank the features and select the best ones. Wrapper methods use a learning algorithm to evaluate the features and select the optimal subset. Embedded methods incorporate feature selection into the learning process and select the features that are most useful for the model. 
- Feature extraction is the process of creating new features from the original features by applying some transformation or operation on them. Feature extraction methods can be divided into linear and nonlinear methods. Linear methods project the data onto a lower-dimensional subspace that maximizes some criterion, such as variance or mutual information. Nonlinear methods use more complex functions to map the data to a lower-dimensional space that preserves some structure or property of the data, such as manifold or topology.  

Some examples of dimensionality reduction methods are:

- Principal component analysis (PCA): A linear feature extraction method that finds the orthogonal directions of maximum variance in the data and projects the data onto them. PCA can be used for noise reduction, data compression, and data visualization. 
- Linear discriminant analysis (LDA): A linear feature extraction method that finds the directions that maximize the separation between different classes in the data and projects the data onto them. LDA can be used for classification and data visualization. 
- t-distributed stochastic neighbor embedding (t-SNE): A nonlinear feature extraction method that maps the data to a lower-dimensional space that preserves the local similarities between the data points. t-SNE can be used for data visualization and cluster analysis. 
- Autoencoder: A nonlinear feature extraction method that uses a neural network to learn a compressed representation of the data that can be reconstructed with minimal error. Autoencoder can be used for data compression, noise reduction, and anomaly detection.