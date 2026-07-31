### Logistic Regression

Logistic Regression is a statistical method for analyzing a dataset in which there are one or more independent variables that determine an outcome. The outcome is measured with a dichotomous variable (in which there are only two possible outcomes).

It is used to model the probability of a certain class or event existing such as pass/fail, win/lose, alive/dead or healthy/sick. This can be extended to model several classes of events such as determining whether an image contains a cat, dog, lion, etc.

Logistic Regression is named after the function used at the core of the method, the logistic function. The logistic function, also called the sigmoid function, was developed by statisticians to describe properties of population growth in ecology, rising quickly and maxing out at the carrying capacity of the environment. It’s an S-shaped curve that can take any real-valued number and map it into a value between 0 and 1, but never exactly at those limits.

1. Logistic Regression is used when the dependent variable(target) is categorical.
2. For example,
    * To predict whether an email is spam (1) or (0)
    * Whether the tumor is malignant (1) or not (0)
3. There are two types of logistic regression:
    * Binary Logistic Regression: The target variable has only two possible outcomes such as Spam or Not Spam, Cancer or No Cancer.
    * Multinomial Logistic Regression: The target variable has three or more nominal categories such as predicting the type of Wine.
    * Ordinal Logistic Regression: the target variable has three or more ordinal categories such as restaurant or product rating from 1 to 5.
4. Logistic Regression measures the relationship between the categorical dependent variable and one or more independent variables by estimating probabilities using a logistic function, which is the cumulative distribution function of logistic distribution.
5. The coefficients of the logistic regression algorithm must be estimated from the training data. This is done using maximum-likelihood estimation.
6. Maximum-likelihood estimation is a common learning algorithm used by a variety of machine learning algorithms, although it does make assumptions about the distribution of your data.
7. The best coefficients would result in a model that would predict a high probability for the default class for negative examples and a low probability for positive examples.
8. The probabilities are then transformed into class predictions.
9. The logistic function has an S-shape and can take any real-valued number and map it into a value between 0 and 1, but never exactly at those limits.
10. Logistic regression is a linear method, but the predictions are transformed using the logistic function.
11. The impact of this is that we can no longer understand the predictions as a linear combination of the inputs as we can with linear regression, for example, continuing on from above, the model can be stated as:
    * odds = e^(b0 + b1*X1)
    * p(X) = e^(b0 + b1*X1) / (1 + e^(b0 + b1*X1))
12. Where p(X) is the probability of the positive class given the input values of X.