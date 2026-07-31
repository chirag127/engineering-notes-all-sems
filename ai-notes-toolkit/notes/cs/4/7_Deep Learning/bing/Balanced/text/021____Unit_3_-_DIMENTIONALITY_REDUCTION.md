## Unit 3 - Dimensionality Reduction

- Dimensionality reduction is the process of transforming data from a high-dimensional space into a low-dimensional space so that the low-dimensional representation retains some meaningful properties of the original data, ideally close to its intrinsic dimension.
- Dimensionality reduction can be done for a variety of reasons, such as to reduce the complexity of a model, to improve the performance of a learning algorithm, or to make it easier to visualize the data.
- Dimensionality reduction techniques can be divided into two categories: feature selection and feature extraction.
  - Feature selection methods select a subset of the original features that are most relevant or informative for the task at hand, such as backward feature elimination or forward feature selection .
  - Feature extraction methods create new features from the original features that capture the most variance or information in the data, such as principal component analysis (PCA) or singular value decomposition (SVD) .
- Dimensionality reduction techniques have advantages and disadvantages, depending on the data and the task. Some of the advantages are :
  - Reducing the noise and redundancy in the data, which can improve the accuracy and generalization of the model.
  - Reducing the computational cost and memory requirement of the model, which can speed up the training and inference process.
  - Reducing the curse of dimensionality, which is the phenomenon that high-dimensional data becomes sparse and difficult to analyze.
  - Facilitating the interpretation and visualization of the data, which can help to discover patterns and insights.
- Some of the disadvantages are :
  - Losing some information or variability in the data, which can affect the performance or quality of the model.
  - Introducing bias or distortion in the data, which can lead to misleading or inaccurate results.
  - Depending on the technique, dimensionality reduction can be computationally expensive or complex to implement.
  - Depending on the technique, dimensionality reduction can be sensitive to the parameters or assumptions of the method.