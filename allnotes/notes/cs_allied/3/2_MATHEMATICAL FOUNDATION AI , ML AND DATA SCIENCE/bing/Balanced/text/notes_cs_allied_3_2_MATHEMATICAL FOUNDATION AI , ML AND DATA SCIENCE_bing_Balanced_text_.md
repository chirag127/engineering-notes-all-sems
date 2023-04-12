

# Mathematical Foundation of AI, ML and Data Science

- AI, ML and Data Science are interdisciplinary fields that use computational methods to analyze data and make predictions, decisions or actions.
- Mathematics is an essential foundation of any contemporary discipline of science. Therefore, almost all data science techniques and concepts, such as Artificial Intelligence (AI) and Machine Learning (ML), have deep-rooted mathematical underpinnings.
- Some of the main mathematical topics that are relevant for AI, ML and Data Science are:

  - Linear Algebra: The study of vector spaces, matrices, tensors, linear transformations, eigenvalues, eigenvectors, singular value decomposition, etc. Linear algebra is used to manipulate and transform data, perform dimensionality reduction, solve systems of linear equations, and implement neural networks.
  - Calculus: The study of functions, limits, derivatives, integrals, optimization, etc. Calculus is used to understand the behavior of functions, find the optimal values of parameters, compute gradients, and perform backpropagation.
  - Probability and Statistics: The study of random variables, distributions, sampling, inference, hypothesis testing, confidence intervals, etc. Probability and statistics are used to model uncertainty, quantify variability, estimate parameters, and test hypotheses.
  - Discrete Mathematics: The study of finite and discrete structures, such as sets, logic, graphs, algorithms, complexity, etc. Discrete mathematics is used to represent and manipulate discrete data, perform logical reasoning, design and analyze algorithms, and measure computational efficiency.
  - Optimization: The study of finding the best solution to a problem, subject to some constraints, such as minimizing a cost function or maximizing a utility function. Optimization is used to solve various problems in AI, ML and Data Science, such as linear programming, convex optimization, gradient descent, etc.

- These are some of the core mathematical topics that are needed for AI, ML and Data Science, but there are also other topics that are useful, such as numerical analysis, differential equations, graph theory, game theory, etc.
- Learning these mathematical topics can help you master the fundamental mathematics toolkit of machine learning and data science, and enable you to write programs and algorithms for AI and ML applications .



## Unit 1 - Descriptive Statistics

- Descriptive statistics are methods of summarizing and displaying data in a concise and informative way.
- Descriptive statistics can be divided into two categories: measures of central tendency and measures of variability.
- Measures of central tendency describe the typical or average value of a data set, such as the mean, median, and mode.
- Measures of variability describe the spread or dispersion of a data set, such as the range, interquartile range, standard deviation, and variance.
- Descriptive statistics can also include graphical representations of data, such as histograms, box plots, scatter plots, and pie charts.
- Descriptive statistics are useful for exploring and understanding data, but they do not allow for making inferences or generalizations about a larger population. For that, inferential statistics are needed.



### Diagrammatic representation of data

- Diagrammatic representation of data is the use of diagrams to display and summarize numerical data in a clear and effective way .
- Diagrams can be geometrical figures, such as lines, bars, and circles, or graphical elements, such as charts, graphs, and maps .
- Diagrams can help to simplify complex data, highlight important trends and patterns, compare different categories or groups, and communicate the main findings to the audience .
- Some of the common types of diagrams used in data representation are:

  - Line diagram: A diagram that shows the change in a variable over time or space using a line or curve.
  - Bar diagram: A diagram that shows the frequency or magnitude of different categories or groups using rectangular bars of equal width and varying height or length.
  - Pie chart: A diagram that shows the proportion of different categories or groups using a circle divided into sectors whose angles are proportional to the relative frequencies or percentages.
  - Histogram: A diagram that shows the distribution of a continuous variable using adjacent rectangular bars whose heights are proportional to the frequencies and whose widths are equal to the class intervals.
  - Frequency polygon: A diagram that shows the distribution of a continuous variable using a line or curve that connects the midpoints of the tops of the bars in a histogram.
  - Ogive: A diagram that shows the cumulative frequency or percentage distribution of a continuous variable using a line or curve that connects the points obtained by plotting the upper limits of the class intervals against the corresponding cumulative frequencies or percentages.
  - Scatter plot: A diagram that shows the relationship between two variables using dots or points that represent the pairs of values for the variables.
  - Box plot: A diagram that shows the summary statistics of a variable using a box that contains the median, the lower and upper quartiles, and the minimum and maximum values, and optionally the outliers.
  - Stem-and-leaf plot: A diagram that shows the distribution of a variable using the digits of the values, where the leftmost digit(s) form the stem and the rightmost digit(s) form the leaf.



### Measures of Central Tendency

- Measures of central tendency are summary measures that attempt to describe a whole set of data with a single value that represents the middle or centre of its distribution.
- Colloquially, measures of central tendency are often called averages.
- The most common measures of central tendency are the arithmetic mean, the median, and the mode   .
- The mean is the sum of all values divided by the total number of values . It is also called the arithmetic average.
- The median is the middle number in an ordered dataset . It is also called the 50th percentile.
- The mode is the most frequent value in a dataset . It is also called the peak of the distribution.
- Different measures of central tendency may give different values for the same dataset, depending on how the data are distributed.
- The mean is sensitive to outliers, which are extreme values that deviate from the rest of the data. The median and the mode are more robust to outliers.
- The mean is the most commonly used measure of central tendency for symmetric distributions, such as the normal distribution. The median is the most commonly used measure of central tendency for skewed distributions, such as the exponential distribution. The mode is the most commonly used measure of central tendency for categorical or discrete data, such as the number of heads in a coin toss.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content on the topic of measures of dispersion for the notes of the Unit 1 - Descriptive Statistics in the subject of Mathematical Foundation AI, ML and Data Science. Here is the content I have written in markdown format:

### Measures of Dispersion

- Measures of dispersion are numerical values that indicate the variability or spread of a data set.
- They complement the measures of central tendency, such as mean, median and mode, which describe the average or typical value of a data set.
- Measures of dispersion help to understand how much the data values deviate from the center, how consistent or inconsistent the data values are, and how the data values are distributed.
- Some common measures of dispersion are:

  - **Range**: The difference between the maximum and minimum values of a data set. It is the simplest measure of dispersion, but it is sensitive to outliers and does not consider the distribution of the data values.

  - **Interquartile Range (IQR)**: The difference between the third quartile (Q3) and the first quartile (Q1) of a data set. It is the range of the middle 50% of the data values. It is more robust than the range, as it is not affected by outliers and extreme values.

  - **Variance**: The average of the squared deviations of the data values from the mean. It measures how far the data values are spread around the mean. It is a widely used measure of dispersion, but it is difficult to interpret as it is not in the same unit as the data values.

  - **Standard Deviation**: The square root of the variance. It measures how far the data values are spread around the mean. It is in the same unit as the data values, and it is easier to interpret than the variance.

  - **Coefficient of Variation (CV)**: The ratio of the standard deviation to the mean, expressed as a percentage. It measures the relative variability of the data values. It is useful for comparing the dispersion of data sets with different units or scales.

- Measures of dispersion are important for data analysis, as they provide information about the reliability, accuracy and precision of the data values. They also help to identify outliers, anomalies and patterns in the data.



### Measures of Skewness and Kurtosis

- Skewness and kurtosis are two measures of shape that describe the distribution of data values.
- Skewness measures the degree of symmetry or asymmetry of a distribution. A symmetric distribution has zero skewness, while an asymmetric distribution has either positive or negative skewness.
- Positive skewness means that the distribution has a longer right tail, and the mean is greater than the median. Negative skewness means that the distribution has a longer left tail, and the mean is less than the median.
- One formula to measure skewness is Pearson's median skewness, which is defined as:

