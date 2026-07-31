### Learning and Generalisation

- Learning is the process of finding patterns or relationships in data that can be used to make predictions or decisions.
- Generalisation is the ability of a learned model to perform well on new or unseen data that was not used for training.
- Learning and generalisation are related but not the same. A model that learns well on the training data may not generalise well on the test data, and vice versa.
- The goal of learning is to find a model that balances the trade-off between fitting the training data and generalising to the test data. This is also known as the bias-variance trade-off.
- Bias is the error due to the model's assumptions or simplifications that do not match the true underlying data distribution. A high-bias model is underfitting, meaning it cannot capture the complexity or variability of the data.
- Variance is the error due to the model's sensitivity or instability to small changes in the data. A high-variance model is overfitting, meaning it memorises the noise or outliers in the data.
- A good model should have low bias and low variance, meaning it can fit the training data well and generalise to the test data well.
- There are several techniques to improve the learning and generalisation performance of a model, such as:
  - Cross-validation: splitting the data into multiple subsets and using some of them for training and some of them for testing, and averaging the results.
  - Regularisation: adding a penalty term to the model's objective function that reduces its complexity or flexibility, such as L1 or L2 regularisation.
  - Feature selection: choosing a subset of relevant or informative features that contribute to the model's prediction, and discarding the redundant or noisy features.
  - Feature engineering: transforming or creating new features that capture the underlying structure or relationships in the data, such as polynomial or interaction features.
  - Ensemble methods: combining multiple models or learners that have different strengths and weaknesses, and aggregating their predictions, such as bagging, boosting, or stacking.