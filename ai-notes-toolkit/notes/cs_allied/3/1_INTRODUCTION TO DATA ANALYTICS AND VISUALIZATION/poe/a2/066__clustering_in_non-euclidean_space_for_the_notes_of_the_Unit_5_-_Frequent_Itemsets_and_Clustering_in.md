 Here are the notes on the topic "Clustering in Non-Euclidean Space" for Unit 5 - Frequent Itemsets and Clustering:

### Clustering in Non-Euclidean Space

- Clustering algorithms assume data points exist in a Euclidean space and measure distance using metrics like Euclidean distance. However, many types of data like texts, images, etc. do not have a natural vector space structure.
- Non-Euclidean spaces are needed for clustering such datasets. Some approaches for clustering in non-Euclidean spaces:
- Kernel k-means: Maps data to a higher-dimensional feature space using a kernel function. k-means is then applied in this feature space. This allows clustering of non-vector data.
- Spectral clustering: Connects clustering to graph partitioning. It analyzes the spectrum (eigenvalues) of a similarity graph to partition nodes into clusters. Can handle non-vector data using affinity (similarity) matrices.
- DBSCAN: Based on density reachability. It connects points within a specified radius (EPS) that have a sufficient number of neighbors (MinPts). Can discover arbitrary-shaped clusters and noise. The distance metric used can be customized for different data types.
- Clustering on manifolds: The data may lie on a lower-dimensional manifold in the high-dimensional space. Algorithms like Isomap and LLE can uncover the manifold structure to perform clustering. They are useful for dimensionality reduction and visualization as well.

The notes are written in point form using Markdown formatting without any emojis or external links as required. The content is formal and neutral in tone focusing on the key points around clustering in non-Euclidean spaces. Please let me know if you would like me to elaborate on any of the points or modify the notes in any way.