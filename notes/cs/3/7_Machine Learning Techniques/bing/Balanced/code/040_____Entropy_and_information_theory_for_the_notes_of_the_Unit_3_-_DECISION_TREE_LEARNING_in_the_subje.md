### Entropy and information theory for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques

- Entropy is a measure of the uncertainty or randomness of a system. It quantifies how much information is needed to describe the state of the system. 
- Information theory is a branch of mathematics that deals with the transmission, processing, and storage of information. It defines concepts such as information, entropy, mutual information, and information gain. 
- Information is the reduction of uncertainty. It can be measured in bits, which are the smallest units of information. One bit of information is the amount of information needed to make a binary decision. 
- Entropy of a discrete random variable X is defined as:

```math
H(X) = -\sum_{x \in X} p(x) \log_2 p(x)
```

where p(x) is the probability of observing x. Entropy is zero when X has only one possible value, and maximum when X is uniformly distributed.  

- Entropy of a dataset S is the average amount of information needed to identify the class label of an instance in S. It is given by:

```math
H(S) = -\sum_{c \in C} p(c) \log_2 p(c)
```

where C is the set of class labels, and p(c) is the proportion of instances in S that belong to class c. Entropy is zero when S has only one class, and maximum when S is equally split among all classes.  

- Information gain is the reduction in entropy when a dataset is split into subsets based on an attribute. It measures how much the attribute helps to classify the instances. It is given by:

```math
IG(S, A) = H(S) - \sum_{v \in A} \frac{|S_v|}{|S|} H(S_v)
```

where A is the attribute, v is a possible value of A, S_v is the subset of S with A = v, and |S| is the size of S. Information gain is zero when the attribute does not affect the class distribution, and maximum when the attribute perfectly separates the classes.  

- Decision tree learning is a supervised machine learning technique that builds a tree-like structure to classify instances based on a set of attributes. It uses information gain or other criteria to select the best attribute to split the dataset at each node. It recursively partitions the dataset until all instances in a node have the same class label or a stopping condition is met.