$$
\text{Pearson's median skewness} = \frac{3(\text{mean} - \text{median})}{\text{standard deviation}}
$$

- Kurtosis measures the degree of peakedness or flatness of a distribution. A normal distribution has a kurtosis of 3, while a distribution that is more peaked or more flat than normal has a kurtosis greater or less than 3, respectively.
- A distribution with a high kurtosis is called leptokurtic, and it has heavy tails and a narrow peak. A distribution with a low kurtosis is called platykurtic, and it has light tails and a wide peak. A distribution with a normal kurtosis is called mesokurtic, and it has a similar shape to the normal curve.
- One formula to measure kurtosis is the excess kurtosis, which is defined as:

$$
\text{Excess kurtosis} = \frac{\text{fourth moment}}{(\text{standard deviation})^4} - 3
$$

- The fourth moment is the expected value of the fourth power of the deviation from the mean, and it measures the spread of the distribution.

- Skewness and kurtosis are useful for describing the shape of data and comparing different distributions. They can also indicate the presence of outliers, extreme values, or non-normality in the data.



### Correlation

- Correlation is a statistical measure that expresses the extent to which two variables are linearly related, meaning they change together at a constant rate.
- Correlation can be used to describe the strength and direction of the relationship between two variables, without implying causation .
- Correlation can be measured by different methods, such as Pearson's correlation coefficient, Spearman's rank correlation coefficient, and Kendall's rank correlation coefficient .
- Correlation coefficients range from -1 to 1, where -1 indicates a perfect negative linear relationship, 0 indicates no linear relationship, and 1 indicates a perfect positive linear relationship .
- Correlation can be used for various purposes, such as exploring data, testing hypotheses, and diversifying portfolios  .



### Inference procedure for correlation coefficient

- A correlation coefficient is a numerical measure of the strength and direction of a linear relationship between two variables.
- The most common correlation coefficient is the Pearson correlation coefficient (r), which ranges from -1 to 1, where -1 indicates a perfect negative linear relationship, 0 indicates no linear relationship, and 1 indicates a perfect positive linear relationship.
- To test the significance of the Pearson correlation coefficient, we can use the following steps:

  1. State the null hypothesis (H0) and the alternative hypothesis (Ha). The null hypothesis is usually that there is no linear relationship between the variables (r = 0), and the alternative hypothesis is that there is a linear relationship (r ≠ 0).
  2. Calculate the t value using this formula: t = r * sqrt((n - 2) / (1 - r^2)), where r is the sample correlation coefficient and n is the sample size.
  3. Find the critical value of t from a t table, using the significance level (α) and the degrees of freedom (df = n - 2).
  4. Compare the t value to the critical value. If the absolute value of t is greater than the critical value, reject the null hypothesis. If the absolute value of t is less than or equal to the critical value, fail to reject the null hypothesis.
  5. Interpret the results in the context of the problem.

- To construct a confidence interval for the Pearson correlation coefficient, we can use the following steps:

  1. Transform the sample correlation coefficient (r) to a Fisher z score using this formula: z = 0.5 * ln((1 + r) / (1 - r)), where ln is the natural logarithm function.
  2. Find the standard error of the Fisher z score using this formula: SE = 1 / sqrt(n - 3), where n is the sample size.
  3. Find the margin of error using this formula: ME = z* * SE, where z* is the critical value from a standard normal distribution corresponding to the confidence level.
  4. Find the lower and upper bounds of the confidence interval for the Fisher z score using this formula: LB = z - ME, UB = z + ME.
  5. Back-transform the lower and upper bounds of the confidence interval for the Fisher z score to the confidence interval for the correlation coefficient using this formula: r = (e^(2z) - 1) / (e^(2z) + 1), where e is the base of the natural logarithm function.
  6. Interpret the confidence interval in the context of the problem.



### Bivariate Correlation

- Bivariate correlation is a statistical technique that measures the strength and direction of the relationship between two variables.
- Bivariate correlation can be positive, negative, or zero, depending on how the variables change together.
- Bivariate correlation can be calculated using different methods, such as Pearson's correlation coefficient, Spearman's rank correlation coefficient, or Kendall's tau coefficient.
- Pearson's correlation coefficient is the most common method of bivariate correlation. It measures the linear correlation between two continuous variables that have a normal distribution.
- Pearson's correlation coefficient ranges from -1 to 1, where -1 indicates a perfect negative linear relationship, 0 indicates no linear relationship, and 1 indicates a perfect positive linear relationship.
- Spearman's rank correlation coefficient is a nonparametric method of bivariate correlation. It measures the monotonic correlation between two ordinal or continuous variables that do not have a normal distribution.
- Spearman's rank correlation coefficient ranges from -1 to 1, where -1 indicates a perfect negative monotonic relationship, 0 indicates no monotonic relationship, and 1 indicates a perfect positive monotonic relationship.
- Kendall's tau coefficient is another nonparametric method of bivariate correlation. It measures the concordance or discordance between two ordinal or continuous variables that do not have a normal distribution.
- Kendall's tau coefficient ranges from -1 to 1, where -1 indicates a perfect negative concordance, 0 indicates no concordance, and 1 indicates a perfect positive concordance.
- Bivariate correlation can be used to explore the associations between variables, test hypotheses, and identify potential confounding factors in research.
- Bivariate correlation does not imply causation, meaning that a high or low correlation does not mean that one variable causes the other. To establish causation, other methods such as experiments or regression analysis are needed.



### Multiple Correlation

- Multiple correlation is a measure of the relationship between a dependent variable and a set of independent variables considered together.
- The multiple correlation coefficient, denoted by R, is the correlation between the dependent variable's values and the best predictions that can be computed linearly from the independent variables.
- The formula for the multiple correlation coefficient is:

R = sqrt(R^2)

where R^2 is the coefficient of determination, which is the proportion of variance in the dependent variable that can be explained by the independent variables.

- The value of R ranges from 0 to 1, where 0 indicates no linear relationship and 1 indicates a perfect linear relationship.
- The multiple correlation coefficient can be computed using the following steps:

  - Perform a multiple linear regression analysis on the data, where the dependent variable is regressed on the independent variables.
  - Obtain the value of R^2 from the regression output, which is usually reported as the "adjusted R-squared" or the "coefficient of multiple determination".
  - Take the square root of R^2 to get the value of R.

- The multiple correlation coefficient can be interpreted as the strength of the linear association between the dependent variable and the set of independent variables. A higher value of R indicates a stronger relationship, while a lower value indicates a weaker relationship.
- The multiple correlation coefficient can also be used to assess the goodness of fit of the multiple linear regression model, by comparing it with the simple correlation coefficient between the dependent variable and each independent variable. A higher value of R indicates that the multiple regression model fits the data better than the simple regression models.



### Linear Regression and Its Inference Procedure

- Linear regression is a statistical method that models the relationship between a dependent variable (y) and one or more independent variables (x) by fitting a linear equation to the observed data.
- The linear equation can be written as: y = β0 + β1x1 + β2x2 + ... + βkxk + ε, where β0 is the intercept, β1, β2, ..., βk are the slopes, and ε is the error term.
- The goal of linear regression is to estimate the unknown parameters β0, β1, ..., βk that best fit the data, and to assess the quality and significance of the fitted model.
- Inference in linear regression is the process of testing hypotheses and constructing confidence intervals about the parameters and the model using the data.
- Some common inference procedures in linear regression are:

  - Testing the significance of the overall model using the F-test. The F-test compares the variability explained by the model (sum of squares regression) to the variability not explained by the model (sum of squares error). The null hypothesis is that all the slopes are zero, meaning that the model has no explanatory power. The alternative hypothesis is that at least one slope is not zero, meaning that the model is useful. The F-test statistic is calculated as: F = (SSR/k) / (SSE/(n-k-1)), where SSR is the sum of squares regression, SSE is the sum of squares error, k is the number of independent variables, and n is the sample size. The F-test statistic follows an F-distribution with k and n-k-1 degrees of freedom. The p-value is the probability of obtaining an F-test statistic as extreme or more extreme than the observed one under the null hypothesis. A small p-value indicates strong evidence against the null hypothesis, and a large p-value indicates weak evidence against the null hypothesis.
  - Testing the significance of individual slopes using the t-test. The t-test compares the estimated slope (b) to the null value (usually zero) and assesses how likely it is to obtain such a slope by chance. The null hypothesis is that the slope is equal to the null value, meaning that the corresponding independent variable has no effect on the dependent variable. The alternative hypothesis is that the slope is not equal to the null value, meaning that the corresponding independent variable has an effect on the dependent variable. The t-test statistic is calculated as: t = (b - null value) / SE(b), where b is the estimated slope, SE(b) is the standard error of the slope, and null value is the hypothesized value of the slope. The t-test statistic follows a t-distribution with n-k-1 degrees of freedom. The p-value is the probability of obtaining a t-test statistic as extreme or more extreme than the observed one under the null hypothesis. A small p-value indicates strong evidence against the null hypothesis, and a large p-value indicates weak evidence against the null hypothesis.
  - Constructing confidence intervals for the parameters and the predictions. A confidence interval is a range of values that is likely to contain the true value of a parameter or a prediction with a certain level of confidence. For example, a 95% confidence interval for the slope β1 means that we are 95% confident that the true value of β1 lies within the interval. A confidence interval for the slope β1 can be calculated as: b ± t* SE(b), where b is the estimated slope, SE(b) is the standard error of the slope, and t* is the critical value from the t-distribution with n-k-1 degrees of freedom and the desired level of confidence. A confidence interval for the prediction of y for a given value of x can be calculated as: y ± t* SE(y), where y is the estimated value of y, SE(y) is the standard error of the prediction, and t* is the same as above. The standard error of the prediction depends on the variability of the residuals, the distance of x from the mean of x, and the number of independent variables in the model. A narrower confidence interval indicates more precision, and a wider confidence interval indicates more uncertainty.



### Multiple Regression

- Multiple regression is a statistical technique that allows us to estimate the relationship between a dependent variable and two or more independent variables.
- The dependent variable is the outcome or response that we want to predict or explain, such as sales, test scores, or weight.
- The independent variables are the factors or predictors that influence the dependent variable, such as advertising, education, or diet.
- Multiple regression can be used for various purposes, such as:
  - Testing hypotheses about the effects of the independent variables on the dependent variable.
  - Estimating the value of the dependent variable for a given set of values of the independent variables.
  - Identifying the most important or significant independent variables that affect the dependent variable.
  - Assessing the fit or accuracy of the regression model.
- Multiple regression can be expressed as a mathematical equation, such as:

  - y = b0 + b1x1 + b2x2 + ... + bnxn + e
  - where y is the dependent variable, x1, x2, ..., xn are the independent variables, b0 is the intercept, b1, b2, ..., bn are the regression coefficients, and e is the error term.
- The regression coefficients represent the slope or change in the dependent variable for a one-unit change in the corresponding independent variable, holding all other independent variables constant.
- The intercept represents the value of the dependent variable when all the independent variables are zero.
- The error term represents the random variation or noise that is not explained by the regression model.
- Multiple regression can be performed using various methods, such as:
  - Ordinary least squares (OLS), which minimizes the sum of squared errors between the observed and predicted values of the dependent variable.
  - Maximum likelihood estimation (MLE), which maximizes the probability of observing the data given the regression model.
  - Generalized linear models (GLM), which allow for different types of distributions and link functions for the dependent variable, such as logistic, Poisson, or gamma.
  - Regularization methods, such as ridge, lasso, or elastic net, which add a penalty term to the regression model to reduce overfitting and multicollinearity.



### Probability

- Probability is a measure of how likely an event is to occur in a random experiment.
- An event is a subset of the sample space, which is the set of all possible outcomes of the experiment.
- The probability of an event A is denoted by P(A) and satisfies the following properties:
  - 0 ≤ P(A) ≤ 1 for any event A
  - P(S) = 1, where S is the sample space
  - P(∅) = 0, where ∅ is the empty set
  - If A and B are mutually exclusive events, then P(A ∪ B) = P(A) + P(B)
  - P(Aᶜ) = 1 - P(A), where Aᶜ is the complement of A
- The probability of an event can be calculated using different approaches, such as:
  - Classical approach: P(A) = n(A) / n(S), where n(A) is the number of favorable outcomes for A and n(S) is the number of possible outcomes in the sample space. This approach assumes that all outcomes are equally likely.
  - Relative frequency approach: P(A) = f(A) / N, where f(A) is the frequency of occurrence of A and N is the number of trials in the experiment. This approach is based on empirical data and the law of large numbers.
  - Subjective approach: P(A) is a degree of belief or confidence in the occurrence of A, based on personal judgment or prior information. This approach is useful when there is no data or when the outcomes are not equally likely.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of measures of probability for the unit 1 - descriptive statistics in the subject of mathematical foundation AI, ML and data science.

### Measures of probability

- Probability is a numerical measure of the likelihood of an event occurring.
- Probability can range from 0 to 1, where 0 means the event is impossible and 1 means the event is certain.
- There are different ways to assign probabilities to events, depending on the available information and assumptions.
- Some common methods are:

  - **Empirical probability**: based on the relative frequency of the event in a large number of trials or observations.
  - **Classical probability**: based on the assumption that all possible outcomes are equally likely.
  - **Subjective probability**: based on the personal judgment or belief of the person assigning the probability.

- Some basic rules of probability are:

  - **Complement rule**: the probability of an event not occurring is equal to 1 minus the probability of the event occurring. P(not A) = 1 - P(A)
  - **Addition rule**: the probability of the union of two events is equal to the sum of their individual probabilities minus the probability of their intersection. P(A or B) = P(A) + P(B) - P(A and B)
  - **Multiplication rule**: the probability of the intersection of two events is equal to the product of their individual probabilities if they are independent, or the product of one probability and the conditional probability of the other given the first if they are dependent. P(A and B) = P(A) * P(B) if A and B are independent, or P(A and B) = P(A) * P(B|A) if A and B are dependent.
  - **Conditional probability**: the probability of an event given that another event has occurred. P(A|B) = P(A and B) / P(B)
  - **Bayes' theorem**: a formula that allows us to update the probability of an event based on new information. P(A|B) = P(B|A) * P(A) / P(B)



### Conditional Probability

- Conditional probability is the probability of one event occurring with some relationship to one or more other events.
- Conditional probability is denoted by P(A|B), which means the probability of event A given that event B has occurred .
- The formula for conditional probability is P(A|B) = P(A and B) / P(B), where P(A and B) is the joint probability of both events happening and P(B) is the marginal probability of event B happening .
- Conditional probability can be used to model situations where the outcome of one event affects the outcome of another event, such as weather, sports, games, genetics, etc .
- Conditional probability can also be used to update the prior probability of an event based on new information, such as Bayes' theorem.
- Conditional probability can be visualized using Venn diagrams, tree diagrams, or tables .

#### Examples of Conditional Probability

- Example 1: A coin is tossed twice. What is the probability of getting two heads given that the first toss is a head?
  - Solution: Let A be the event of getting two heads and B be the event of getting a head on the first toss. Then P(A|B) = P(A and B) / P(B). Since the coin is fair, P(A and B) = 1/4 and P(B) = 1/2. Therefore, P(A|B) = (1/4) / (1/2) = 1/2.
- Example 2: A card is drawn from a standard deck of 52 cards. What is the probability of getting a king given that the card is a face card?
  - Solution: Let A be the event of getting a king and B be the event of getting a face card. Then P(A|B) = P(A and B) / P(B). There are 4 kings and 12 face cards in the deck, so P(A and B) = 4/52 and P(B) = 12/52. Therefore, P(A|B) = (4/52) / (12/52) = 1/3.



### Independent event

- An independent event is an event that is not affected by the occurrence of another event.
- Two events A and B are independent if and only if P(A and B) = P(A) * P(B), where P(A and B) is the probability of both events happening, and P(A) and P(B) are the probabilities of each event happening.
- For example, if you toss a coin and roll a die, the outcome of the coin toss is independent of the outcome of the die roll, because the coin and the die are not related in any way. The probability of getting heads and a 6 is equal to the probability of getting heads times the probability of getting a 6, or 0.5 * 1/6 = 1/12.
- Independent events can be represented by a Venn diagram, where the two circles do not overlap, indicating that there is no common outcome between the two events.



### Bayes' Theorem

- Bayes' theorem is a mathematical formula for determining conditional probability, which is the likelihood of an event occurring, based on a previous outcome having occurred in similar circumstances.
- Bayes' theorem is named after Thomas Bayes, an 18th-century British mathematician, statistician and philosopher, who used conditional probability to provide an algorithm for calculating limits on an unknown parameter.
- Bayes' theorem can be used to update or revise predictions or beliefs in light of new or relevant evidence, also known as posterior probability or inverse probability .
- Bayes' theorem can be generalized to include improper prior distributions, such as the uniform distribution on the real line, and can be applied to various fields, such as science, engineering, medicine, economics, etc.
- Bayes' theorem can be expressed in various forms, but the most common one is:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

where:

- $P(A|B)$ is the conditional probability of event A given that event B has occurred, also known as the posterior probability.
- $P(B|A)$ is the conditional probability of event B given that event A has occurred, also known as the likelihood.
- $P(A)$ is the prior probability of event A, which is the probability of event A before observing event B.
- $P(B)$ is the marginal probability of event B, which is the probability of event B regardless of event A.

- Bayes' theorem can be derived from the definition of conditional probability and the law of total probability, as follows:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

$$P(B|A) = \frac{P(A \cap B)}{P(A)}$$

$$P(A \cap B) = P(B|A)P(A) = P(A|B)P(B)$$

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

- Bayes' theorem can be extended to more than two events, such as:

$$P(A|B,C) = \frac{P(B,C|A)P(A)}{P(B,C)}$$

- Bayes' theorem can also be applied to continuous random variables, such as:

$$f(x|y) = \frac{f(y|x)f(x)}{f(y)}$$

where:

- $f(x|y)$ is the conditional probability density function of random variable X given that random variable Y has a value of y, also known as the posterior density.
- $f(y|x)$ is the conditional probability density function of random variable Y given that random variable X has a value of x, also known as the likelihood function.
- $f(x)$ is the prior probability density function of random variable X, which is the probability density of X before observing Y.
- $f(y)$ is the marginal probability density function of random variable Y, which is the probability density of Y regardless of X.

- Bayes' theorem can be illustrated by various examples, such as:

  - Example 1: Suppose there is a test for a disease that has a 99% accuracy rate, meaning that 99% of the time it gives a correct result (positive or negative) for a person who has or does not have the disease. Suppose also that 1% of the population has the disease. What is the probability that a person who tests positive actually has the disease?

    - Solution: Let A be the event that a person has the disease, and B be the event that a person tests positive. We want to find $P(A|B)$, the probability that a person has the disease given that they test positive. Using Bayes' theorem, we have:

    $$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

    - We know that $P(B|A) = 0.99$, the accuracy rate of the test for a person who has the disease. We also know that $P(A) = 0.01$, the prevalence rate of the disease in the population. To find $P(B)$, the probability that a person tests positive, we can use the law of total probability, which states that:

    $$P(B) = P(B|A)P(A) + P(B|\neg A)P(\neg A)$$



### Random Variable

- A random variable is a variable that is used to denote the numerical outcome of a random experiment.
- A random experiment is an event or process that has a random outcome, such as rolling a die, choosing a card, or playing a slot machine .
- There are two types of random variables: discrete and continuous .
- A discrete random variable can take only a countable number of distinct values, such as 0, 1, 2, 3, etc. Examples are the number of heads in a coin toss, the number of red cards in a deck, or the number of customers in a queue  .
- A continuous random variable can take any value within a range of values, such as 0.03, 1.2374553, etc. Examples are the height of a person, the weight of a fruit, or the time of arrival of a bus  .
- A probability distribution is a function that assigns probabilities to the possible values of a random variable  .
- A probability distribution can be represented by a table, a graph, or a formula  .
- The mean (or expected value) of a random variable is the average of the possible values, weighted by their probabilities  .
- The mean of a random variable can be calculated by multiplying each possible value by its probability and adding them up  .
- The mean of a random variable gives a measure of the center of the probability distribution  .



### Discrete and Continuous Probability Distributions

- A probability distribution is a function that describes all possible values of a random variable as well as the associated probabilities.
- A random variable is a variable whose value is determined by the outcome of a random experiment.
- A probability distribution may be either discrete or continuous.
- A discrete probability distribution counts occurrences that have countable or finite outcomes.
- A continuous probability distribution is the probability distribution of a continuous variable, which can have any value between its lowest and highest values.
- For a discrete distribution, probabilities can be assigned to the values in the distribution, such as P(X = x).
- For a continuous distribution, probabilities can be assigned to the ranges of values, such as P(a < X < b), where the probability is equal to the area under the curve of its probability density function (PDF).
- Common examples of discrete distribution include the binomial, Poisson, and Bernoulli distributions.
- Common examples of continuous distribution include the normal, uniform, exponential, and beta distributions.



### Expectation and Variance

- The **expectation** of a random variable is the weighted average of its possible values, where the weights are the probabilities of each value. It is also called the **mean** or the **expected value** of the random variable. It is denoted by E(X) or µX.
- The **variance** of a random variable is the measure of how much the values of the random variable deviate from the mean. It is also called the **mean squared deviation** or the **second central moment** of the random variable. It is denoted by Var(X) or σX^2.
- The **standard deviation** of a random variable is the positive square root of the variance. It is also a measure of dispersion or spread of the random variable. It is denoted by SD(X) or σX.

- The formulas for expectation and variance depend on whether the random variable is discrete or continuous. For a discrete random variable X with probability mass function p(x), the formulas are:

  - E(X) = ∑xp(x) for all possible values of x
  - Var(X) = E(X^2) - E(X)^2 = ∑x^2p(x) - E(X)^2 for all possible values of x
  - SD(X) = √Var(X)

- For a continuous random variable X with probability density function f(x), the formulas are:

  - E(X) = ∫xf(x)dx over the domain of x
  - Var(X) = E(X^2) - E(X)^2 = ∫x^2f(x)dx - E(X)^2 over the domain of x
  - SD(X) = √Var(X)

- Some properties of expectation and variance are:

  - E(aX + b) = aE(X) + b for any constants a and b
  - Var(aX + b) = a^2Var(X) for any constants a and b
  - SD(aX + b) = |a|SD(X) for any constant a
  - Cov(X, Y) = E(XY) - E(X)E(Y) is the **covariance** of two random variables X and Y, which measures the linear relationship between them
  - Corr(X, Y) = Cov(X, Y) / (SD(X)SD(Y)) is the **correlation** of two random variables X and Y, which measures the strength and direction of the linear relationship between them
  - Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y) for any two random variables X and Y
  - Var(X - Y) = Var(X) + Var(Y) - 2Cov(X, Y) for any two random variables X and Y
  - If X and Y are **independent**, then Cov(X, Y) = 0 and Corr(X, Y) = 0
  - If X and Y are independent, then E(XY) = E(X)E(Y) and Var(X + Y) = Var(X) + Var(Y) and Var(X - Y) = Var(X) + Var(Y)



### Markov Inequality

- Markov inequality is a mathematical result that gives an upper bound on the probability that a non-negative random variable exceeds a certain value.
- Markov inequality can be stated as follows: Let X be a non-negative random variable and a be a positive constant. Then, P(X >= a) <= E(X) / a, where E(X) is the expected value of X.
- Markov inequality can be used to derive other inequalities, such as Chebyshev's inequality and Chernoff's bound, by applying suitable transformations to the random variable X.
- Markov inequality can be proved by using the definition of expected value and the indicator function. The proof is as follows:

  - Let I be the indicator function of the event {X >= a}, i.e., I = 1 if X >= a and I = 0 otherwise. Then, E(I) = P(X >= a).
  - Since X is non-negative, we have X >= XI for all values of X. Taking the expected value of both sides, we get E(X) >= E(XI).
  - By the linearity of expectation, we have E(XI) = E(X)E(I) = E(X)P(X >= a).
  - Dividing both sides by E(X), we get P(X >= a) <= E(X) / a, which is the Markov inequality.



### Chebyshev’s Inequality

- Chebyshev’s inequality is a theorem in probability theory that guarantees that, for any probability distribution, no more than a certain fraction of values can be more than a certain distance from the mean .
- The fraction is given by 1/k^2, where k is the number of standard deviations from the mean. The distance is given by k times the standard deviation of the distribution .
- Chebyshev’s inequality can be written as:

P(|X - μ| ≥ kσ) ≤ 1/k^2

where X is a random variable, μ is the mean, σ is the standard deviation, and k is any positive number .

- Chebyshev’s inequality is useful because it applies to any probability distribution, regardless of its shape or parameters . It provides a lower bound for the probability that a value will be within a certain number of standard deviations from the mean .
- For example, Chebyshev’s inequality states that at most 25% of the values will be more than two standard deviations from the mean (k = 2), and at most 11.11% of the values will be more than three standard deviations from the mean (k = 3)  . These bounds are valid for any distribution, but they may not be tight for some distributions, such as the normal distribution, which has smaller probabilities of extreme values .
- Chebyshev’s inequality can be used to analyze the variability of data, to estimate confidence intervals, and to test hypotheses . It can also be generalized to higher moments, such as the variance and the skewness, and to multivariate distributions .



### Central Limit Theorem

- The central limit theorem (CLT) is one of the most fundamental and important theorems in probability and statistics.
- The CLT states that, under certain conditions, the distribution of the sample means of a random variable approaches a normal distribution as the sample size increases, regardless of the shape of the population distribution.
- The CLT has many applications and implications in statistics, such as:
  - It allows us to use the normal distribution to approximate the sampling distribution of many statistics, such as the sample mean, the sample proportion, and the difference between two sample means or proportions.
  - It enables us to perform hypothesis testing and construct confidence intervals for population parameters using the standard normal distribution (z-distribution) or the Student's t-distribution.
  - It provides a theoretical justification for the use of parametric tests, such as t-tests, ANOVAs, and linear regression, which assume that the errors or residuals are normally distributed.
- The CLT also has some important properties and assumptions, such as:
  - The mean of the sampling distribution of the sample mean is equal to the mean of the population distribution, i.e., x̄ = μ.
  - The standard deviation of the sampling distribution of the sample mean is equal to the standard deviation of the population distribution divided by the square root of the sample size, i.e., σx̄ = σ/√n.
  - The shape of the sampling distribution of the sample mean depends on the sample size and the population distribution. If the population distribution is normal, then the sampling distribution of the sample mean is also normal for any sample size. If the population distribution is not normal, then the sampling distribution of the sample mean becomes more normal as the sample size increases, and it is approximately normal when the sample size is 30 or more.
  - The samples must be independent and identically distributed (i.i.d.), which means that each sample is drawn randomly and with replacement from the same population, and that the samples do not influence each other.



