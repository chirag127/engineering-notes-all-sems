### k-Nearest Neighbour Learning

- k-Nearest Neighbour (k-NN) is a **supervised learning** technique and algorithm that can be used for both **regression** and **classification** tasks .
- k-NN is a **non-parametric** method, which means it does not make any assumptions about the underlying distribution of the data .
- k-NN is based on the idea of **proximity** or **similarity**, which means that similar data points are likely to have similar labels or outputs .
- k-NN works by finding the **k** closest or most similar data points (called **neighbours**) to a given **query** or **test** point, and then using their labels or outputs to make a prediction for the query point  .
- The number of neighbours **k** is a **hyperparameter** that can be chosen by the user or tuned using cross-validation .
- The **distance** or **similarity** measure between data points can also be chosen by the user or learned from the data. Some common distance measures are **Euclidean distance**, **Manhattan distance**, **Minkowski distance**, **Hamming distance**, and **cosine similarity** .
- For **classification** tasks, k-NN predicts the class of the query point by taking a **majority vote** of the classes of the k neighbours, or by weighting the votes by the inverse of the distances  .
- For **regression** tasks, k-NN predicts the output of the query point by taking the **average** or **weighted average** of the outputs of the k neighbours  .
- k-NN is a **lazy learning** method, which means it does not learn a model from the training data, but rather stores the entire training data and performs the prediction at the query time  .
- k-NN has some advantages and disadvantages as a machine learning technique. Some of the advantages are:
  - It is **simple** and **intuitive** to understand and implement  .
  - It can handle **multiclass** and **non-linear** problems  .
  - It can adapt to **local** patterns and **complex** boundaries  .
- Some of the disadvantages are:
  - It is **computationally expensive** and **slow** to make predictions, especially for large and high-dimensional data sets   .
  - It is **sensitive** to the choice of **k**, the distance measure, and the presence of **noise** and **outliers** in the data   .
  - It does not provide any **explanation** or **confidence** for the predictions  .