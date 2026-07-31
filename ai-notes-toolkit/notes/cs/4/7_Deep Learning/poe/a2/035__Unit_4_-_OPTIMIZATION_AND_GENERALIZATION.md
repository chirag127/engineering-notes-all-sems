 Here is the formal content written in Markdown format without any emojis or external links under the header ## Unit 4 - OPTIMIZATION AND GENERALIZATION:

## Unit 4 - OPTIMIZATION AND GENERALIZATION

1. Overfitting - When a machine learning model performs very well on the training data but does not generalize well to new data, it is said to be overfitting. This happens when the model captures the noise in the training data along with the signal. Some ways to reduce overfitting are:
- Getting more training data
- Reducing the number of features
- Regularization
- Early stopping

2. Underfitting - When a model is not complex enough and cannot capture the patterns in the data, it leads to underfitting. The model performs poorly on both training and test data in this case. Some ways to address underfitting are:
- Increasing the model complexity by adding more layers or nodes
- Trying a more powerful model
- Collecting more data

3. Model selection - The process of selecting a final model out of multiple trained models is called model selection. Some common model selection techniques are:
- Cross-validation - The data is split into training and validation sets multiple times and the model with the best average performance is selected.
- Grid search - Models are trained for a grid of hyperparameters and the best one is picked.
- Random search - Hyperparameters are sampled randomly and the best model is selected. This avoids exhaustive search and can be more efficient.

4. Hyperparameter tuning - The hyperparameters of a model control its complexity and performance. Tuning the hyperparameters refers to systematically varying them and selecting the combination that yields the best performance. Some ways to do hyperparameter tuning are:
- Manual search
- Grid search
- Random search
- Bayesian optimization