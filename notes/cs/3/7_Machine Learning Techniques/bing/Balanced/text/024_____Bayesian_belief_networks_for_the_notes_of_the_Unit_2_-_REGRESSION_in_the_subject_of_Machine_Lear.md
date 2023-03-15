### Bayesian belief networks

- Bayesian belief networks (BBNs) are graphical models that represent the joint probability distribution of a set of variables and their conditional dependencies via a directed acyclic graph (DAG) .
- BBNs can capture the causal relationships among the variables and support inference and learning from data .
- BBNs can handle uncertainty, missing data, and noisy observations, and can be used for classification, prediction, diagnosis, and decision making  .
- BBNs consist of two components: a qualitative component and a quantitative component.
  - The qualitative component is the DAG, where each node represents a variable and each edge represents a direct dependency between two variables. The DAG encodes the conditional independence assumptions among the variables, such that a variable is conditionally independent of its non-descendants given its parents .
  - The quantitative component is the set of conditional probability tables (CPTs) associated with each node, which specify the probability distribution of the node given its parents. The CPTs can be learned from data or elicited from experts .
- BBNs can be used for various types of inference, such as:
  - Marginal inference: computing the probability distribution of a variable given some evidence on other variables .
  - Conditional inference: computing the probability distribution of a variable given some evidence and an intervention on another variable .
  - Causal inference: computing the probability distribution of a variable given some evidence and a counterfactual query on another variable .
- BBNs can be learned from data using various methods, such as:
  - Structure learning: finding the optimal DAG that best fits the data, based on some scoring function and search strategy .
  - Parameter learning: estimating the CPTs of the nodes given a fixed DAG, using maximum likelihood or Bayesian methods .
  - Hybrid learning: combining structure and parameter learning, using methods such as expectation-maximization (EM) or Bayesian model averaging (BMA) .