## Unit 2 - Inferential Statistics

- Inferential statistics are methods of drawing conclusions about a population based on a sample of data from that population.
- Inferential statistics are useful when it is impractical or impossible to measure every individual in a population of interest.
- Inferential statistics rely on the assumption that the sample is representative of the population, meaning that it reflects the characteristics and variability of the population.
- Inferential statistics can be divided into two main types: hypothesis testing and estimation.
- Hypothesis testing is a process of evaluating a claim or a statement about a population parameter (such as the mean, the proportion, the standard deviation, etc.) based on a sample statistic.
- Hypothesis testing involves setting up a null hypothesis (H0) and an alternative hypothesis (Ha), which are mutually exclusive and exhaustive statements about the population parameter.
- Hypothesis testing also involves choosing a significance level (alpha), which is the probability of rejecting the null hypothesis when it is true (a type I error).
- Hypothesis testing then involves calculating a test statistic, which is a function of the sample data and the null hypothesis, and comparing it to a critical value or a p-value, which are measures of the strength of the evidence against the null hypothesis.
- Hypothesis testing results in either rejecting the null hypothesis in favor of the alternative hypothesis, or failing to reject the null hypothesis, based on the chosen significance level and the test statistic.
- Estimation is a process of using a sample statistic to estimate a population parameter with a certain degree of confidence or precision.
- Estimation can be done using point estimates or interval estimates.
- A point estimate is a single value that is the best guess of the population parameter based on the sample data.
- An interval estimate is a range of values that is likely to contain the population parameter with a certain level of confidence.
- An interval estimate consists of a point estimate plus or minus a margin of error, which is a measure of the uncertainty or variability of the estimate.
- An interval estimate can be constructed using different methods, such as the z-interval, the t-interval, the bootstrap interval, etc., depending on the type of population parameter, the sample size, and the distribution of the sample data.
- An interval estimate can be interpreted as saying that if the sampling process is repeated many times, a certain percentage of the intervals will contain the true population parameter. This percentage is called the confidence level of the interval.



### Sampling & Confidence Interval

- Sampling is the process of selecting a subset of individuals or units from a population of interest for the purpose of collecting data or making inferences about the population.
- Sampling can be done using different methods, such as random sampling, stratified sampling, cluster sampling, systematic sampling, convenience sampling, etc.
- Sampling can help reduce the cost and time of data collection, increase the accuracy and precision of estimates, and allow for generalization to a larger population.
- Confidence interval is an estimate of an interval in statistics that may contain a population parameter, such as the mean, proportion, variance, etc.
- Confidence interval is calculated from a sample statistic and a measure of sampling variability, such as the standard error or the margin of error.
- Confidence interval has a specified level of confidence, which is the probability that the interval contains the true population parameter.
- Confidence level is usually expressed as a percentage, such as 95% or 99%, and it indicates how confident we are that the interval covers the true parameter value.
- Confidence interval can be interpreted as follows: if we repeat the sampling process many times and calculate the confidence interval for each sample, then a certain percentage of the intervals (equal to the confidence level) will contain the true population parameter.
- Confidence interval can be used to assess the precision and reliability of an estimate, to compare the estimates from different samples or populations, and to test hypotheses about the population parameter.
- Confidence interval can be affected by the sample size, the sampling method, the sample variability, and the confidence level.
- Confidence interval can be calculated using different formulas depending on the type of parameter, the distribution of the data, and the availability of the population standard deviation.
- For example, to calculate a 95% confidence interval for the mean of a normally distributed population with known standard deviation, we can use the formula:

$$\bar{x} \pm 1.96 \frac{\sigma}{\sqrt{n}}$$

where $\bar{x}$ is the sample mean, $\sigma$ is the population standard deviation, and $n$ is the sample size.

- To calculate a 95% confidence interval for the proportion of a binomial population, we can use the formula:

$$\hat{p} \pm 1.96 \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

where $\hat{p}$ is the sample proportion and $n$ is the sample size.



### Inference & Significance

- **Inference** is the process of making propositions or conclusions about a population, using data drawn from the population with some form of sampling.
- **Significance** is a term used by researchers to state that it is unlikely their observations could have occurred under the null hypothesis of a statistical test.
- **Null hypothesis** is a statement that assumes there is no difference or relationship between two or more variables of interest.
- **Alternative hypothesis** is a statement that contradicts the null hypothesis and claims there is a difference or relationship between the variables of interest.
- **P-value** is the probability of obtaining a result equal to or more extreme than what was actually observed, given that the null hypothesis is true.
- **Alpha level** is the threshold or cut-off point that determines whether the p-value is small enough to reject the null hypothesis and accept the alternative hypothesis.
- **Statistical significance** means that the p-value is less than or equal to the alpha level, indicating that the observed result is unlikely to occur by chance under the null hypothesis.
- **Confidence interval** is a range of values that is likely to contain the true population parameter with a certain level of confidence.
- **Margin of error** is the maximum possible difference between the point estimate and the true population parameter.
- **Test statistic** is a numerical value that summarizes the sample data and is used to calculate the p-value.
- **Type I error** is the mistake of rejecting the null hypothesis when it is actually true (false positive).
- **Type II error** is the mistake of failing to reject the null hypothesis when it is actually false (false negative).
- **Power** is the probability of correctly rejecting the null hypothesis when it is false (true positive).
- **Effect size** is a measure of the magnitude or strength of the difference or relationship between the variables of interest.

Some common techniques for inferential statistics are:

- **Z-test** for comparing the mean of one sample to a population mean or the means of two samples, when the population standard deviation is known or the sample size is large.
- **T-test** for comparing the mean of one sample to a population mean or the means of two independent or paired samples, when the population standard deviation is unknown or the sample size is small.
- **ANOVA** for comparing the means of more than two independent samples, when the population variances are assumed to be equal.
- **Chi-square test** for comparing the observed frequencies of categorical data to the expected frequencies under the null hypothesis, or for testing the independence of two categorical variables.
- **Correlation** for measuring the strength and direction of the linear relationship between two quantitative variables.
- **Regression** for modeling the relationship between one or more explanatory variables and a response variable, and for making predictions based on the model.
- **Bootstrap** for estimating the sampling distribution of a statistic by resampling with replacement from the original sample, and for constructing confidence intervals based on the bootstrap samples.
- **Permutation** for testing the significance of a difference or relationship between two or more variables by randomly shuffling the values of one variable among the units, and for calculating the p-value based on the permutation distribution.
- **Bayesian inference** for updating the prior beliefs about a population parameter based on the sample data, and for expressing the uncertainty about the parameter using the posterior distribution.



### Estimation and Hypothesis Testing

- Estimation is a statistical process of finding the value of an unknown parameter or quantity based on sample data.
- Hypothesis testing is a statistical process of testing a claim or assumption about a population parameter or quantity based on sample data.
- Estimation and hypothesis testing are related but different methods of inferential statistics, which aim to draw conclusions about a population from a sample.
- Estimation can be divided into two types: point estimation and interval estimation.
  - Point estimation is the process of finding a single value that best represents the unknown parameter or quantity. For example, the sample mean is a point estimate of the population mean.
  - Interval estimation is the process of finding a range of values that contains the unknown parameter or quantity with a certain level of confidence. For example, a 95% confidence interval for the population mean is a range of values that has a 95% probability of containing the true population mean.
- Hypothesis testing can be divided into two types: parametric and non-parametric.
  - Parametric hypothesis testing is the process of testing a claim or assumption about a population parameter using a sample statistic and a probability distribution. For example, a t-test is a parametric test that compares the means of two populations or groups using the sample means and the t-distribution.
  - Non-parametric hypothesis testing is the process of testing a claim or assumption about a population without making any assumptions about the distribution or parameters of the population. For example, a chi-square test is a non-parametric test that compares the observed and expected frequencies of categorical data using the chi-square distribution.
- The general steps of hypothesis testing are:
  - State the null and alternative hypotheses, which are mutually exclusive and exhaustive statements about the population parameter or quantity of interest.
  - Choose a significance level, which is the probability of rejecting the null hypothesis when it is true (Type I error).
  - Collect and analyze the sample data using an appropriate test statistic, which is a function of the sample data that measures the evidence against the null hypothesis.
  - Calculate the p-value, which is the probability of obtaining a test statistic at least as extreme as the observed one, assuming the null hypothesis is true.
  - Compare the p-value with the significance level and make a decision to reject or fail to reject the null hypothesis based on the strength of the evidence.
  - Interpret the results in the context of the problem and state the conclusion in plain language.



### Goodness of fit

- Goodness of fit is a measure of how well a statistical model or distribution matches the observed data.
- Goodness of fit tests are used to compare the observed frequencies or proportions of a categorical variable with the expected frequencies or proportions based on a theoretical model or distribution.
- Goodness of fit tests can be used to test hypotheses such as:
  - Whether a sample of categorical data comes from a specified population or distribution.
  - Whether two or more samples of categorical data come from the same population or distribution.
  - Whether a categorical variable is independent of another categorical variable.
- Some common goodness of fit tests are:
  - Chi-square test: A test that compares the observed and expected frequencies of a categorical variable using the chi-square statistic, which measures the discrepancy between the two frequencies.
  - Kolmogorov-Smirnov test: A test that compares the empirical cumulative distribution function (ECDF) of a continuous variable with a theoretical cumulative distribution function (CDF) using the Kolmogorov-Smirnov statistic, which measures the maximum distance between the two functions.
  - Anderson-Darling test: A test that compares the ECDF of a continuous variable with a theoretical CDF using the Anderson-Darling statistic, which measures the weighted sum of squared distances between the two functions.
  - Shapiro-Wilk test: A test that compares the ECDF of a continuous variable with a normal CDF using the Shapiro-Wilk statistic, which measures the correlation between the ordered data and the corresponding normal quantiles.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write some notes on the topic of Test of Independence for the Unit 2 - Inferential Statistics in the subject of Mathematical Foundation for AI, ML and Data Science. Here are some points that you can use for your study material:

### Test of Independence

- A test of independence is a statistical procedure that determines whether two categorical variables are independent of each other or not.
- Independence means that the occurrence of one variable does not affect the probability of occurrence of the other variable.
- A test of independence is based on a contingency table, which shows the frequency distribution of the two variables in different categories.
- A test of independence uses the chi-square statistic, which measures the discrepancy between the observed frequencies and the expected frequencies under the assumption of independence.
- The null hypothesis of a test of independence is that the two variables are independent, and the alternative hypothesis is that they are dependent or associated.
- The test of independence can be performed using the following steps:
  - Construct a contingency table with the observed frequencies of the two variables in different categories.
  - Calculate the expected frequencies for each cell of the table, using the formula: E = (row total * column total) / grand total
  - Calculate the chi-square statistic, using the formula: X^2 = sum of [(O - E)^2 / E] for all cells, where O is the observed frequency and E is the expected frequency.
  - Find the degrees of freedom, using the formula: df = (number of rows - 1) * (number of columns - 1)
  - Find the p-value, using a chi-square distribution table or a calculator, with the chi-square statistic and the degrees of freedom as inputs.
  - Compare the p-value with the significance level (usually 0.05 or 0.01), and make a decision to reject or fail to reject the null hypothesis.
  - Interpret the results in the context of the problem. If the p-value is less than the significance level, reject the null hypothesis and conclude that the two variables are dependent or associated. If the p-value is greater than or equal to the significance level, fail to reject the null hypothesis and conclude that the two variables are independent or not associated.



### Permutations and Randomization Test

- Permutations and randomization tests are two types of nonparametric statistical tests that can be used to compare two or more samples without making any assumptions about the underlying population distribution.
- Permutations and randomization tests are based on the idea of shuffling or rearranging the data in some way to create different possible scenarios under the null hypothesis of no difference between the samples.
- Permutations and randomization tests differ in how they generate the scenarios and how they calculate the p-value for the test statistic.

#### Permutation Test

- A permutation test involves two or more samples. The null hypothesis is that all samples come from the same distribution.
- A permutation test is conducted by following these three steps:
  - Compute some test statistic using the set of original observations.
  - Re-arrange the observations in all possible orders, computing the test statistic each time. This creates the permutation distribution of the test statistic under the null hypothesis.
  - Calculate the permutation test p-value, which is the proportion of permutations that have a test statistic as extreme or more extreme than the observed one.
- A permutation test is an exact test, meaning that it gives the exact p-value without any approximation or error. However, a permutation test can be computationally intensive, especially when the sample size is large or the number of samples is more than two, as the number of possible permutations grows exponentially.
- A permutation test assumes that the data is sampled randomly from an underlying population distribution (the population model). This means that the conclusions drawn from the permutation test are generally applicable to other data from the population.

#### Randomization Test

- A randomization test is also called a re-randomization test or a random assignment test. It is based on the idea of randomly assigning the observations to different groups or treatments, as in a randomized experiment.
- A randomization test involves two or more groups or treatments. The null hypothesis is that there is no difference between the groups or treatments in terms of the outcome variable.
- A randomization test is conducted by following these three steps:
  - Compute some test statistic using the set of original observations.
  - Re-assign the observations to different groups or treatments in a random manner, computing the test statistic each time. This creates the randomization distribution of the test statistic under the null hypothesis.
  - Calculate the randomization test p-value, which is the proportion of randomizations that have a test statistic as extreme or more extreme than the observed one.
- A randomization test is an approximate test, meaning that it gives an approximate p-value that may have some error. However, a randomization test can be computationally efficient, as it does not require generating all possible permutations, but only a large enough number of randomizations to get a reliable estimate of the p-value.
- A randomization test does not assume any population model, but only relies on the random assignment procedure. This means that the conclusions drawn from the randomization test are only applicable to the specific data and the specific randomization method used.



### t-test/z-test (one sample, independent, paired)

- A t-test is a statistical test that is used to compare the means of two groups or the mean of one group against a known value. It is often used in hypothesis testing to determine whether a process or treatment actually has an effect on the population of interest, or whether two groups are different from one another.
- A z-test is a statistical test that is used to test the hypothesis that proportions from two independent samples differ greatly. It is also used to test the hypothesis that the mean of a population is equal to a specified value, when the population standard deviation is known.
- Both t-test and z-test are parametric tests, which means they assume that the samples are normally distributed. However, the t-test is more robust than the z-test, as it can handle situations where the population standard deviation is unknown or the sample size is small.
- There are three main types of t-test:
  - One sample t-test: A statistical test that compares the mean of one group against a known value. For example, testing whether the average height of students in a class is equal to 170 cm.
  - Independent sample t-test: A statistical test that compares the means of two independent groups. For example, testing whether the average weight of males and females in a population is different.
  - Paired sample t-test: A statistical test that compares the means of two dependent or matched groups. For example, testing whether the blood pressure of patients before and after a treatment is different.
- There are two main types of z-test:
  - One sample z-test: A statistical test that compares the proportion or mean of one group against a known value, when the population standard deviation is known. For example, testing whether the proportion of voters who support a candidate is equal to 50%.
  - Two sample z-test: A statistical test that compares the proportions or means of two independent groups, when the population standard deviations are known. For example, testing whether the proportion of smokers in two cities is different.



### ANOVA

- ANOVA stands for **Analysis of Variance**, a statistical test that compares the means of three or more groups on a continuous variable.
- The null hypothesis of ANOVA is that there is **no significant difference** between the group means, while the alternative hypothesis is that **at least one** group mean is different from the others.
- ANOVA can be used to test the effects of different factors or treatments on a response variable, such as the impact of studying technique on exam scores or the effect of tea on weight loss.
- There are different types of ANOVA, depending on the number and nature of the factors or treatments involved. Some common types are:
  - **One-way ANOVA**: tests the effect of one factor with two or more levels on a response variable. For example, testing the effect of social media use (low, medium, high) on hours of sleep per night.
  - **Two-way ANOVA**: tests the effect of two factors, each with two or more levels, on a response variable, as well as the interaction between the factors. For example, testing the effect of gender (male, female) and exercise (low, medium, high) on blood pressure, and whether the effect of exercise depends on gender.
  - **Repeated measures ANOVA**: tests the effect of one or more factors on a response variable measured at different time points or under different conditions for the same subjects. For example, testing the effect of a drug (placebo, low dose, high dose) on pain level measured at three time points (before, during, after) for the same patients.
  - **ANCOVA**: stands for **Analysis of Covariance**, a type of ANOVA that adjusts the group means for the effect of one or more continuous variables, called covariates, that may influence the response variable. For example, testing the effect of studying technique (flashcards, notes, practice tests) on exam scores, while controlling for the effect of prior knowledge (measured by a pre-test) on exam scores.
- To perform an ANOVA, some assumptions must be met, such as:
  - The response variable is normally distributed within each group.
  - The groups have equal variances, also known as homogeneity of variance.
  - The observations are independent within and between groups.
- If the assumptions are violated, alternative methods may be used, such as non-parametric tests or transformations.
- To conduct an ANOVA, the following steps are usually followed:
  - Define the null and alternative hypotheses.
  - Choose the appropriate type of ANOVA based on the research question and the data.
  - Check the assumptions of ANOVA using graphical and numerical methods.
  - Calculate the ANOVA table, which summarizes the sources of variation and the corresponding sums of squares, degrees of freedom, mean squares, and F-statistics.
  - Compare the F-statistic with the critical value or the p-value with the significance level to make a decision about the null hypothesis.
  - If the null hypothesis is rejected, perform post-hoc tests to identify which groups are significantly different from each other.
  - Report and interpret the results of ANOVA and post-hoc tests.
