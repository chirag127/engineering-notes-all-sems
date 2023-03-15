### Entropy and information theory for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques

- Entropy is a measure of the uncertainty or randomness of a system. It quantifies how much information is needed to describe the state of the system. 
- Information theory is a branch of mathematics that deals with the transmission, processing, and storage of information. It defines concepts such as information, entropy, mutual information, and information gain. 
- Information is the reduction of uncertainty. It can be measured in bits, which are the smallest units of information. One bit of information is the amount of information needed to make a binary decision. 
- The entropy of a discrete random variable X with possible values x1, x2, ..., xn and probability distribution P(X) is defined as:

    H(X) = - sum(P(xi) * log2(P(xi))) for i = 1 to n

  The entropy of X is the average amount of information needed to specify the value of X. It is zero when X is deterministic and maximal when X is uniformly distributed.  
- The entropy of a joint distribution of two random variables X and Y is defined as:

    H(X, Y) = - sum(P(xi, yj) * log2(P(xi, yj))) for i = 1 to n and j = 1 to m

  The entropy of (X, Y) is the average amount of information needed to specify the values of both X and Y. It is equal to the entropy of X plus the entropy of Y given X, or the entropy of Y plus the entropy of X given Y.  
- The conditional entropy of a random variable X given another random variable Y is defined as:

    H(X | Y) = - sum(P(xi, yj) * log2(P(xi | yj))) for i = 1 to n and j = 1 to m

  The conditional entropy of X given Y is the average amount of information needed to specify the value of X when the value of Y is known. It is zero when X is completely determined by Y and maximal when X is independent of Y.  
- The mutual information of two random variables X and Y is defined as:

    I(X; Y) = H(X) - H(X | Y) = H(Y) - H(Y | X) = H(X) + H(Y) - H(X, Y)

  The mutual information of X and Y is the amount of information that X and Y share. It is zero when X and Y are independent and maximal when X and Y are identical. It measures the reduction of uncertainty about X when Y is known, or vice versa.  
- The information gain of a random variable X with respect to another random variable Y is defined as:

    IG(X; Y) = H(Y) - H(Y | X)

  The information gain of X with respect to Y is the amount of information that Y gains from knowing X. It is equal to the mutual information of X and Y. It measures the expected reduction of entropy of Y when X is given.  
- In machine learning, entropy and information theory are used to measure the quality of a split in a decision tree. A decision tree is a hierarchical structure that partitions the data into subsets based on some attribute values. The goal is to create a tree that minimizes the entropy or maximizes the information gain at each node.  
- The entropy of a dataset D with possible class labels c1, c2, ..., ck and class distribution P(C) is defined as:

    H(D) = - sum(P(ci) * log2(P(ci))) for i = 1 to k

  The entropy of D is the average amount of information needed to specify the class label of an instance in D. It is zero when D is pure (all instances have the same class label) and maximal when D is balanced (all class labels have equal probability). 
- The information gain of an attribute A with possible values v1, v2, ..., vm and subset distribution P(A) with respect to a dataset D is defined as:

    IG(D, A) = H(D) - sum(P(vi) * H(D | vi)) for i = 1 to m