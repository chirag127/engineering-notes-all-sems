# k-Nearest Neighbour Learning

- k-Nearest Neighbour (k-NN) is a **supervised learning** technique and algorithm that can be used for both **regression** and **classification** tasks .
- k-NN is a **non-parametric** method, which means it does not make any assumptions about the underlying distribution of the data .
- k-NN is based on the idea of **proximity** or **similarity**, which means that similar data points are likely to have similar labels or outputs .
- k-NN works by finding the **k** closest or most similar data points (called **neighbours**) to a given **query** or **test** point, and then using their labels or outputs to make a prediction for the query point  .
- k-NN can be applied to different types of data, such as **numerical**, **categorical**, or **textual** data, as long as a suitable **distance** or **similarity** measure is defined for the data  .
- k-NN is a **lazy** learning method, which means it does not learn a model or a function from the training data, but rather stores the training data and performs the computation at the time of prediction  .
- k-NN is a **simple** and **intuitive** algorithm, but it also has some **limitations** and **challenges**, such as:
  - Choosing the optimal value of **k**, which can affect the accuracy and complexity of the algorithm  .
  - Dealing with **high-dimensional** data, which can cause the distance or similarity measure to become less meaningful and increase the computational cost  .
  - Handling **imbalanced** data, which can cause the majority class to dominate the prediction and reduce the performance for the minority class .
  - Addressing **noise** and **outliers** in the data, which can affect the prediction and the quality of the neighbours .
  - Selecting the appropriate **distance** or **similarity** measure for the data, which can influence the results and the interpretation of the algorithm  .
  - Implementing an efficient **data structure** and **search algorithm** for finding the nearest neighbours, which can improve the speed and scalability of the algorithm  .