- ANOVA is a powerful and widely used technique for comparing group means and testing the effects of factors or treatments on a response variable. However, it also has some limitations, such as:
  - It does not provide information about the direction or magnitude of the differences between groups.
  - It may not detect small differences between groups if the sample size is small or the variance is large.
  - It may not account for the effects of confounding variables or interactions that are not included in the model.
  - It may not be applicable if the assumptions are severely violated or the data are not suitable for ANOVA.

: https://www.thoughtco.com/analysis-of-variance-anova-3026693
: https://www.scribbr.com/statistics/one-way-anova/
: https://www.statology.org/ancova/
: https://www.stat



### Chi-square test

- A chi-square test is a statistical hypothesis test used to compare observed and expected frequencies of categorical data.
- It can be used to test the independence or association of two or more categorical variables, the goodness of fit of a theoretical distribution to observed data, or the homogeneity or difference of population variances .
- The test statistic, chi-square (Χ²), is calculated by summing the squared differences between the observed and expected frequencies, divided by the expected frequencies.
- The formula for chi-square is:

chi-square formula

- Where O is the observed frequency, E is the expected frequency, and k is the number of categories.
- The expected frequency for each category is calculated by multiplying the row total and the column total, divided by the grand total.
- The chi-square test statistic follows a chi-square distribution with degrees of freedom (df) equal to the number of categories minus one.
- The chi-square distribution is a family of curves that depends on the degrees of freedom. As the degrees of freedom increase, the curve becomes more symmetrical and bell-shaped.
- The chi-square test has a null hypothesis (H0) that states that there is no significant difference between the observed and expected frequencies, or that the variables are independent.
- The alternative hypothesis (Ha) states that there is a significant difference between the observed and expected frequencies, or that the variables are dependent.
- The chi-square test has a significance level (α) that determines the probability of rejecting the null hypothesis when it is true. Common values for α are 0.05, 0.01, or 0.001.
- The chi-square test has a critical value (Χ²c) that corresponds to the significance level and the degrees of freedom. It can be found in a chi-square table.
- The chi-square test has a p-value that represents the probability of obtaining a chi-square value equal to or more extreme than the observed one, assuming the null hypothesis is true.
- The chi-square test has a decision rule that compares the test statistic, the critical value, and the p-value to determine whether to reject or fail to reject the null hypothesis.
- The chi-square test has a conclusion that interprets the results in the context of the research question.
- The chi-square test has some assumptions that must be met for the test to be valid. These include:

  - The data must be in the form of frequencies, not percentages or proportions.
  - The categories must be mutually exclusive and exhaustive.
  - The expected frequencies for each category must be at least 5.
  - The observations must be independent and randomly sampled.

- The chi-square test has some limitations that must be considered when using it. These include:

  - The test is sensitive to sample size, meaning that large samples may result in significant differences even if they are trivial.
  - The test does not provide information about the direction or strength of the relationship between the variables.
  - The test does not account for measurement errors or confounding variables.

- The chi-square test has some applications in various fields of study, such as biology, psychology, sociology, education, and business . Some examples of research questions that can be answered by the chi-square test are:

  - Is there a relationship between gender and political affiliation?
  - Does the distribution of blood types in a population match the expected distribution?



### Linear Methods for Regression Analysis

- Regression analysis is a statistical technique that aims to explore the relationship between a dependent variable (output) and one or more independent variables (inputs).
- Linear regression is a type of regression that assumes a linear relationship between the dependent and independent variables, meaning that the change in the output is proportional to the change in the input.
- Linear regression can be used to model various phenomena, such as the effect of advertising on sales, the relationship between height and weight, the impact of education on income, etc.
- Linear regression can be divided into two categories: simple linear regression and multiple linear regression.
  - Simple linear regression involves only one independent variable and one dependent variable. The equation of the simple linear regression line is Y = a + bX + c, where Y is the output, X is the input, a is the intercept, b is the slope, and c is the error term.
  - Multiple linear regression involves more than one independent variable and one dependent variable. The equation of the multiple linear regression line is Y = a + b1X1 + b2X2 + ... + bnXn + c, where Y is the output, X1, X2, ..., Xn are the inputs, a is the intercept, b1, b2, ..., bn are the slopes, and c is the error term.
- The goal of linear regression is to find the values of the intercept and the slopes that minimize the sum of squared errors (SSE), which is the difference between the observed and predicted values of the output.
- There are various methods to estimate the intercept and the slopes, such as the least squares method, the maximum likelihood method, the gradient descent method, etc.
- Linear regression has some assumptions that need to be checked before applying the technique, such as:
  - The dependent and independent variables show a linear relationship between the slope and the intercept.
  - The independent variable is not random.
  - The value of the error term is zero on average.
  - The value of the error term is constant across all observations (homoscedasticity).
  - The value of the error term is not correlated across all observations (independence).
  - The error term follows a normal distribution (normality).
- Linear regression can be evaluated by various measures, such as the coefficient of determination (R-squared), the standard error of the estimate, the F-test, the t-test, the confidence intervals, the residual analysis, etc.
- Linear regression can be extended to handle nonlinear relationships, categorical variables, interactions, transformations, etc. by using techniques such as polynomial regression, logistic regression, dummy variables, interaction terms, power functions, etc.



### Multiple Regression Analysis

- Multiple regression analysis is a statistical evaluation tool that predicts the value of a dependent variable based on the values of two or more independent variables.
- Multiple regression analysis is an extension of linear regression, which predicts the value of a dependent variable based on the value of one independent variable.
- Multiple regression analysis can be used for various purposes, such as:
  - Giving insight into predictive factors that affect the dependent variable.
  - Predicting factors that affect outcomes of interest, such as sales, profits, customer satisfaction, etc.
  - Creating models that explain the relationships among variables and test hypotheses.
  - Controlling for confounding variables that may influence the dependent variable.
- The formula for a multiple linear regression, which is a type of multiple regression analysis, is:

  - y = b0 + b1x1 + b2x2 + ... + bnxn + e
  - where:
    - y is the predicted value of the dependent variable
    - b0 is the y-intercept (value of y when all other parameters are set to 0)
    - b1, b2, ..., bn are the regression coefficients of the independent variables x1, x2, ..., xn
    - e is the error term (residual)
- To conduct a multiple regression analysis, the following steps are usually followed:
  - Define the research question and hypotheses
  - Select the dependent and independent variables
  - Check the assumptions of linearity, normality, homoscedasticity, independence, multicollinearity, and outliers
  - Run the multiple regression analysis and interpret the results
  - Report the findings and conclusions



### Orthogonalization by Householder transformations (QR)

- Orthogonalization is the process of finding a set of orthogonal vectors that span the same subspace as a given set of vectors.
- Orthogonal vectors are those that are perpendicular to each other, i.e. their dot product is zero.
- Orthogonal vectors have the property that they are linearly independent and form a basis for the subspace they span.
- Orthogonalization is useful for many applications, such as solving linear systems, finding least squares solutions, computing eigenvalues and eigenvectors, etc.
- One method for performing orthogonalization is the Householder transformation, which uses reflection across a hyperplane to zero out some components of a vector.
- A Householder transformation can be expressed as a matrix of the form H = I - 2vv^T, where v is a unit normal vector to the hyperplane of reflection, and I is the identity matrix.
- A Householder transformation is an orthogonal matrix, i.e. H^T = H^-1, and preserves the length of any vector, i.e. ||Hx|| = ||x|| for any x.
- A Householder transformation can be used to orthogonalize a set of vectors by applying it successively to each vector and subtracting its projection onto the previous orthogonal vectors.
- This process is equivalent to finding the QR decomposition of a matrix A, where A = QR, Q is an orthogonal matrix whose columns are the orthogonalized vectors, and R is an upper triangular matrix whose diagonal entries are the lengths of the orthogonalized vectors.
- The QR decomposition can be computed efficiently by using the Householder transformation to introduce zeros into the lower triangle of A, and storing the vectors v in the lower triangle of R.
- The QR decomposition can be used to solve linear systems, find least squares solutions, compute eigenvalues and eigenvectors, etc. by exploiting the properties of Q and R.



### Singular Value Decomposition (SVD)

- SVD is a factorization of a real or complex matrix into three matrices: A = UDV^T, where U and V are orthonormal and D is diagonal with positive real entries .
- SVD generalizes the eigendecomposition of a square normal matrix with an orthonormal eigenbasis to any matrix.
- SVD has some interesting algebraic properties and conveys important geometrical and theoretical insights about linear transformations.
- SVD produces orthonormal bases of v's and u's for the four fundamental subspaces of a matrix: column space, row space, null space and left null space.
- SVD is useful in many tasks, such as data compression, dimensionality reduction, image processing, signal processing, etc.
- SVD can be computed using various algorithms, such as the power method, the QR algorithm, the Jacobi algorithm, etc.



### Linear Dimension Reduction Using Principal Component Analysis (PCA)

- Linear dimension reduction is a technique that aims to reduce the number of variables or features in a data set while preserving as much information as possible.
- Principal component analysis (PCA) is one of the most popular linear dimension reduction algorithms. It is a projection based method that transforms the data by projecting it onto a set of orthogonal (perpendicular) axes .
- The axes are called principal components (PCs) and they are ordered by the amount of variance they explain in the data. The first PC explains the most variance, the second PC explains the most variance among the remaining ones, and so on.
- The PCs are linear combinations of the original variables, and they are uncorrelated with each other. The coefficients of the linear combinations are called loadings and they indicate how much each variable contributes to each PC.
- PCA can be performed by using eigenvalue decomposition or singular value decomposition (SVD) of the covariance matrix or the correlation matrix of the data .
- PCA can be used for various purposes, such as data compression, data visualization, feature extraction, noise reduction, and data analysis  .
- PCA has some limitations, such as being sensitive to outliers, being affected by scaling of the variables, and being unable to capture nonlinear relationships in the data .



## Unit 3 - Pseudo-Random Numbers

- Pseudo-random numbers are numbers that appear to be random but are actually generated by a deterministic algorithm.
- Pseudo-random number generators (PRNGs) are algorithms that produce sequences of pseudo-random numbers using a seed value and a mathematical formula.
- PRNGs are useful for applications that require randomness, such as cryptography, simulations, games, and statistical analysis.
- PRNGs have different properties and quality criteria, such as period, uniformity, independence, and unpredictability.
- PRNGs can be classified into two types: linear and nonlinear.
- Linear PRNGs use linear operations, such as addition, multiplication, and modulo, to generate pseudo-random numbers. Examples of linear PRNGs are linear congruential generators (LCGs) and linear feedback shift registers (LFSRs).
- Nonlinear PRNGs use nonlinear operations, such as bitwise operations, exponentiation, and hashing, to generate pseudo-random numbers. Examples of nonlinear PRNGs are Blum Blum Shub (BBS), Mersenne Twister (MT), and secure hash algorithms (SHAs).
- PRNGs can also be classified into two categories: cryptographic and non-cryptographic.
- Cryptographic PRNGs are designed to produce pseudo-random numbers that are hard to predict, even by an attacker who knows the algorithm and the seed. Cryptographic PRNGs are suitable for security-related applications, such as encryption, authentication, and digital signatures.
- Non-cryptographic PRNGs are designed to produce pseudo-random numbers that are fast and efficient, but not necessarily secure. Non-cryptographic PRNGs are suitable for non-security-related applications, such as simulations, games, and sampling.
- PRNGs can be tested for their randomness and quality using various methods, such as statistical tests, empirical tests, and theoretical analysis. Some examples of randomness tests are frequency test, runs test, autocorrelation test, and chi-square test.



### Random number generation

- Random number generation is a process by which a sequence of numbers or symbols that cannot be reasonably predicted better than by random chance is generated.
- Random numbers are useful for many applications, such as cryptography, simulation, gaming, statistical sampling, and scientific experiments.
- There are two main types of random number generators: hardware-based and pseudo-random.
- Hardware-based random number generators use physical devices or phenomena, such as dice, coins, quantum effects, or radioactive decay, to produce random outcomes .
- Pseudo-random number generators use mathematical algorithms or functions, such as linear congruential generators, Mersenne Twister, or Blum Blum Shub, to produce sequences of numbers that appear random but are actually deterministic and reproducible .
- Pseudo-random number generators have advantages over hardware-based ones, such as speed, portability, and scalability, but they also have limitations, such as periodicity, correlation, and predictability .
- Pseudo-random number generators require an initial value or seed to start the sequence, which can be chosen randomly or based on some external input .
- The quality of a pseudo-random number generator can be measured by various statistical tests, such as frequency, runs, autocorrelation, or chi-square tests, that check how well the generated sequence matches the expected properties of a true random sequence .
- Some applications require true random numbers, which can be obtained from hardware-based generators or online services, such as RANDOM.ORG, that use atmospheric noise or other sources of randomness to generate numbers.
- Some applications require cryptographically secure random numbers, which can be obtained from hardware-based generators or special pseudo-random number generators, such as Yarrow, Fortuna, or NIST SP 800-90A, that use cryptographic techniques to ensure the unpredictability and secrecy of the generated numbers .



### Inverse-transform method for pseudo-random number generation

- The inverse-transform method is a basic technique for generating pseudo-random numbers from any probability distribution given its cumulative distribution function (CDF) .
- The CDF of a random variable X is the function that gives the probability that X is less than or equal to a given value x, i.e., F_X(x) = P(X <= x) .
- The inverse-transform method works as follows  :
  - Generate a uniform random number U between 0 and 1.
  - Find the inverse of the CDF, F_X^{-1}(u), such that F_X^{-1}(u) = x if and only if F_X(x) = u.
  - Return F_X^{-1}(U) as the pseudo-random number from the distribution of X.
- The inverse-transform method is based on the fact that if U is a uniform random variable on [0, 1], then F_X^{-1}(U) has the same distribution as X  .
- The inverse-transform method can be used to generate pseudo-random numbers from any distribution that has a known and invertible CDF  .
- Some examples of distributions that have known and invertible CDFs are the exponential, normal, Poisson, binomial, and geometric distributions  .
- The inverse-transform method has some advantages and disadvantages  :
  - Advantages:
    - It is simple and intuitive to implement.
    - It can be applied to any distribution that has a known and invertible CDF.
    - It can be easily extended to generate multivariate random variables by using the inverse of the joint CDF.
  - Disadvantages:
    - It may be computationally expensive or difficult to find the inverse of the CDF, especially for complex or continuous distributions.
    - It may suffer from numerical errors or instability due to rounding or truncation of the CDF or its inverse.
    - It may not be efficient or accurate for generating random variables from distributions that have heavy tails or high variance.



### Acceptance-Rejection Method

- The acceptance-rejection method is a technique for generating pseudorandom numbers from a target distribution, given a proposal distribution that is easy to sample from and that covers the target distribution.
- The basic idea is to generate a pair of random numbers, one from the proposal distribution and one from the uniform distribution, and accept the first one as a sample from the target distribution if it satisfies a certain criterion, otherwise reject it and repeat the process.
- The criterion is based on comparing the ratio of the target density and the proposal density with the uniform random number, and accepting the sample if the ratio is greater than or equal to the uniform random number.
- The acceptance-rejection method requires a constant c such that the target density is always less than or equal to c times the proposal density over the common support of the two distributions. The smaller the c, the more efficient the method is, as the acceptance rate is inversely proportional to c.
- The acceptance-rejection method can be used to generate random numbers from various distributions, such as exponential, normal, gamma, beta, etc., by choosing appropriate proposal distributions, such as uniform, exponential, normal, etc.



### Transformations for the notes of the Unit 3 - Pseudo-Random Numbers

- Pseudo-random numbers are numbers that are generated by a deterministic algorithm that mimics the properties of random numbers, such as uniformity and independence.
- Pseudo-random number generators (PRNGs) are functions that take a seed (a short random value) and produce a longer sequence of pseudo-random numbers.
- There are different types of PRNGs, such as linear congruential generators, linear feedback shift registers, and Blum Blum Shub. Each PRNG has its own parameters, such as modulus, multiplier, increment, and feedback polynomial, that affect its period, quality, and security.
- To generate pseudo-random numbers from other distributions than the uniform distribution, there are several methods that can be used, such as:
  - The probability integral transform: This method uses the inverse of the cumulative distribution function (CDF) of the desired distribution to map uniform pseudo-random numbers to the target distribution. For example, if F is the CDF of the exponential distribution with parameter lambda, then F^-1 (U) is an exponential pseudo-random number, where U is a uniform pseudo-random number.
  - The rejection method: This method generates pseudo-random numbers from a proposal distribution that is easy to sample from and has a similar shape to the target distribution. Then, it rejects some of the samples based on a criterion that ensures the final samples have the target distribution. For example, if f is the target density function and g is the proposal density function, then the criterion is to accept X ~ g if U < f(X) / (M * g(X)), where U is a uniform pseudo-random number and M is a constant such that f(X) / g(X) <= M for all X.
  - The convolution method: This method generates pseudo-random numbers from the target distribution by summing several generated pseudo-random numbers with the appropriate distribution. For example, if X1, X2, ..., Xn are independent and identically distributed (iid) Bernoulli(p) pseudo-random numbers, then X1 + X2 + ... + Xn is a binomial(n, p) pseudo-random number.
  - The transformation method: This method generates pseudo-random numbers from the target distribution by applying a transformation to a pseudo-random number from a related distribution. For example, if X is a standard normal pseudo-random number, then Y = mu + sigma * X is a normal(mu, sigma^2) pseudo-random number, where mu and sigma are the mean and standard deviation parameters.



