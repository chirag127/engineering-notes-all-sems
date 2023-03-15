 Here is the content in markdown format for the topic ### logistic regression for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning:

### Logistic Regression
- Logistic regression is a supervised learning classification algorithm.
- It is used to predict a binary outcome (1 / 0, yes / no, true / false) given a set of independent variables.
- It uses a logistic/sigmoid function to convert the input variables' values to a probability value which ranges between 0 and 1.
- Threshold value of 0.5 is used to classify the output as 0 or 1.
- Output probability > 0.5 = 1 (classified as the positive class)
- Output probability <= 0.5 = 0 (classified as the negative class)
- Advantages:
-- Simple and easy to implement.
-- No complex interactions between features required for the model.
-- Only linear boundaries between classes (straight-line separation between classes).
-- Gives probabilistic outputs (can give confidence scores).
- Disadvantages:
-- Assumes linear relationship and independent variables.
-- Does not directly provide probability estimates. Requires conversion using sigmoid function.
-- Can overfit easily due to simplicity.

Mnemonics:
- The probability that an event will occur is never < 0 or > 1. (use of sigmoid/logistic function)
- Think of a straight line dividing the 2 classes. (linear decision boundary)
- Higher the probability, higher the confidence of being in the positive class. (threshold at 0.5)

Examples:
- Predicting if an email is spam or not spam.
- Predicting if a tumor is malignant or benign.
- Predicting if a customer will churn or not.

Applications:
- Classification problems with binary outcomes.
- Initial baseline model due to simplicity before trying complex models.
- Output probability scores can be used to rank and select top candidates.

Diagrams and codes can be added if required to understand the concepts better.