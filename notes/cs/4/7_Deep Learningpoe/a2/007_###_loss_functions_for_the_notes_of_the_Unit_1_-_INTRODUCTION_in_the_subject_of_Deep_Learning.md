 Here is the content in markdown format for the topic ### loss functions for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning:

### Loss Functions

 Loss functions are a way to quantify how bad our model's predictions are. We want to minimize the loss function to improve our model's predictions.

- **Mean Squared Error (MSE)** - Average squared difference between predictions and actual values. Tries to minimize large errors.  
MSE(y,y') = ∑(y-y')2/n
- **Mean Absolute Error (MAE)** - Average absolute difference between predictions and actual values. Less sensitive to outliers than MSE.  
MAE(y,y') = ∑|y-y'|/n
- **Cross Entropy** - Measures the difference between two probability distributions (actual vs predicted). Often used for classification.  
CE(y,y') = -∑ylog(y')

Some things to keep in mind when choosing a loss function:

- What problem are you solving (regression vs classification)?
- Sensitivity to outliers
- Scale of target values
- Ease of optimization

There are no strict rules on which loss function is best, it really depends on your problem and goals. It's often a good idea to experiment with a few different loss functions and see which gives the best results!

Mnemonics and Learning Tricks:
- MSE: Squares amplify errors, good for regression
- MAE: Absolute values discard sign, less sensitive to outliers
- Cross Entropy: Measures diff between distributions, good for classification

Advantages:
- MSE: Differentiates well, intuitive to optimize
- MAE: Less sensitive to outliers
- Cross Entropy: Proper scoring rule for probabilities

Disadvantages:
- MSE: Sensitive to outliers
- MAE: Less differentiable, can cause optimization difficulties
- Cross Entropy: Can be hard to optimize, requires log

Examples:
- Regression: MSE, MAE
- Classification: Cross Entropy

Applications:
- MSE: Linear/logistic regression
- MAE: Robust regression
- Cross Entropy: Neural networks