### Multivariate Probability Calculations

- Multivariate probability is the study of random variables that are jointly distributed over a sample space. It involves the calculation of probabilities of events that depend on more than one random variable. 
- Multivariate probability distributions are functions that assign probabilities to vectors of random variables. There are many types of multivariate distributions, such as multivariate normal, multivariate binomial, multivariate Poisson, etc. 
- One example of a multivariate distribution is the multinomial distribution, which is a generalization of the binomial distribution. It is used to model the outcomes of a multinomial experiment, which is an experiment that has a fixed number of trials, each with a finite number of possible outcomes, and the probability of each outcome is constant across trials. 
- The probability mass function of a multinomial distribution is given by:

$$
P(X_1 = x_1, X_2 = x_2, \dots, X_k = x_k) = \frac{n!}{x_1! x_2! \dots x_k!} p_1^{x_1} p_2^{x_2} \dots p_k^{x_k}
$$

where $n$ is the number of trials, $k$ is the number of possible outcomes, $x_i$ is the number of times outcome $i$ occurs, and $p_i$ is the probability of outcome $i$. The conditions for a multinomial distribution are:

- $n$ is fixed and known
- Each trial has $k$ possible outcomes
- The trials are independent
- The probabilities of the outcomes are constant and sum to 1

- To calculate the probability of a multivariate event using a multinomial distribution, we need to identify the values of $n$, $k$, $x_i$, and $p_i$, and plug them into the formula. For example, suppose we toss a fair die 10 times and want to find the probability of getting exactly 2 ones, 3 twos, and 5 threes. In this case, we have:

- $n = 10$
- $k = 6$
- $x_1 = 2, x_2 = 3, x_3 = 5, x_4 = x_5 = x_6 = 0$
- $p_1 = p_2 = p_3 = p_4 = p_5 = p_6 = 1/6$

- Plugging these values into the formula, we get:

$$
P(X_1 = 2, X_2 = 3, X_3 = 5) = \frac{10!}{2! 3! 5! 0! 0! 0!} \left(\frac{1}{6}\right)^{2} \left(\frac{1}{6}\right)^{3} \left(\frac{1}{6}\right)^{5} \left(\frac{1}{6}\right)^{0} \left(\frac{1}{6}\right)^{0} \left(\frac{1}{6}\right)^{0}
$$

$$
= \frac{10 \times 9 \times 8 \times 7 \times 6}{2 \times 3 \times 5 \times 6^6} = \frac{504}{6^7} \approx 0.0037
$$

- This is the probability of getting exactly 2 ones, 3 twos, and 5 threes in 10 tosses of a fair die.



### Monte Carlo Integration

- Monte Carlo integration is a technique for numerical integration using random numbers .
- It is a particular Monte Carlo method that numerically computes a definite integral.
- While other algorithms usually evaluate the integrand at a regular grid, Monte Carlo randomly chooses points at which the integrand is evaluated .
- The basic concept of the Monte Carlo estimator is to approximate the value of the integral by the average value of the integrand at the random points.
- The Monte Carlo estimator converges to the true value of the integral as the number of random points increases, according to the law of large numbers.
- The advantage of Monte Carlo integration is that it can handle complex domains and high-dimensional integrals, where other methods may fail or be inefficient .
- The disadvantage of Monte Carlo integration is that it is a non-deterministic approach, meaning that each realization provides a different outcome with respective error bars.
- The error of Monte Carlo integration depends on the variance of the integrand and the number of random points, and it decreases as the inverse square root of the number of points  .
- There are various ways to improve the accuracy and efficiency of Monte Carlo integration, such as importance sampling, stratified sampling, quasi-Monte Carlo methods, and variance reduction techniques   .



### Simulation and Monte Carlo integration

Simulation is a computational technique that uses random numbers to generate and analyze data that mimic real-world phenomena. Simulation can be used to study complex systems that are difficult or impossible to model analytically, such as physical, biological, social, or economic systems. Simulation can also be used to test hypotheses, evaluate policies, optimize designs, or estimate uncertainties.

Monte Carlo integration is a specific type of simulation that can be used to estimate definite integrals that cannot be easily solved by analytical methods. Monte Carlo integration is based on the idea of using random samples to approximate the area under a curve. Monte Carlo integration can be applied to integrals of any dimension, shape, or complexity.

The basic steps of Monte Carlo integration are:

- Define the domain of integration and the integrand function.
- Generate random points within the domain of integration, using a uniform or non-uniform distribution.
- Evaluate the integrand function at each random point.
- Calculate the average value of the function over the random points.
- Multiply the average value by the volume of the domain of integration to obtain an estimate of the integral.

The accuracy of Monte Carlo integration depends on the number of random points used and the variance of the integrand function. The more random points are used, the more likely the estimate is to converge to the true value of the integral. The lower the variance of the integrand function, the less random points are needed to achieve a given accuracy. The error of Monte Carlo integration can be estimated by using the standard deviation of the function values over the random points, divided by the square root of the number of points.

Monte Carlo integration has several advantages over other numerical methods, such as:

- It can handle integrals of any dimension, shape, or complexity, without requiring special techniques or transformations.
- It can easily incorporate constraints or conditions on the integrand function or the domain of integration.
- It can exploit the properties of the integrand function, such as symmetry, periodicity, or sparsity, to improve the efficiency or accuracy of the estimation.
- It can be parallelized or distributed to speed up the computation.

Monte Carlo integration also has some limitations, such as:

- It can be computationally expensive, especially for high-dimensional or high-variance integrals.
- It can be affected by the quality of the random number generator or the sampling distribution used.
- It can be difficult to assess the convergence or the error of the estimation.



### Variance Reduction

- Variance reduction is a set of techniques that aim to improve the accuracy and efficiency of Monte Carlo simulations by reducing the variance of the estimator without changing its expected value.
- Variance reduction techniques are useful when the estimator has a high variance, which means that it fluctuates a lot around the true value and requires a large number of samples to achieve a desired level of precision.
- Some common variance reduction techniques are:

  - **Common random numbers (CRN)**: This technique applies when comparing two or more alternative configurations of a system using the same random numbers to generate the samples for each configuration. This induces a positive correlation between the estimators and reduces the variance of their difference.
  - **Control variates**: This technique uses a known quantity that is correlated with the quantity of interest to adjust the estimator and reduce its variance. The known quantity is called a control variate and its value and variance are either known or easy to compute.
  - **Partial integration**: This technique reduces the variance by replacing some integrals over random variables or regions of space by their exact values, which are either known or easy to compute. This technique is also known as Rao-Blackwellization.
  - **Systematic sampling**: This technique uses a deterministic or structured way of selecting the samples instead of a purely random way. This can reduce the variance by ensuring a more uniform coverage of the sample space and avoiding clustering or gaps. Some examples of systematic sampling methods are antithetic variates, stratified sampling, and quasi-Monte Carlo integration.
  - **Importance sampling**: This technique changes the probability distribution of the random variables to sample from a more relevant or informative region of the sample space. This can reduce the variance by assigning more weight to the samples that have a larger impact on the estimator. The weights are adjusted by the ratio of the original and the new probability distributions.
  - **Rare event sampling**: This technique is a special case of importance sampling that focuses on estimating the probability or frequency of rare events that have a very low probability of occurrence. This can reduce the variance by using an importance function that increases the probability of sampling the rare events and reduces the probability of sampling the common events.



### Monte Carlo hypothesis testing

- Monte Carlo hypothesis testing is a method for conducting statistical tests using simulated data under the null hypothesis .
- The null hypothesis is the assumption that there is no significant difference or relationship between the variables of interest.
- The test statistic is a numerical measure that summarizes the evidence against the null hypothesis, such as the mean difference, the correlation coefficient, or the chi-square value.
- The p-value is the probability of obtaining a test statistic at least as extreme as the observed one, assuming the null hypothesis is true.
- The p-value is used to make a decision about the null hypothesis: if the p-value is smaller than a pre-specified significance level (usually 0.05), then the null hypothesis is rejected; otherwise, it is not rejected.
- Monte Carlo hypothesis testing involves the following steps  :
  - Specify the null hypothesis and the alternative hypothesis.
  - Choose a test statistic that is sensitive to the difference or relationship between the variables of interest.
  - Generate a large number of simulated data sets that follow the null hypothesis, using random number generators or other methods.
  - Calculate the test statistic for each simulated data set and store the results in a vector.
  - Compare the observed test statistic from the original data set with the vector of simulated test statistics, and count how many simulated test statistics are at least as extreme as the observed one.
  - Divide the count by the number of simulated data sets to obtain the p-value.
  - Compare the p-value with the significance level and make a decision about the null hypothesis.
- Monte Carlo hypothesis testing has some advantages over traditional hypothesis testing  :
  - It does not require any assumptions about the distribution of the test statistic or the data, such as normality, independence, or homogeneity of variance.
  - It can be applied to any test statistic, even if its distribution is unknown or complicated.
  - It can handle complex models and data structures, such as nonlinear regression, multilevel models, or spatial data.
  - It can provide exact p-values, without any approximation or correction.
  - It can control the level of the test, which is the probability of rejecting the null hypothesis when it is true, by adjusting the number of simulated data sets.
- Monte Carlo hypothesis testing also has some limitations and challenges  :
  - It can be computationally intensive and time-consuming, especially for large or complex data sets and models.
  - It can be affected by the quality and randomness of the simulated data sets, which depend on the choice of random number generators and other parameters.
  - It can be difficult to specify the null hypothesis and the alternative hypothesis, especially for complex models and data structures.
  - It can be sensitive to the choice of the test statistic, which should be appropriate for the research question and the data.
  - It can be influenced by the significance level, which should be chosen carefully and reported clearly.



### Antithetic Variables/Control Variates

- Antithetic variables and control variates are two variance reduction techniques used in Monte Carlo methods.
- Monte Carlo methods are a class of algorithms that use random sampling to approximate numerical integrals or expectations of functions.
- Variance reduction techniques aim to improve the accuracy and efficiency of Monte Carlo methods by reducing the variance of the estimator.

#### Antithetic Variables

- The antithetic variables method is based on the idea of using the opposite or complementary values of the random variables to cancel out some of the randomness.
- For example, if X is a random variable with a uniform distribution on [a,b], then its antithetic variable is Y = a + b - X, which has the same distribution as X but is negatively correlated with X.
- The antithetic variables method works as follows:

  - Generate n pairs of random variables (X1, Y1), ..., (Xn, Yn) such that Xi and Yi are antithetic variables for i = 1, ..., n.
  - Evaluate the function of interest g at each pair of random variables and take the average of the two values: Zi = (g(Xi) + g(Yi))/2 for i = 1, ..., n.
  - Use the sample mean of Zi as the estimator of the expectation of g: Z = (1/n) * sum(Zi) for i = 1, ..., n.

- The antithetic variables method reduces the variance of the estimator Z if the function g is monotonic and the random variables X and Y are negatively correlated.
- The antithetic variables method is simple to implement and does not require any additional information about the function g or the distribution of X.

#### Control Variates

- The control variates method is based on the idea of using a known function h that is correlated with the function of interest g to adjust the estimator of the expectation of g.
- For example, if X is a random variable with a normal distribution and g(X) is the payoff of a European call option, then h(X) could be the payoff of a European put option with the same strike price and maturity, which has a known analytical formula.
- The control variates method works as follows:

  - Generate n random variables X1, ..., Xn from the distribution of X.
  - Evaluate the functions g and h at each random variable: gi = g(Xi) and hi = h(Xi) for i = 1, ..., n.
  - Use the sample mean of gi as the naive estimator of the expectation of g: G = (1/n) * sum(gi) for i = 1, ..., n.
  - Use the sample mean of hi as the estimator of the expectation of h: H = (1/n) * sum(hi) for i = 1, ..., n.
  - Choose a constant c that minimizes the variance of the estimator Z = G + c * (H - E[h(X)]), where E[h(X)] is the known expectation of h.
  - Use Z as the estimator of the expectation of g.

- The control variates method reduces the variance of the estimator Z if the function h is correlated with the function g and the constant c is chosen appropriately.
- The control variates method requires some additional information about the function h and its expectation, which may not be easy to obtain or compute.



### Importance sampling

- Importance sampling is a **variance reduction technique** that can be used in the **Monte Carlo method**.
- The idea behind importance sampling is that certain values of the input random variables in a simulation have more impact on the parameter being estimated than others.
- Importance sampling can be used to evaluate properties of a particular distribution, while only having samples generated from a different distribution than the distribution of interest.
- The basic idea of importance sampling is to sample the states from a different distribution to lower the variance of the estimation of E[X;P], or when sampling from P is difficult.
- This is accomplished by first choosing a random variable L such that E[L;P] = 1 and that L > 0 P-almost everywhere.
- Then, the expectation of X with respect to P can be written as E[X;P] = E[XL;P] = E[X/L;L].
- The last equality follows from the law of total expectation.
- The random variable L is called the **importance sampling function** or the **likelihood ratio**.
- The distribution L is called the **importance sampling distribution** or the **proposal distribution**.
- The importance sampling function L should be chosen such that it is **similar** to X and **easy** to sample from.
- A good choice of L can significantly reduce the variance of the estimator.
- A bad choice of L can increase the variance or even make the estimator invalid.
- An example of importance sampling is to estimate the probability of a rare event.
- Suppose we want to estimate the probability that a standard normal random variable Z is greater than 5.
- Sampling directly from the standard normal distribution would require a very large number of samples to observe such an event.
- Instead, we can sample from a normal distribution with mean 5 and standard deviation 1, which has a higher probability of generating values greater than 5.
- Then, the importance sampling function is L = f(Z)/g(Z), where f is the standard normal density and g is the normal density with mean 5 and standard deviation 1.
- The estimator of the probability is then the average of L times the indicator function of Z > 5 over the samples.
- This estimator has a much lower variance than the naive estimator based on the standard normal samples.



### Stratified Sampling

Stratified sampling is a method of sampling from a population that can be divided into subgroups or strata that share some common characteristics. The purpose of stratified sampling is to ensure that each subgroup is adequately represented in the sample, and to reduce the sampling error and increase the precision of the estimates.

Some examples of stratified sampling are:

- A survey of students' academic performance that divides the population into subgroups by grade level, and then randomly selects a proportional number of students from each grade.
- A study of customer satisfaction that splits the population into subgroups by product category, and then randomly chooses a fixed number of customers from each category.
- A simulation of a random process that partitions the population into subgroups by the probability of an event, and then randomly generates outcomes from each subgroup according to their probabilities.

The steps to perform stratified sampling are:

1. Define the population and the subgroups of interest.
2. Separate the population into non-overlapping strata based on the chosen criteria.
3. Determine the sample size for each stratum, either proportionally or equally.
4. Randomly select the sample units from each stratum using simple random sampling or systematic sampling.
5. Combine the sample units from all strata to form the final sample.

Some advantages of stratified sampling are:

- It can improve the accuracy and representativeness of the sample by reducing the sampling variability within each stratum.
- It can ensure that all subgroups of the population are included in the sample, especially when some subgroups are rare or small in size.
- It can allow for separate analysis and comparison of the subgroups, as well as the overall population.

Some disadvantages of stratified sampling are:

- It can be difficult and costly to identify and classify the population into appropriate strata, especially when the population is heterogeneous or complex.
- It can introduce bias and error if the strata are not mutually exclusive or exhaustive, or if the sampling method within each stratum is not random.
- It can reduce the efficiency and power of the sample if the strata are too many or too similar, or if the sample size for each stratum is too small or too large.



### Markov chain Monte Carlo (MCMC) for the notes of the Unit 3 - Pseudo-Random Numbers in the subject of MATHEMATICAL FOUNDATION AI , ML AND DATA SCIENCE

- Markov chain Monte Carlo (MCMC) methods are a class of algorithms for sampling from a probability distribution.
- MCMC methods construct a Markov chain that has the desired distribution as its equilibrium or stationary distribution.
- A Markov chain is a sequence of random variables where the next state depends only on the current state and not on the previous states.
- The equilibrium or stationary distribution of a Markov chain is the probability distribution that remains unchanged in the long run as the chain is run.
- MCMC methods can be used to evaluate integrals, expected values, variances, and other quantities of interest over a continuous random variable, by generating samples from that variable .
- MCMC methods can also be used to explore the posterior distribution of Bayesian models, by generating samples from the posterior distribution given the data and the prior distribution .
- The main challenge of MCMC methods is to design a Markov chain that converges quickly and efficiently to the desired distribution, and to assess the quality and accuracy of the samples .
- The two most common approaches to MCMC sampling are Gibbs sampling and the Metropolis-Hastings algorithm .
- Gibbs sampling is a special case of the Metropolis-Hastings algorithm, where the acceptance probability of a new state is always one .
- Gibbs sampling works by updating one component of the state vector at a time, conditional on the rest of the components .
- The Metropolis-Hastings algorithm works by proposing a new state from a proposal distribution, and accepting or rejecting it based on a ratio of the target and proposal densities .
- The Metropolis-Hastings algorithm can handle more general proposal distributions than Gibbs sampling, but it may require more tuning and calibration .
- Both Gibbs sampling and the Metropolis-Hastings algorithm are examples of random-walk MCMC methods, where the next state is a perturbation of the current state.
- Other types of MCMC methods include Hamiltonian Monte Carlo, slice sampling, reversible jump MCMC, and sequential Monte Carlo .
- These methods aim to improve the efficiency, robustness, and scalability of MCMC sampling, by exploiting the structure, geometry, or dynamics of the target distribution .



