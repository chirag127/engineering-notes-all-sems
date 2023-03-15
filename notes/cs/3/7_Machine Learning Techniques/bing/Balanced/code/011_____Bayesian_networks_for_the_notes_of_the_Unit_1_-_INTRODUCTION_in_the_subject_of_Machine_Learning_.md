### Bayesian networks

- Bayesian networks are a type of **probabilistic graphical model** that can be used to build models from data and/or expert opinion .
- They represent a set of **variables** and their **conditional dependencies** via a **directed acyclic graph (DAG)** .
- Each node in the DAG corresponds to a **random variable** and each edge represents the **conditional probability** for the corresponding random variables .
- Bayesian networks can be used for a wide range of tasks including:
  - **Diagnostics**: finding the most likely causes of an observed effect.
  - **Reasoning**: inferring the most probable state of some variables given the evidence of others.
  - **Causal modeling**: discovering the causal relationships among variables from data or prior knowledge.
  - **Decision making under uncertainty**: choosing the best action to maximize the expected utility.
  - **Anomaly detection**: identifying outliers or abnormal patterns in data.
  - **Automated insight**: generating explanations or hypotheses from data.
  - **Prediction**: forecasting the future values of some variables based on the current or past values of others.
- Bayesian networks are based on the **Bayes' theorem**, which is a mathematical formula that relates the conditional and marginal probabilities of two events.
- Bayes' theorem can be written as:

```math
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
```

where:

  - $P(A|B)$ is the **posterior probability** of event A given event B.
  - $P(B|A)$ is the **likelihood** of event B given event A.
  - $P(A)$ is the **prior probability** of event A.
  - $P(B)$ is the **evidence** or the marginal probability of event B.

- Bayesian networks can be learned from data using various methods, such as **maximum likelihood estimation**, **Bayesian estimation**, or **structure learning algorithms**.
- Bayesian networks can also be constructed from expert knowledge using **domain-specific languages**, **graphical editors**, or **ontologies**.
- Bayesian networks can be queried using various **inference algorithms**, such as **exact inference**, **approximate inference**, or **sampling methods**.
- Bayesian networks can be evaluated using various **performance measures**, such as **accuracy**, **precision**, **recall**, **F1-score**, **AUC**, or **log-likelihood**.
- Bayesian networks can be visualized using various **graphical tools**, such as **d-separation**, **moralization**, **triangulation**, or **junction trees**.