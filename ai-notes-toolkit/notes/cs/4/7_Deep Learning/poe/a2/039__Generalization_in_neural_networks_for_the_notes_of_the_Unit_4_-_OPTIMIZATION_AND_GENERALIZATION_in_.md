 Here are the points on Generalization in neural networks for the notes of the Unit 4 - OPTIMIZATION AND GENERALIZATION in the subject of Deep Learning:

### Generalization in neural networks

1. Overfitting - When a model performs very well on the training data but does not generalize well to new data, it is said to be overfitting the training data. This happens when the model is too complex relative to the amount of data available.
2. Underfitting - When a model is not complex enough and does not capture the underlying patterns in the data, it is said to be underfitting the data. Such a model will not learn the training data well nor will it generalize to new data.
3. Model complexity - The complexity of a model is related to the number of parameters it has. More parameters allow the model to capture more complex relationships but also increase the chance of overfitting. The optimal model complexity needs to be balanced out using data and regularization.
4. Regularization - Regularization is a technique used to control model complexity and avoid overfitting. Some common regularization techniques are:
- L1 and L2 regularization: Adding a penalty term to the loss function that shrinks the weights towards zero.
- Data augmentation: Generating additional training data by transforming the existing training samples.
- Early stopping: Stopping training once the validation loss starts increasing.
5. Cross-validation - Cross-validation is a technique to estimate the skill of a machine learning model on unseen data. The training data is split into k folds, the model is trained and tested k times with different folds acting as test sets, and the k results are averaged to get the cross-validation estimate.