### Markov Chains

- A Markov chain is a mathematical system that experiences transitions from one state to another according to certain probabilistic rules.
- The defining characteristic of a Markov chain is that no matter how the process arrived at its present state, the possible future states are fixed. This is known as the **Markov property**.
- A Markov chain can be represented by a **transition matrix**, which gives the probabilities of moving from one state to another .
- A Markov chain can also be represented by a **directed graph**, where the nodes are the states and the edges are labeled with the transition probabilities .
- A Markov chain is one example of a Markov model, but other examples exist, such as the **hidden Markov model**, which is a Markov chain for which the state is not directly observable.
- Markov chains are quite common, intuitive, and have been used in multiple domains like automating content creation, text generation, finance modeling, cruise control systems, etc.

#### Examples of Markov Chains

- One simple and often used example of a Markov chain is the board game “Chutes and Ladders”. The state of the game is the position of the player on the board, and the transition probabilities are determined by the dice roll and the presence of chutes or ladders. The game has a finite number of states and the Markov property holds, since the future state depends only on the current state and not on the past moves.
- Another example of a Markov chain is the weather prediction. The state of the weather can be categorized into discrete categories, such as sunny, cloudy, rainy, etc. The transition probabilities can be estimated from historical data or meteorological models. The weather prediction has the Markov property, since the future weather depends only on the current weather and not on the previous days.
- A third example of a Markov chain is the eating habits of a person who eats only fruits, vegetables, or meat. The state of the person's diet can be represented by one of the three categories, and the transition probabilities can be based on the person's preferences or health goals. The eating habits have the Markov property, since the future diet depends only on the current diet and not on the previous meals.



### Metropolis-Hastings algorithm

- The Metropolis-Hastings algorithm is a Markov chain Monte Carlo (MCMC) method for obtaining a sequence of random samples from a probability distribution from which direct sampling is difficult .
- The algorithm works by generating a sequence of sample values in such a way that, as more and more sample values are produced, the distribution of values more closely approximates the desired distribution.
- The algorithm involves designing a Markov process that fulfills two conditions: 
  - The Markov process is irreducible, meaning that any state can be reached from any other state in a finite number of steps.
  - The Markov process is aperiodic, meaning that the states are not visited in a regular pattern.
