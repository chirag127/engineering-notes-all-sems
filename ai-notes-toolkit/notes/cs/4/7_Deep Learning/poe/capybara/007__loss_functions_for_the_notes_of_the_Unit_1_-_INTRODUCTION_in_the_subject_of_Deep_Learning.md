### Loss Functions for the Notes of Unit 1 - Introduction in the Subject of Deep Learning

Loss functions play a crucial role in deep learning models. They measure the difference between the predicted output and the actual output. Choosing the right loss function is important as it directly impacts the accuracy of the model. Here are some common loss functions used in deep learning:

1. Mean Squared Error (MSE)
- Measures the average squared difference between predicted and actual values
- Used for regression problems where the output is a continuous value
- Formula: MSE = (1/n) * Σ(y_pred - y_actual)^2

2. Binary Cross-Entropy Loss
- Measures the difference between predicted and actual values for binary classification problems
- Formula: BCE = - (y_actual * log(y_pred) + (1 - y_actual) * log(1 - y_pred))

3. Categorical Cross-Entropy Loss
- Measures the difference between predicted and actual values for multi-class classification problems
- Formula: CCE = - Σ(y_actual * log(y_pred))

4. Hinge Loss
- Used for classification problems where the output is a binary label
- Penalizes incorrect predictions more than correct ones
- Formula: Hinge Loss = max(0, 1 - y_actual * y_pred)

5. Kullback-Leibler (KL) Divergence Loss
- Measures the difference between two probability distributions
- Used for tasks such as image segmentation and language modeling
- Formula: KL = Σ(y_actual * log(y_actual / y_pred))

It is important to choose the right loss function based on the type of problem and the data being used. Experimentation with different loss functions can also lead to better model performance.