## Unit 4 - OPTIMIZATION AND GENERALIZATION

1. **Optimization** refers to the process of finding the best solution or decision for a given problem. In the context of machine learning, optimization is the process of adjusting the model's parameters to minimize the loss function.

2. **Generalization** refers to the ability of a machine learning model to perform well on unseen data. A model that generalizes well is able to make accurate predictions on new data that it has not seen during training.

3. The goal of optimization in machine learning is to find the best set of parameters for the model that allows it to generalize well to new data.

4. There are several optimization algorithms that can be used to adjust the model's parameters, including gradient descent, stochastic gradient descent, and batch gradient descent.

5. Overfitting is a common problem in machine learning, where the model fits the training data too well and is not able to generalize well to new data. Regularization techniques, such as L1 and L2 regularization, can be used to prevent overfitting.

6. Cross-validation is a technique used to assess the generalization ability of a machine learning model. It involves splitting the data into several subsets and training the model on some of the subsets while evaluating its performance on the remaining subsets.

7. The bias-variance tradeoff is an important concept in machine learning. A model with high bias makes strong assumptions about the data and may not fit the training data well, while a model with high variance is sensitive to the training data and may not generalize well to new data. The goal is to find a balance between bias and variance to achieve good generalization performance.

8. Hyperparameter tuning is the process of selecting the best set of hyperparameters for a machine learning model. Hyperparameters are parameters that are not learned from the data, but are set by the user before training the model. Grid search and random search are common methods for hyperparameter tuning.

9. Early stopping is a technique used to prevent overfitting in neural networks. It involves monitoring the validation loss during training and stopping the training process when the validation loss stops decreasing.

10. Transfer learning is a technique used to improve the generalization performance of a machine learning model by leveraging knowledge learned from a related task. It involves using a pre-trained model as a starting point and fine-tuning it on the new task. This can save time and computational resources compared to training a model from scratch.