- The stationary distribution of the Markov process is chosen to be the desired distribution .
- The algorithm consists of the following steps:
  - Choose an initial value for the state variable x.
  - Repeat the following steps until a sufficient number of samples are obtained:
    - Generate a candidate value x' from a proposal distribution q(x'|x), which depends on the current value of x.
    - Compute the acceptance ratio r = p(x')q(x|x') / (p(x)q(x'|x)), where p(x) is the desired distribution.
    - Generate a uniform random number u from [0,1].
    - If u < r, accept the candidate value and set x = x'. Otherwise, reject the candidate value and keep x unchanged.
    - Record the value of x as a sample from the desired distribution.



### Gibbs sampling

- Gibbs sampling is a Markov chain Monte Carlo (MCMC) algorithm for obtaining a sequence of observations which are approximated from a specified multivariate probability distribution, when direct sampling is difficult.
- Gibbs sampling is based on the idea of sampling from the conditional distributions of each variable given the current values of the other variables.
- Gibbs sampling can be used as a means of statistical inference, especially Bayesian inference, when the posterior distribution is too complex to sample from directly or to compute analytically .
- Gibbs sampling consists of the following steps:
  - Choose initial values for each variable in the multivariate distribution.
  - For each iteration, do the following for each variable:
    - Fix the current values of the other variables.
    - Sample a new value for the variable from its conditional distribution given the current values of the other variables.
    - Update the value of the variable with the sampled value.
  - Repeat the iterations until convergence or a desired number of samples is obtained.
- Gibbs sampling has some advantages and disadvantages:
  - Advantages:
    - It is easy to implement and does not require tuning parameters or proposal distributions like some other MCMC methods.
    - It can handle high-dimensional problems and complex dependencies among variables.
    - It can be combined with other MCMC methods to improve efficiency and flexibility.
  - Disadvantages:
    - It can be slow to converge and sensitive to the initial values and the order of updating the variables.
    - It can suffer from poor mixing and correlation among the samples, especially when the conditional distributions are highly skewed or multimodal.
    - It can be difficult to assess the convergence and the quality of the samples.



### Convergence for the notes of the Unit 3 - Pseudo-Random Numbers in the subject of MATHEMATICAL FOUNDATION AI, ML AND DATA SCIENCE

- Pseudo-random numbers are numbers that are generated by a deterministic algorithm that simulates a random process. They are not truly random, but they can pass some statistical tests of randomness.
- A common pseudo-random number generation technique is called the linear congruential method. The pseudo-random numbers are generated using the following equation:

  `X_n+1 = (aX_n + c) mod m`

  where,

  - `X_n` is the previous pseudo-random number
  - `a` is a constant multiplier
  - `c` is a constant increment
  - `m` is a constant modulus
  - `X_0` is the initial value of the sequence, known as the seed

- The choice of `a`, `c`, `m`, and `X_0` affects the quality and the period of the pseudo-random sequence. The period is the number of pseudo-random numbers generated before the sequence repeats. Ideally, the period should be equal to `m`.
- Convergence is a property of a sequence of numbers that measures how close the sequence gets to a certain value as the number of terms increases. For example, the sequence `1, 1/2, 1/3, 1/4, ...` converges to zero as the number of terms increases.
- Convergence is important for pseudo-random numbers because it affects the accuracy and the efficiency of the algorithms that use them. For example, some algorithms use pseudo-random numbers to approximate the value of an integral or a probability. The convergence rate of these algorithms depends on how well the pseudo-random numbers approximate the true randomness of the problem.
- One way to measure the convergence of pseudo-random numbers is to use the discrepancy, which is the difference between the empirical distribution of the pseudo-random numbers and the uniform distribution. The smaller the discrepancy, the better the pseudo-random numbers approximate the uniform distribution, and the faster the convergence of the algorithms that use them.
- Another way to measure the convergence of pseudo-random numbers is to use the variance, which is the average squared deviation of the pseudo-random numbers from their mean. The smaller the variance, the more concentrated the pseudo-random numbers are around their mean, and the less noise they introduce in the algorithms that use them.
- Quasi-random numbers are numbers that are generated by a deterministic algorithm that tries to minimize the discrepancy and the variance of the pseudo-random numbers. They are more uniform and less random than pseudo-random numbers, and they can speed up the convergence of some algorithms, but they may not pass some randomness tests.



## Unit 4 - Vector Spaces

- A vector space is a set of objects called vectors, which can be added together and multiplied by scalars, satisfying certain axioms.
- A scalar is a real or complex number that can be used to scale a vector, i.e. change its magnitude or direction.
- The axioms of a vector space are:
  - Closure under addition: For any two vectors u and v in the vector space, u + v is also in the vector space.
  - Closure under scalar multiplication: For any scalar c and any vector u in the vector space, c * u is also in the vector space.
  - Commutativity of addition: For any two vectors u and v in the vector space, u + v = v + u.
  - Associativity of addition: For any three vectors u, v and w in the vector space, (u + v) + w = u + (v + w).
  - Additive identity: There exists a vector 0 in the vector space such that for any vector u, u + 0 = u.
  - Additive inverse: For any vector u in the vector space, there exists a vector -u such that u + (-u) = 0.
  - Distributivity of scalar multiplication over vector addition: For any scalar c and any two vectors u and v in the vector space, c * (u + v) = (c * u) + (c * v).
  - Distributivity of vector addition over scalar multiplication: For any two scalars a and b and any vector u in the vector space, (a + b) * u = (a * u) + (b * u).
  - Multiplicative identity: There exists a scalar 1 such that for any vector u, 1 * u = u.
- Examples of vector spaces are:
  - The set of all n-tuples of real or complex numbers, denoted by R^n or C^n, with the usual operations of component-wise addition and scalar multiplication.
  - The set of all polynomials of degree less than or equal to n, denoted by P_n, with the usual operations of polynomial addition and scalar multiplication.
  - The set of all continuous functions on a given interval, denoted by C[a, b], with the usual operations of function addition and scalar multiplication.
  - The set of all matrices of a given size, denoted by M_mn, with the usual operations of matrix addition and scalar multiplication.
- A subspace of a vector space is a subset of the vector space that is itself a vector space under the same operations.
- A subspace must satisfy three conditions:
  - It must contain the zero vector of the original vector space.
  - It must be closed under vector addition, i.e. if u and v are in the subspace, then u + v is also in the subspace.
  - It must be closed under scalar multiplication, i.e. if u is in the subspace and c is any scalar, then c * u is also in the subspace.
- Examples of subspaces are:
  - The set of all vectors in R^n that have the first component equal to zero, denoted by W = {(0, x_2, ..., x_n) | x_2, ..., x_n are real numbers}.
  - The set of all polynomials of degree less than or equal to n that have no constant term, denoted by U = {a_n x^n + ... + a_1 x | a_n, ..., a_1 are real or complex numbers}.
  - The set of all continuous functions on [a, b] that have zero integral, denoted by V = {f(x) | f is continuous on [a, b] and ∫_a^b f(x) dx = 0}.
  - The set of all symmetric matrices of size n x n, denoted by S = {A | A is a n x n matrix and A^T = A}.
- A linear combination of a set of vectors {v_1, v_2, ..., v_k} in a vector space is a vector of the form c_1 v_1 + c_2 v_2 + ... + c_k v_k, where c_1, c_2, ..., c_k are scalars.
- A span of a set of vectors {v_1, v_2, ..., v_k} in a vector space is the set of all linear combinations of those vectors, denoted by span{v_1, v_2, ..., v_k}.
- A span of a set of vectors is always a subspace of the vector space that contains the vectors.



### Vector Space

A vector space is a set of objects called vectors that can be added together and multiplied by numbers called scalars. The scalars are usually real numbers, but they can also be complex numbers or other fields. A vector space must satisfy certain properties or axioms that make the operations of addition and scalar multiplication well-defined and consistent. Some of the properties of a vector space are:

- **Closure under addition**: For any two vectors u and v in the vector space, their sum u + v is also in the vector space.
- **Closure under scalar multiplication**: For any vector u in the vector space and any scalar c, the product cu is also in the vector space.
- **Commutativity of addition**: For any two vectors u and v in the vector space, u + v = v + u.
- **Associativity of addition**: For any three vectors u, v and w in the vector space, (u + v) + w = u + (v + w).
- **Additive identity**: There exists a vector 0 in the vector space such that for any vector u, u + 0 = u.
- **Additive inverse**: For any vector u in the vector space, there exists a vector -u such that u + (-u) = 0.
- **Distributivity of scalar multiplication over vector addition**: For any two vectors u and v in the vector space and any scalar c, c(u + v) = cu + cv.
- **Distributivity of vector addition over scalar multiplication**: For any two scalars c and d and any vector u in the vector space, (c + d)u = cu + du.
- **Associativity of scalar multiplication**: For any two scalars c and d and any vector u in the vector space, (cd)u = c(du).
- **Multiplicative identity**: There exists a scalar 1 such that for any vector u in the vector space, 1u = u.

A vector space is characterized by its dimension, which is the number of independent directions in the space. For example, the set of all real numbers is a vector space of dimension 1, the set of all ordered pairs of real numbers is a vector space of dimension 2, and the set of all functions from a set to a field is a vector space of infinite dimension. Two vector spaces with the same dimension have the same vector-space structure, meaning that they are isomorphic or equivalent.



### Subspace

- A subspace is a subset of a vector space that is itself a vector space under the same operations of addition and scalar multiplication.
- A subspace must satisfy three conditions:
  - It must contain the zero vector.
  - It must be closed under scalar multiplication, meaning that if **v** is in the subspace and **c** is any scalar, then **c** **v** is also in the subspace.
  - It must be closed under addition, meaning that if **u** and **v** are in the subspace, then **u** + **v** is also in the subspace.
- Examples of subspaces are :
  - The trivial subspace, which is the set containing only the zero vector.
  - The entire vector space, which is a subspace of itself.
  - Any line passing through the origin in R^2 or R^3.
  - Any plane passing through the origin in R^3.
  - The set of all solutions to a homogeneous system of linear equations.
  - The span of a set of vectors, which is the set of all linear combinations of those vectors.
  - The null space of a matrix, which is the set of all vectors that are mapped to the zero vector by the matrix.
  - The column space of a matrix, which is the span of the columns of the matrix.
  - The row space of a matrix, which is the span of the rows of the matrix.



### Linear Combination

- A linear combination is a mathematical expression that is formed by adding or subtracting multiples of some terms .
- The terms can be variables, vectors, matrices, functions, or any other objects that can be multiplied by a constant and added together .
- The constants that multiply the terms are called coefficients or scalars .
- A linear combination can be written in the form c1v1 + c2v2 + ... + cnvn, where c1, c2, ..., cn are the coefficients and v1, v2, ..., vn are the terms .
- A linear combination can be used to represent a vector as a sum of other vectors, or to solve a system of linear equations by finding the values of the coefficients that make the linear combination equal to a given vector.



### Linear Independence

- A set of vectors is said to be **linearly independent** if none of the vectors can be written as a linear combination of the others.
- In other words, a set of vectors is linearly independent if the only solution to the equation `c1v1 + c2v2 + ... + cnvn = 0` is `c1 = c2 = ... = cn = 0`, where `c1, c2, ..., cn` are scalars and `v1, v2, ..., vn` are vectors.
- A set of vectors is **linearly dependent** if it is not linearly independent, i.e., if there exists a non-trivial solution to the equation `c1v1 + c2v2 + ... + cnvn = 0`.
- Linear independence is a property of a set of vectors, not of a single vector. A single vector is linearly independent if and only if it is non-zero.
- Some examples of linearly independent and dependent sets of vectors are:

  - The set `{(1, 0), (0, 1)}` is linearly independent, because the only way to write `(1, 0)` as a linear combination of `(0, 1)` is to use zero coefficients, and vice versa.
  - The set `{(1, 2), (2, 4)}` is linearly dependent, because `(2, 4) = 2(1, 2)`, so there is a non-zero coefficient that makes the linear combination equal to zero.
  - The set `{(1, 0, 0), (0, 1, 0), (0, 0, 1)}` is linearly independent, because the only way to write any of these vectors as a linear combination of the others is to use zero coefficients.
  - The set `{(1, 0, 0), (0, 1, 0), (1, 1, 0)}` is linearly dependent, because `(1, 1, 0) = (1, 0, 0) + (0, 1, 0)`, so there are non-zero coefficients that make the linear combination equal to zero.

- Linear independence is related to the concepts of **span**, **basis**, and **dimension** of a vector space, which will be discussed in the next sections.



### Basis for the notes of the Unit 4 - Vector Spaces in the subject of MATHEMATICAL FOUNDATION AI , ML AND DATA SCIENCE

- A vector space is a set of objects called vectors that can be added and multiplied by scalars (usually real or complex numbers) according to certain rules called axioms .
- A vector space is also called a linear space because the operations of vector addition and scalar multiplication are linear, meaning they satisfy the properties of distributivity, commutativity, associativity, and identity .
- A vector space can be thought of as a collection of arrows with a common origin, called the zero vector, where each arrow has a length and a direction .
- A vector space can also be thought of as a coordinate system, where each vector is represented by a list of numbers, called coordinates, that specify its position relative to a fixed basis .
- The dimension of a vector space is the number of linearly independent vectors in a basis, or equivalently, the number of coordinates needed to specify any vector in the space .
- The most familiar example of a vector space is the Euclidean space mathbb {R}^n Rn, where vectors are n n -tuples of real numbers, and the operations of vector addition and scalar multiplication are performed componentwise .
- Other examples of vector spaces include the space of polynomials of degree less than or equal to n, the space of matrices of a given size, the space of functions of a certain type, and the space of solutions of a linear differential equation .
- Vector spaces are important in mathematics because they allow us to abstract the concepts of geometry and algebra and apply them to various fields of study, such as physics, engineering, computer science, and data science .



### Dimension of a Vector Space

- A vector space is a set of objects called vectors that can be added and multiplied by scalars (numbers) according to certain rules.
- A basis of a vector space is a set of linearly independent vectors that span the whole space, meaning that every vector in the space can be written as a linear combination of the basis vectors .
- The dimension of a vector space is the number of vectors in a basis of the space, and is denoted by dim(V) .
- The dimension of a vector space is a measure of how many degrees of freedom are available to choose a vector in the space.
- The dimension of a vector space is unique, meaning that any two bases of the same space have the same number of vectors.
- Some examples of dimensions of vector spaces are:
  - The dimension of the trivial vector space {0} is 0, since the only basis is the empty set.
  - The dimension of the real vector space R^n is n, since a basis is the set of n standard unit vectors e_1, e_2, ..., e_n.
  - The dimension of the vector space of polynomials in x with real coefficients having degree at most 2 is 3, since a basis is the set {1, x, x^2} .
  - The dimension of the vector space of 2x2 matrices with real entries is 4, since a basis is the set of four matrices with one 1 and three 0s in each position.



### Finding a Basis of a Vector Space

- A basis of a vector space is a set of linearly independent vectors that span the whole space.
- A basis is not unique, but any two bases of the same vector space have the same number of elements, called the dimension of the space.
- To find a basis of a vector space, one can use the following methods:
  - If the vector space is given as the span of a set of vectors, then one can apply the Gaussian elimination algorithm to the matrix formed by the vectors as columns, and select the pivot columns as a basis.
  - If the vector space is given as the null space of a matrix, then one can apply the reduced row echelon form algorithm to the matrix, and write the general solution of the homogeneous system as a linear combination of free variables, and select the coefficients of the free variables as a basis.
  - If the vector space is given as the column space of a matrix, then one can apply the reduced row echelon form algorithm to the matrix, and select the pivot columns of the original matrix as a basis.
  - If the vector space is given as the row space of a matrix, then one can apply the reduced row echelon form algorithm to the matrix, and select the non-zero rows of the reduced matrix as a basis.



### Coordinates for the notes of the Unit 4 - Vector Spaces in the subject of MATHEMATICAL FOUNDATION AI , ML AND DATA SCIENCE

- A **vector space** is a set of objects called **vectors** that can be added and multiplied by **scalars** (numbers) according to certain rules.
- A **coordinate vector** is a representation of a vector in terms of a **basis**, which is an ordered set of linearly independent vectors that span the vector space.
- A **real coordinate space** is a vector space whose scalars and vectors are real numbers and n-tuples of real numbers, respectively.
- A **complex coordinate space** is a vector space whose scalars and vectors are complex numbers and n-tuples of complex numbers, respectively.
- A **Euclidean space** is a vector space with an inner product, which is a function that assigns a real number to each pair of vectors, satisfying certain properties.
- The **Cartesian coordinates** of a point in a Euclidean space are the coefficients of the linear combination of the standard basis vectors that equals the point.
- The **dimension** of a vector space is the number of vectors in any basis of the vector space.
- A **subspace** of a vector space is a subset of the vector space that is itself a vector space under the same operations.
- A **linear transformation** is a function between two vector spaces that preserves the operations of vector addition and scalar multiplication.
- A **matrix** is a rectangular array of numbers that can represent a linear transformation by multiplying coordinate vectors.
- A **system of linear equations** is a set of equations that can be written in matrix form as Ax = b, where A is a matrix, x is a coordinate vector of unknowns, and b is a coordinate vector of constants.

: Vector space - Wikipedia
: Coordinate vector - Wikipedia
: Real coordinate space - Wikipedia
: Vector space - Wikipedia



### Change of Basis

- A **basis** of a vector space is a set of linearly independent vectors that span the whole space.
- A vector can be expressed as a linear combination of the basis vectors using **coordinates** or **components**.
- A vector can have different coordinates depending on the choice of basis.
- A **change of basis** is a technique to rewrite vectors in terms of a different set of basis vectors.
- A change of basis can be viewed as a type of linear transformation that maps one basis to another.
- A change of basis can be useful for many types of matrix computations in linear algebra, such as simplifying, diagonalizing, or finding eigenvalues and eigenvectors of matrices.
- A change of basis can be performed by using a **change of basis matrix**, which is a matrix that relates the coordinates of a vector in one basis to the coordinates of the same vector in another basis.
- A change of basis matrix can be found by writing the new basis vectors as linear combinations of the old basis vectors, and then arranging the coefficients as columns of the matrix.
- A change of basis matrix can also be found by taking the inverse of the matrix that has the new basis vectors as columns.
- A change of basis matrix can be used to transform a vector from one basis to another by multiplying the vector by the matrix.
- A change of basis matrix can also be used to transform a linear transformation from one basis to another by multiplying the matrix of the linear transformation by the change of basis matrices on both sides.
- A change of basis matrix is always invertible, and its inverse is the change of basis matrix from the new basis to the old basis.



### Inner Product Spaces

- An inner product space is a vector space V over a field F (usually R or C) with an operation called an inner product, which is a function that assigns a scalar to every pair of vectors in V.
- The inner product of two vectors u and v in V is denoted by <u,v> or (u,v) and must satisfy the following properties for all u, v, w in V and all c in F :
  - Conjugate symmetry: <u,v> = <v,u>*
  - Linearity in the first argument: <cu + w, v> = c<u,v> + <w,v>
  - Positive-definiteness: <u,u> ≥ 0 and <u,u> = 0 if and only if u = 0
  - Here, <v,u>* denotes the complex conjugate of <v,u>, which is equal to <v,u> if F is R and is obtained by changing the sign of the imaginary part of <v,u> if F is C.
- An inner product space is also a normed linear space, which means that we can define a norm (or a length) of a vector u in V by ||u|| = √<u,u> and use it to measure the distance between two vectors by d(u,v) = ||u - v||.
- Some examples of inner product spaces are:
  - R^n with the standard dot product: <u,v> = u1v1 + u2v2 + ... + unvn
  - C^n with the Hermitian dot product: <u,v> = u1v1* + u2v2* + ... + unvn*
  - The space of continuous functions on a closed interval [a,b] with the inner product: <f,g> = ∫ab f(x)g(x) dx
  - The space of square-integrable functions on a domain D with the inner product: <f,g> = ∫D f(x)g(x)* dx
- An inner product space allows us to generalize the concepts of angle, orthogonality, projection, and ortho-normal basis to any vector space with an inner product.
  - The angle θ between two nonzero vectors u and v in V is defined by cos θ = <u,v> / (||u|| ||v||)
  - Two vectors u and v in V are orthogonal if <u,v> = 0
  - The projection of a vector u onto a nonzero vector v in V is given by projv u = (<u,v> / <v,v>) v
  - An ortho-normal basis of V is a basis {v1, v2, ..., vn} such that <vi, vj> = 0 if i ≠ j and <vi, vi> = 1 for all i and j
- An inner product space is a special case of a more general concept called a Hilbert space, which is an inner product space that is also complete, meaning that every Cauchy sequence in the space converges to a limit in the space.



### Inner Product

- An inner product is a way to multiply two vectors in a vector space and get a scalar as the result   .
- An inner product is a generalization of the dot product, which is the standard inner product in Euclidean vector spaces   .
- An inner product must satisfy four properties for any vectors u, v, w and any scalar c in the vector space   :
  - Linearity: <u + v, w> = <u, w> + <v, w> and <cu, v> = c<u, v>
  - Symmetry: <u, v> = <v, u>
  - Positivity: <u, u> ≥ 0 and <u, u> = 0 if and only if u = 0
  - Conjugate symmetry: <u, v> = <v, u>*
- An inner product space is a vector space with an inner product defined on it   .
- An inner product space allows us to define geometric concepts such as length, angle, orthogonality, projection, and distance of vectors   .
- The length or norm of a vector u is defined as ||u|| = √<u, u>   .
- The angle θ between two nonzero vectors u and v is defined as cos θ = <u, v> / (||u|| ||v||)   .
- Two vectors u and v are orthogonal if <u, v> = 0   .
- The projection of a vector u onto a nonzero vector v is defined as proj<sub>v</sub> u = (<u, v> / <v, v>) v   .
- The distance between two vectors u and v is defined as d(u, v) = ||u - v||   .



### Length for the notes of the Unit 4 - Vector Spaces in the subject of MATHEMATICAL FOUNDATION AI, ML AND DATA SCIENCE

- The length of the notes for the Unit 4 - Vector Spaces should be concise and comprehensive, covering the main concepts and definitions, theorems and proofs, examples and applications, and exercises and problems.
- The length of the notes should also be appropriate for the level of difficulty and depth of the unit, as well as the time and resources available for studying and revising the unit.
- A possible guideline for the length of the notes is as follows:

  - Introduction: 1-2 pages, summarizing the objectives, scope, and motivation of the unit, and providing an overview of the topics and subtopics covered in the unit.
  - Vector Spaces: 3-4 pages, defining the concept of a vector space, its properties and axioms, and giving examples of vector spaces in different fields and contexts.
  - Subspaces: 2-3 pages, explaining the notion of a subspace of a vector space, its properties and criteria, and giving examples of subspaces and their bases and dimensions.
  - Linear Independence and Dependence: 2-3 pages, introducing the concepts of linear independence and dependence of vectors, their properties and implications, and giving examples of linearly independent and dependent sets of vectors and their relations to subspaces and bases.
  - Spanning Sets and Bases: 3-4 pages, defining the concepts of a spanning set and a basis of a vector space or a subspace, their properties and uniqueness, and giving examples of spanning sets and bases and their applications to coordinate systems and linear transformations.
  - Dimension: 2-3 pages, defining the concept of the dimension of a vector space or a subspace, its properties and invariance, and giving examples of dimensions and their applications to rank and nullity of matrices and linear transformations.
  - Summary and Review: 1-2 pages, highlighting the main points and results of the unit, and providing a list of key terms and formulas, as well as some review questions and exercises to test the understanding and mastery of the unit.

- Therefore, the total length of the notes for the Unit 4 - Vector Spaces could be around 16-24 pages, depending on the font size, spacing, and formatting of the notes, as well as the level of detail and rigor of the explanations and proofs.



### Orthogonal Vectors

- Orthogonal vectors are vectors that are perpendicular to each other, i.e., they form a right angle or their dot product is zero   .
- For example, the standard basis vectors **i**, **j**, and **k** in three-dimensional space are orthogonal to each other, since **i** · **j** = **j** · **k** = **k** · **i** = 0.
- Some properties of orthogonal vectors are:
  - The zero vector is orthogonal to every vector.
  - The cross product of two orthogonal vectors is a vector that is orthogonal to both of them.
  - The length of the projection of a vector onto an orthogonal vector is zero.
  - The Pythagorean theorem holds for orthogonal vectors, i.e., if **u** and **v** are orthogonal, then |**u** + **v**|² = |**u**|² + |**v**|².
  - A set of vectors is called mutually orthogonal if every pair of vectors in the set is orthogonal.
  - A set of mutually orthogonal vectors that are also unit vectors (i.e., have length one) is called an orthonormal set or basis.



### Triangle Inequality

- The triangle inequality is a property of vectors that states that the norm (or length) of the sum of two vectors is less than or equal to the sum of their norms. Mathematically, for any two vectors **u** and **v** in a vector space, we have:

  $$\| \mathbf{u} + \mathbf{v} \| \leq \| \mathbf{u} \| + \| \mathbf{v} \|$$

- The triangle inequality can be understood geometrically by considering the vectors **u** and **v** as two sides of a triangle, and the vector **u** + **v** as the third side. The length of the third side is always less than or equal to the sum of the lengths of the other two sides, as shown in the figure below:

  Triangle Inequality

- The triangle inequality can be proved using the Cauchy-Schwarz inequality, which states that for any two vectors **u** and **v** in an inner product space, we have:

  $$| \langle \mathbf{u}, \mathbf{v} \rangle | \leq \| \mathbf{u} \| \| \mathbf{v} \|$$

- The proof of the triangle inequality is as follows:

  - Start with the norm of the vector **u** + **v** and square both sides:

    $$\| \mathbf{u} + \mathbf{v} \|^2 = \langle \mathbf{u} + \mathbf{v}, \mathbf{u} + \mathbf{v} \rangle$$

  - Use the properties of the inner product to expand the right-hand side:

    $$\| \mathbf{u} + \mathbf{v} \|^2 = \langle \mathbf{u}, \mathbf{u} \rangle + \langle \mathbf{u}, \mathbf{v} \rangle + \langle \mathbf{v}, \mathbf{u} \rangle + \langle \mathbf{v}, \mathbf{v} \rangle$$

  - Use the fact that the inner product is symmetric and real-valued to simplify the right-hand side:

    $$\| \mathbf{u} + \mathbf{v} \|^2 = \| \mathbf{u} \|^2 + 2 \langle \mathbf{u}, \mathbf{v} \rangle + \| \mathbf{v} \|^2$$

  - Apply the Cauchy-Schwarz inequality to the inner product term:

    $$\| \mathbf{u} + \mathbf{v} \|^2 \leq \| \mathbf{u} \|^2 + 2 \| \mathbf{u} \| \| \mathbf{v} \| + \| \mathbf{v} \|^2$$

  - Factor the right-hand side using the formula for the square of a sum:

    $$\| \mathbf{u} + \mathbf{v} \|^2 \leq (\| \mathbf{u} \| + \| \mathbf{v} \|)^2$$

  - Take the square root of both sides and obtain the triangle inequality:

    $$\| \mathbf{u} + \mathbf{v} \| \leq \| \mathbf{u} \| + \| \mathbf{v} \|$$

- The triangle inequality is useful for many applications in mathematics, such as measuring distances, angles, and norms of vectors and matrices. It is also a fundamental property of metric spaces, which are abstract spaces where distances between points are defined.



### Cauchy-Schwarz Inequality

- The Cauchy-Schwarz inequality is one of the most important and widely used inequalities in mathematics. It relates the inner product of two vectors to their norms, and can be applied to various fields such as geometry, analysis, probability, and linear algebra.
- The inequality states that for any two vectors **x** and **y** in an inner product space, it is true that

  $$|\langle x, y \rangle| \leq \|x\| \|y\|$$

  where $\langle x, y \rangle$ is the inner product of **x** and **y**, and $\|x\|$ and $\|y\|$ are their norms, defined as

  $$\|x\| = \sqrt{\langle x, x \rangle}$$

  $$\|y\| = \sqrt{\langle y, y \rangle}$$

- The equality holds if and only if **x** and **y** are linearly dependent, that is, one of them is a scalar multiple of the other.
- The inequality can be proved by using the fact that the inner product is bilinear, symmetric, and positive definite, and by considering the following expression for any scalar $\lambda$:

  $$\langle x - \lambda y, x - \lambda y \rangle \geq 0$$

  Expanding and simplifying, we get

  $$\lambda^2 \|y\|^2 - 2 \lambda \langle x, y \rangle + \|x\|^2 \geq 0$$

  This is a quadratic equation in $\lambda$, and it has at most one real root, since its discriminant is

  $$\Delta = 4 \langle x, y \rangle^2 - 4 \|x\|^2 \|y\|^2$$

  To ensure that $\Delta \leq 0$, we must have

  $$\langle x, y \rangle^2 \leq \|x\|^2 \|y\|^2$$

  Taking the square root of both sides, we obtain the Cauchy-Schwarz inequality.
- The inequality can be generalized to other settings, such as sums, integrals, and matrices. For example, if **a** and **b** are two vectors in $\mathbb{R}^n$, then

  $$\left| \sum_{i=1}^n a_i b_i \right| \leq \sqrt{\sum_{i=1}^n a_i^2} \sqrt{\sum_{i=1}^n b_i^2}$$

  where the inner product is defined as

  $$\langle a, b \rangle = \sum_{i=1}^n a_i b_i$$

  and the norm is defined as

  $$\|a\| = \sqrt{\langle a, a \rangle}$$

  This is a special case of the more general Hölder's inequality, which applies to any positive exponents $p$ and $q$ such that $\frac{1}{p} + \frac{1}{q} = 1$.



### Orthonormal (Orthogonal) Basis

- A set of vectors $\{v_1, v_2, ..., v_n\}$ in a vector space $V$ is called an **orthogonal basis** if the vectors are linearly independent and pairwise orthogonal, i.e., $v_i \cdot v_j = 0$ for $i \neq j$.
- An orthogonal basis has the property that the length of any vector $v \in V$ can be computed as $\|v\| = \sqrt{(v \cdot v_1)^2 + (v \cdot v_2)^2 + ... + (v \cdot v_n)^2}$.
- An orthogonal basis can be normalized by dividing each vector by its length, resulting in an **orthonormal basis**, i.e., a set of vectors $\{u_1, u_2, ..., u_n\}$ such that $u_i \cdot u_j = \delta_{ij}$, where $\delta_{ij}$ is the Kronecker delta function, which is $1$ if $i = j$ and $0$ otherwise.
- An orthonormal basis has the property that the coordinates of any vector $v \in V$ with respect to the basis are given by $v = (v \cdot u_1)u_1 + (v \cdot u_2)u_2 + ... + (v \cdot u_n)u_n$.
- An orthonormal basis is also called an **orthogonal coordinate system** or an **orthogonal frame**.
- An orthonormal basis is useful for simplifying calculations involving inner products, norms, angles, and projections of vectors.
- An example of an orthonormal basis in $\mathbb{R}^2$ is $\{(1, 0), (0, 1)\}$, which is also the standard basis. An example of an orthonormal basis in $\mathbb{R}^3$ is $\{(1, 0, 0), (0, 1, 0), (0, 0, 1)\}$, which is also the standard basis. An example of an orthonormal basis that is not the standard basis is $\{(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0), (-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0), (0, 0, 1)\}$, which is obtained by rotating the standard basis by $45$ degrees around the $z$-axis.
- Any vector space with an inner product has an orthonormal basis, which can be constructed by applying the **Gram-Schmidt process** to any linearly independent set of vectors. The Gram-Schmidt process is an algorithm that takes a set of vectors $\{v_1, v_2, ..., v_n\}$ and produces an orthonormal set of vectors $\{u_1, u_2, ..., u_n\}$ such that the span of $\{v_1, ..., v_k\}$ is equal to the span of $\{u_1, ..., u_k\}$ for any $k \leq n$. The algorithm works as follows:

  - Set $u_1 = \frac{v_1}{\|v_1\|}$.
  - For $k = 2, 3, ..., n$, do the following:
    - Let $w_k = v_k - (v_k \cdot u_1)u_1 - (v_k \cdot u_2)u_2 - ... - (v_k \cdot u_{k-1})u_{k-1}$, which is the projection of $v_k$ onto the orthogonal complement of the span of $\{u_1, ..., u_{k-1}\}$.
    - Set $u_k = \frac{w_k}{\|w_k\|}$.
  - Return $\{u_1, u_2, ..., u_n\}$.

- An example of applying the Gram-Schmidt process to find an orthonormal basis for $\mathbb{R}^3$ is as follows:

  - Let $\{v_1, v_2, v_3\} = \{(1, 1, 1), (1, 0, 1), (0, 1, 0)\}$.
  - Set $u_1 = \frac{v_1}{\|v_1\|} = \frac{(1, 1, 1)}{\sqrt{



### Gram-Schmidt Process

- The Gram-Schmidt process is a method for orthonormalizing a set of vectors in an inner product space, most commonly the Euclidean space R^n equipped with the standard inner product .
- Orthonormalizing means transforming the vectors into a set of mutually orthogonal unit vectors, which form an orthonormal basis for the space spanned by the original vectors.
- An orthonormal basis is a basis that has the properties of being linearly independent, orthogonal, and normalized. This means that each vector in the basis has length one, and the dot product of any two distinct vectors in the basis is zero.
- The Gram-Schmidt process can be applied to any finite set of linearly independent vectors, and it produces a unique orthonormal basis for the same space.
- The Gram-Schmidt process can be described as follows  :

  - Let u_1, u_2, ..., u_k be a set of linearly independent vectors in R^n.
  - Let v_1, v_2, ..., v_k be the orthonormal vectors obtained by the Gram-Schmidt process.
  - Step 1: Let v_1 = u_1 / ||u_1||, where ||u_1|| is the length of u_1.
  - Step 2: Let v_2 = u_2 - proj_W1 u_2, where W_1 is the space spanned by v_1, and proj_W1 u_2 is the orthogonal projection of u_2 onto W_1. Then normalize v_2 by dividing it by its length.
  - Step 3: Let v_3 = u_3 - proj_W2 u_3, where W_2 is the space spanned by v_1 and v_2, and proj_W2 u_3 is the orthogonal projection of u_3 onto W_2. Then normalize v_3 by dividing it by its length.
  - Step k: Let v_k = u_k - proj_Wk-1 u_k, where W_k-1 is the space spanned by v_1, v_2, ..., v_k-1, and proj_Wk-1 u_k is the orthogonal projection of u_k onto W_k-1. Then normalize v_k by dividing it by its length.
  - The resulting vectors v_1, v_2, ..., v_k form an orthonormal basis for the space spanned by u_1, u_2, ..., u_k.

- The Gram-Schmidt process can be stabilized by a small modification; this version is sometimes referred to as modified Gram-Schmidt or MGS. This approach gives the same result as the original formula in exact arithmetic and introduces smaller errors in finite-precision arithmetic.
- The modified Gram-Schmidt process can be described as follows:

  - Let u_1, u_2, ..., u_k be a set of linearly independent vectors in R^n.
  - Let v_1, v_2, ..., v_k be the orthonormal vectors obtained by the modified Gram-Schmidt process.
  - Step 1: Let v_1 = u_1 / ||u_1||, where ||u_1|| is the length of u_1.
  - Step 2: For i = 2, 3, ..., k, do the following:
    - Let u_i = u_i - sum_{j=1}^{i-1} <u_i, v_j> v_j, where <u_i, v_j> is the dot product of u_i and v_j, and sum_{j=1}^{i-1} <u_i, v_j> v_j is the sum of the orthogonal projections of u_i onto v_1, v_2, ..., v_i-1.
    - Let v_i = u_i / ||u_i||, where ||u_i|| is the length of u_i.
  - The resulting vectors v_1, v_2, ..., v_k form an orthonormal basis for the space spanned by u_1, u_2, ..., u_k.

- The Gram-Schmidt process and the modified Gram-Schmidt process are useful for finding orthonormal bases, which have many applications in linear algebra, such as simplifying calculations, solving systems of linear equations, diagonalizing matrices, performing orthogonal transformations



## Unit 5 - Linear Transformations

- A linear transformation is a function that maps vectors from one vector space to another vector space, preserving the operations of vector addition and scalar multiplication.
- A linear transformation can be represented by a matrix, which encodes the effect of the transformation on the standard basis vectors of the domain and the range.
- The standard matrix of a linear transformation T is denoted by [T] and is defined by [T] = [[T(e1)] [T(e2)] ... [T(en)]], where e1, e2, ..., en are the standard basis vectors of the domain.
- The matrix-vector product [T]x can be interpreted as applying the linear transformation T to the vector x, or as taking a linear combination of the columns of [T] with the coefficients from x.
- The domain of a linear transformation T is the set of all vectors that can be input to T, and the range of T is the set of all possible outputs of T.
- The kernel (or null space) of a linear transformation T is the set of all vectors x such that T(x) = 0, and the image (or column space) of T is the span of the columns of [T].
- A linear transformation T is one-to-one if T(x) = T(y) implies x = y, or equivalently, if the kernel of T contains only the zero vector.
- A linear transformation T is onto if every vector in the range of T is the image of some vector in the domain of T, or equivalently, if the image of T is equal to the range of T.
- A linear transformation T is invertible if there exists another linear transformation S such that T(S(x)) = x and S(T(x)) = x for all x, or equivalently, if T is both one-to-one and onto.
- The inverse of a linear transformation T, denoted by T^-1, is the unique linear transformation that satisfies T(T^-1(x)) = x and T^-1(T(x)) = x for all x.
- The inverse of a linear transformation T, if it exists, can be found by solving the matrix equation [T][S] = I, where I is the identity matrix and [S] is the standard matrix of T^-1.
- A linear transformation T preserves the properties of vectors, such as length, angle, and orthogonality, if and only if [T] is an orthogonal matrix, meaning that [T]^-1 = [T]^T, where [T]^T is the transpose of [T].
- Some examples of linear transformations are rotations, reflections, projections, scaling, and shearing.



### Linear Transformations and Matrices for Linear Transformation

- A linear transformation is a function that maps vectors from one vector space to another vector space, preserving the operations of vector addition and scalar multiplication.
- A matrix is a rectangular array of numbers that can be used to represent linear transformations in a convenient and compact way.
- To find the matrix of a linear transformation, we need to choose a basis for the domain and the codomain of the function, and then compute the images of the basis vectors under the function.
- The matrix of a linear transformation is not unique, as it depends on the choice of the basis. However, different matrices of the same linear transformation are related by a change of basis matrix.
- The action of a linear transformation on a vector can be determined by multiplying the matrix of the linear transformation by the vector, using the appropriate basis.
- Matrices can also be seen as transformations of the coordinate space, where each column of the matrix represents the image of a unit vector along a coordinate axis.
- Matrices allow arbitrary linear transformations to be displayed in a consistent format, suitable for computation. This also allows transformations to be composed easily (by multiplying their matrices).



### Kernel and Range of a Linear Transformation

- A linear transformation is a function T: V -> W that preserves the operations of vector addition and scalar multiplication, i.e., T(u + v) = T(u) + T(v) and T(cu) = cT(u) for any vectors u, v in V and any scalar c.
- The kernel (or null space) of a linear transformation T: V -> W is the set of all vectors u in V such that T(u) = 0 (the zero vector in W). It is denoted by ker(T) or N(T).
- The range (or image) of a linear transformation T: V -> W is the set of all vectors w in W that can be obtained by applying T to some vector in V. It is denoted by ran(T) or Im(T).
- The kernel and the range of a linear transformation are both subspaces, i.e., they are closed under vector addition and scalar multiplication.
- The kernel and the range of a linear transformation are related to the dimension of the domain and the codomain by the rank-nullity theorem, which states that dim(V) = dim(ker(T)) + dim(ran(T)) for any linear transformation T: V -> W, where dim(V) and dim(W) are the dimensions of V and W, respectively.
- The rank of a linear transformation T: V -> W is the dimension of its range, i.e., rank(T) = dim(ran(T)).
- The nullity of a linear transformation T: V -> W is the dimension of its kernel, i.e., null(T) = dim(ker(T)).
- A linear transformation T: V -> W is one-to-one (or injective) if T(u) = T(v) implies that u = v for any vectors u, v in V. Equivalently, T is one-to-one if ker(T) = {0}, i.e., the kernel contains only the zero vector.
- A linear transformation T: V -> W is onto (or surjective) if ran(T) = W, i.e., every vector in W is in the range of T. Equivalently, T is onto if rank(T) = dim(W).
- A linear transformation T: V -> W is bijective if it is both one-to-one and onto. In this case, T has an inverse function T^-1: W -> V that satisfies T^-1(T(u)) = u for any u in V and T(T^-1(w)) = w for any w in W.
- A matrix transformation is a special type of linear transformation that maps a vector x in R^n to a vector Ax in R^m, where A is an m x n matrix. The kernel and the range of a matrix transformation are the same as the null space and the column space of the matrix A, respectively. The rank and the nullity of a matrix transformation are the same as the rank and the nullity of the matrix A, respectively.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 5 - Linear Transformations in the subject of Mathematical Foundation AI, ML and Data Science. Here are some notes on the topic of Change of Basis.

### Change of Basis

- A basis of a vector space is a set of linearly independent vectors that span the whole space.
- Any vector in the space can be written as a unique linear combination of the basis vectors.
- The coordinates of a vector with respect to a basis are the scalars that multiply the basis vectors in the linear combination.
- Different bases can be used to represent the same vector space, but the coordinates of a vector will change depending on the basis chosen.
- A change of basis is a linear transformation that maps the coordinates of a vector from one basis to another.
- To find the change of basis matrix from basis B to basis C, we can write each vector in B as a linear combination of the vectors in C, and then form a matrix with the coefficients as columns.
- The change of basis matrix from basis C to basis B is the inverse of the change of basis matrix from basis B to basis C.
- To change the coordinates of a vector from basis B to basis C, we can multiply the vector by the change of basis matrix from basis B to basis C.
- To change the coordinates of a vector from basis C to basis B, we can multiply the vector by the change of basis matrix from basis C to basis B, or by the inverse of the change of basis matrix from basis B to basis C.
- A change of basis preserves the linear relationships among vectors, such as linear independence, span, and dimension.



### Eigenvalues and Eigenvectors

- Eigenvalues and eigenvectors are concepts related to linear transformations of vector spaces.
- A linear transformation is a function that maps vectors from one vector space to another, preserving the operations of vector addition and scalar multiplication.
- A matrix is a rectangular array of numbers that can represent a linear transformation by multiplying it with a vector.
- An eigenvector of a matrix is a nonzero vector that does not change its direction when multiplied by the matrix. It may only change its length or sign.
- An eigenvalue of a matrix is a scalar that corresponds to an eigenvector. It is the factor by which the eigenvector is scaled when multiplied by the matrix.
- Geometrically, an eigenvector points in a direction that is stretched or shrunk by the matrix, and the eigenvalue is the amount of stretching or shrinking.
- Mathematically, an eigenvector **x** and an eigenvalue **λ** of a matrix **A** satisfy the equation **Ax = λx**.
- To find the eigenvalues of a matrix, we need to solve the characteristic equation **det(A - λI) = 0**, where **det** is the determinant and **I** is the identity matrix.
- To find the eigenvectors of a matrix, we need to find the null space of **A - λI** for each eigenvalue **λ**, where the null space is the set of vectors that are mapped to the zero vector by the matrix.
- Some properties of eigenvalues and eigenvectors are:
  - If **A** is a triangular matrix, then the diagonal elements of **A** are the eigenvalues of **A**.
  - If **λ** is an eigenvalue of **A** with eigenvector **x**, then **1/λ** is an eigenvalue of **A**<sup>-1</sup> with eigenvector **x**.
  - If **λ** is an eigenvalue of **A**, then **λ** is an eigenvalue of **A**<sup>T</sup>, where **T** denotes the transpose of the matrix.
  - The sum of the eigenvalues of **A** is equal to the trace of **A**, which is the sum of the diagonal elements of **A**.
  - The product of the eigenvalues of **A** is equal to the determinant of **A**.
  - The number of linearly independent eigenvectors of **A** is equal to the rank of **A**, which is the dimension of the column space of **A**.
  - If **A** has **n** distinct eigenvalues, then **A** has **n** linearly independent eigenvectors, and **A** is diagonalizable, meaning that it can be written as **A = PDP**<sup>-1</sup>, where **P** is a matrix whose columns are the eigenvectors of **A**, and **D** is a diagonal matrix whose diagonal elements are the eigenvalues of **A**.



### Definition of Eigenvalue and Eigenvector

- An **eigenvalue** of a square matrix A is a scalar λ that satisfies the equation Av = λv, where v is a non-zero vector in the same space as A.  
- An **eigenvector** of a square matrix A is a non-zero vector v that satisfies the equation Av = λv, where λ is a scalar called the eigenvalue of A corresponding to v.  
- The word eigen comes from the German word for "proper" or "characteristic". 
- Eigenvalues and eigenvectors are important concepts in linear algebra that help in analyzing the properties and behavior of linear transformations and matrices.  
- To find the eigenvalues and eigenvectors of a matrix A, one has to solve the characteristic equation det(A - λI) = 0, where I is the identity matrix of the same size as A. The roots of this equation are the eigenvalues of A, and the corresponding eigenvectors can be found by plugging in each eigenvalue into the equation (A - λI)v = 0 and solving for v.



### Diagonalization

- Diagonalization is the process of finding a diagonal matrix that is similar to a given matrix. A diagonal matrix is a matrix that has non-zero entries only on its main diagonal.
- Diagonalization is useful because diagonal matrices are easier to work with than general matrices. For example, it is easy to compute the power of a diagonal matrix, or to find its inverse.
- Diagonalization is related to the concept of eigenvalues and eigenvectors of a matrix. An eigenvalue of a matrix A is a scalar λ such that there exists a non-zero vector v satisfying Av = λv. Such a vector v is called an eigenvector of A corresponding to the eigenvalue λ.
- A matrix A is diagonalizable if and only if there exists a basis of the vector space consisting of eigenvectors of A. In other words, A is diagonalizable if and only if there are n linearly independent eigenvectors of A, where n is the dimension of the vector space.
- If A is diagonalizable, then there exists an invertible matrix P such that P^-1AP is a diagonal matrix D. The columns of P are the eigenvectors of A, and the diagonal entries of D are the eigenvalues of A. The matrix P is called the change of basis matrix, and the matrix D is called the diagonalized matrix.
- To diagonalize a matrix A, we need to follow four steps:
  - Step 1: Find the eigenvalues of A by solving the characteristic equation det(A - λI) = 0, where I is the identity matrix.
  - Step 2: For each eigenvalue λ, find the eigenvectors of A by solving the system (A - λI)v = 0.
  - Step 3: Check if there are n linearly independent eigenvectors of A. If not, then A is not diagonalizable. If yes, then form the matrix P by putting the eigenvectors as columns.
  - Step 4: Compute the matrix D by multiplying P^-1AP. The diagonal entries of D are the eigenvalues of A.



### Symmetric Matrices and Orthogonal Diagonalization

- A symmetric matrix is a square matrix that is equal to its transpose, i.e., A = A^T^.
- A symmetric matrix has real eigenvalues and orthogonal eigenvectors.
- An orthogonal matrix is a square matrix whose columns (or rows) are orthonormal, i.e., Q^T^Q = QQ^T^ = I.
- An orthogonal matrix preserves the length and angle of vectors, i.e., ||Qx|| = ||x|| and <Qx, Qy> = <x, y>.
- An orthogonal matrix has determinant 1 or -1 and inverse Q^T^.
- A matrix A is orthogonally diagonalizable if there exists an orthogonal matrix P and a diagonal matrix D such that A = PDP^T^.
- A symmetric matrix is orthogonally diagonalizable by the spectral theorem.
- To orthogonally diagonalize a symmetric matrix A, we need to find an orthonormal basis of eigenvectors of A and form the matrix P with these eigenvectors as columns. Then D is the diagonal matrix with the corresponding eigenvalues of A on the diagonal.
- Orthogonal diagonalization simplifies the computation of powers of a matrix, i.e., A^k^ = PD^k^P^T^.
- Orthogonal diagonalization also allows us to write a quadratic form as a sum of squares, i.e., x^T^Ax = y^T^Dy, where y = P^T^x and D is the diagonal matrix of eigenvalues of A.

