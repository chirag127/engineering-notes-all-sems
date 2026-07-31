### Entropy and information theory for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques

- Entropy is a measure of the uncertainty or randomness of a system. It quantifies how much information is needed to describe the state of the system. 
- Information theory is a branch of mathematics that deals with the transmission, processing, and storage of information. It defines concepts such as information, entropy, mutual information, and information gain. 
- In machine learning, entropy and information theory are used to measure the quality of a split in a decision tree, the similarity between two probability distributions, and the amount of information gained from observing a feature or a label.   
- Some of the key concepts and formulas related to entropy and information theory are:

  - Entropy of a discrete random variable X with possible values x1, x2, ..., xn and probabilities p1, p2, ..., pn is defined as:

    H(X) = - sum(p_i * log(p_i)) for i = 1 to n

    where log is the logarithm base 2. Entropy is zero when X has only one possible value (certainty) and maximum when X has a uniform distribution (maximum uncertainty).  

  - Conditional entropy of a discrete random variable X given another discrete random variable Y with possible values y1, y2, ..., ym and probabilities q1, q2, ..., qm is defined as:

    H(X|Y) = sum(q_j * H(X|Y = y_j)) for j = 1 to m

    where H(X|Y = y_j) is the entropy of X when Y is fixed at y_j. Conditional entropy measures the uncertainty of X after observing Y. It is zero when X and Y are perfectly dependent and equal to H(X) when X and Y are independent.  

  - Information gain of a discrete random variable X with respect to another discrete random variable Y is defined as:

    IG(X;Y) = H(X) - H(X|Y)

    It measures the reduction in the uncertainty of X after observing Y. It is zero when X and Y are independent and maximum when X and Y are perfectly dependent.  

  - Cross-entropy of two discrete probability distributions P and Q over the same set of possible values x1, x2, ..., xn is defined as:

    H(P,Q) = - sum(p_i * log(q_i)) for i = 1 to n

    where p_i and q_i are the probabilities of x_i according to P and Q, respectively. Cross-entropy measures the average number of bits needed to encode the outcomes of P using the code based on Q. It is equal to H(P) when P and Q are identical and greater than H(P) when P and Q are different.  

  - Kullback-Leibler divergence or relative entropy of two discrete probability distributions P and Q over the same set of possible values x1, x2, ..., xn is defined as:

    D(P||Q) = sum(p_i * log(p_i / q_i)) for i = 1 to n

    where p_i and q_i are the probabilities of x_i according to P and Q, respectively. It measures the difference between P and Q in terms of the information lost when Q is used to approximate P. It is zero when P and Q are identical and positive when P and Q are different.  

- In decision tree learning, entropy and information gain are used to select the best attribute to split the data at each node. The attribute that maximizes the information gain or equivalently minimizes the entropy of the child nodes is chosen. This ensures that the tree is built in a way that reduces the uncertainty of the class labels as much as possible.