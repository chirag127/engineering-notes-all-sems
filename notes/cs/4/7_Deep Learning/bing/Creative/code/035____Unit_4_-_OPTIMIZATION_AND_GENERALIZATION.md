## Unit 4 - OPTIMIZATION AND GENERALIZATION

- Optimization and generalization are two key concepts in machine learning that are closely related.
- Optimization refers to the process of finding the best parameters for a machine learning model that minimize the loss function on the training data  .
- Generalization refers to the ability of a machine learning model to perform well on new and unseen data, not just on the training data  .
- Optimization and generalization are often in conflict, as optimizing the model too much on the training data can lead to overfitting, which means the model fails to generalize well on the test data  .
- To achieve a good balance between optimization and generalization, machine learning practitioners use various techniques, such as:
  - Regularization: adding a penalty term to the loss function that reduces the complexity of the model and prevents overfitting  .
  - Dropout: randomly dropping out some units or connections in a neural network during training to reduce co-adaptation and improve generalization.
  - Early stopping: stopping the training process before the model reaches the minimum of the loss function on the training data, to avoid overfitting .
  - Data augmentation: applying transformations to the original data to create more and diverse examples for training the model.
  - Adding noise: adding some noise to the input or the output of the model to make it more robust and less sensitive to small variations.