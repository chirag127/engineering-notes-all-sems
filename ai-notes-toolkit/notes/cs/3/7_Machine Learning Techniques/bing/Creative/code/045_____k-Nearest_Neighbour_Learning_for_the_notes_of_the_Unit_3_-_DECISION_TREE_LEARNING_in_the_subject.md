### k-Nearest Neighbour Learning

- k-Nearest Neighbour (k-NN) is a **supervised learning** technique and algorithm that can be used for both **regression** and **classification** tasks .
- k-NN is a **non-parametric** method, which means it does not make any assumptions about the underlying distribution of the data .
- k-NN is based on the idea of **proximity** or **similarity**, which means that similar data points are likely to have similar labels or outputs .
- k-NN works by finding the **k** closest or most similar data points (called **neighbours**) to a given **query** or **test** data point, and then using their labels or outputs to make a prediction for the query data point  .
- The number of neighbours **k** is a **hyperparameter** that can be chosen by the user or tuned using cross-validation .
- The **distance** or **similarity** measure between data points can also be chosen by the user or learned from the data. Some common distance measures are **Euclidean distance**, **Manhattan distance**, **Minkowski distance**, **Hamming distance**, and **cosine similarity**  .
- For **classification** tasks, k-NN predicts the class of the query data point by taking a **majority vote** of the classes of its k neighbours. For example, if k=3 and the query data point has 2 neighbours of class A and 1 neighbour of class B, then k-NN will predict class A for the query data point  .
- For **regression** tasks, k-NN predicts the output of the query data point by taking the **average** or **weighted average** of the outputs of its k neighbours. For example, if k=3 and the query data point has neighbours with outputs 10, 12, and 14, then k-NN will predict 12 as the output for the query data point  .
- k-NN is a **lazy learning** method, which means it does not learn any model or function from the training data, but rather stores the entire training data and performs the prediction at the query time  .
- k-NN has some advantages and disadvantages as a machine learning technique. Some of the advantages are:
  - It is simple and easy to implement and understand .
  - It can handle multi-class problems and non-linear data .
  - It is robust to noisy data and outliers, especially when using a large k .
- Some of the disadvantages are:
  - It is computationally expensive and slow, especially when the training data is large and high-dimensional  .
  - It is sensitive to the choice of k, distance measure, and scaling of the features  .
  - It does not provide any explanation or confidence for its predictions .