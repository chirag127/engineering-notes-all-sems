### Bayesian belief networks

- Bayesian belief networks (BBNs) are graphical models that represent the joint probability distribution of a set of variables and their conditional dependencies using a directed acyclic graph (DAG) .
- BBNs can capture the causal relationships among the variables and support inference and learning from data .
- BBNs can handle uncertainty, missing data, and noisy observations, and can be used for classification, prediction, diagnosis, and decision making  .
- BBNs consist of two components: a qualitative component and a quantitative component .
  - The qualitative component is the DAG, where each node represents a variable and each edge represents a direct causal influence from the parent node to the child node. The DAG encodes the conditional independence assumptions among the variables, such that a node is conditionally independent of its non-descendants given its parents .
  - The quantitative component is the set of conditional probability tables (CPTs) associated with each node, which specify the probability distribution of the node given its parents. The CPTs can be learned from data or elicited from experts .
- BBNs can be used for various types of inference, such as:
  - Marginal inference: computing the probability distribution of a subset of variables given some evidence .
  - Conditional inference: computing the probability distribution of a subset of variables given some evidence and some interventions .
  - Causal inference: computing the probability distribution of a subset of variables given some evidence and some counterfactuals .
- BBNs can be learned from data using various methods, such as:
  - Structure learning: finding the optimal DAG that best fits the data, using score-based or constraint-based approaches .
  - Parameter learning: estimating the CPTs of the nodes given a fixed DAG, using maximum likelihood or Bayesian methods .
  - Hybrid learning: combining structure and parameter learning, using search-and-score or Bayesian methods .