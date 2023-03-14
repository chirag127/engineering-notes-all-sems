 Here is the content in markdown format for the topic ### loss functions for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning:

### Loss functions

Loss functions are used to measure how bad our model's predictions are. We try to minimize the loss function during training to make our model's predictions better.

Some common loss functions used in Deep Learning are:

- Mean Squared Error (MSE): It is the average of the squared differences between the predicted and actual values. MSE punishes large errors more than small errors.
- MSE = 1/n * sum(actual - predicted)^2
- Mnemonic: Meaning - Measure of wrongness, Squares the error, Errors averaged

- Mean Absolute Error (MAE): It is the average of the absolute differences between the predicted and actual values. MAE does not square the differences, so it punishes all errors equally.
- MAE = 1/n * sum(abs(actual - predicted))
- Mnemonic: Meaning - Measure of wrongness, Absolute value of error, Errors averaged

- Binary Cross Entropy (BCE): It is used for binary classification problems. It measures the "distance" between the model's predictions and the actual values.
- BCE = -1/n * sum(actual * log(predicted) + (1 - actual) * log(1 - predicted))
- Mnemonic: Actual vs Predicted, Cross product, Entropy (measure of randomness/impurity)

- Categorical Cross Entropy (CCE): It is used for multi-class classification problems. It is a generalization of BCE for more than 2 classes.
- CCE = -1/n * sum(actual * log(predicted))
- Mnemonic: Actual vs Predicted, Cross product, Entropy (measure of randomness/impurity)

Advantages and disadvantages of each loss function, examples, applications, etc. can be included if required. Detailed diagrams and codes can also be added if helpful for learning.