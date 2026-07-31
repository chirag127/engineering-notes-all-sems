### Entropy and information theory for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques

- Entropy is a measure of the uncertainty or randomness of a system. It quantifies how much information is needed to describe the state of the system. 
- Information theory is a branch of mathematics that deals with the transmission, processing, and storage of information. It defines concepts such as information, entropy, mutual information, and information gain. 
- Information is the reduction of uncertainty. It can be measured in bits, which are the smallest units of information. One bit of information can answer a yes/no question. 
- The entropy of a discrete random variable X with possible values x1, x2, ..., xn and probabilities p1, p2, ..., pn is defined as:

    H(X) = - sum(p_i * log_2(p_i)) for i = 1 to n

  The entropy is zero when X has only one possible value (no uncertainty), and it is maximized when X has a uniform distribution (maximum uncertainty).  
- The entropy of a dataset D with m examples and c classes is the entropy of the class distribution:

    H(D) = - sum(p_j * log_2(p_j)) for j = 1 to c

  where p_j is the proportion of examples in D that belong to class j. 
- The conditional entropy of a random variable X given another random variable Y is the average entropy of X when Y is known:

    H(X|Y) = sum(p(y) * H(X|Y=y)) for all y

  The conditional entropy is zero when X is completely determined by Y, and it is equal to H(X) when X and Y are independent.  
- The information gain of a random variable X with respect to another random variable Y is the reduction in entropy of X when Y is known:

    IG(X|Y) = H(X) - H(X|Y)

  The information gain is zero when X and Y are independent, and it is equal to H(X) when X is completely determined by Y.  
- The information gain of a dataset D with respect to an attribute A is the reduction in entropy of D when A is known:

    IG(D|A) = H(D) - H(D|A)

  The information gain is used to measure the quality of a split in decision tree learning. The attribute that maximizes the information gain is chosen as the root node of the tree or a subtree. 
- The cross-entropy of a random variable X with a true probability distribution p and an estimated probability distribution q is the average number of bits needed to encode X using q instead of p:

    H(p, q) = - sum(p(x) * log_2(q(x))) for all x

  The cross-entropy is always greater than or equal to the entropy of X, and it is equal to the entropy when p and q are the same.  
- The cross-entropy loss of a machine learning model is the cross-entropy between the true labels and the predicted probabilities of the model. It is a measure of how well the model fits the data. The cross-entropy loss is minimized when the model predicts the true labels with high confidence.