## Unit 3 - DECISION TREE LEARNING

Decision tree learning is a method for approximating discrete-valued target functions, in which the learned function is represented by a decision tree. Decision tree learning is one of the most widely used and practical methods for inductive inference.

1. **Decision Tree Representation**: Decision trees represent disjunctions of conjunctions of constraints on the attribute values of instances. Each internal node in the tree tests the value of one of the attributes, and the branches from the node are labeled with the possible values of the attribute. Each leaf node in the tree specifies a value to be returned by the function.

2. **Hypothesis Space Search**: Decision tree learning algorithms search the space of decision trees, guided by a heuristic measure of the quality of the trees. The most common heuristic is the information gain measure, which is based on the concept of entropy from information theory.

3. **Inductive Bias**: The inductive bias of decision tree learning algorithms is a preference for smaller trees over larger trees. This bias is known as the Occam's razor bias, and it is based on the principle that simpler hypotheses are more likely to be correct than complex hypotheses.

4. **Overfitting and Pruning**: Decision tree learning algorithms can suffer from overfitting, in which the learned tree is too complex and does not generalize well to new instances. To avoid overfitting, decision tree learning algorithms often include a pruning step, in which branches of the tree that do not contribute to the accuracy of the tree on a validation set are removed.

5. **Advantages and Disadvantages**: Decision tree learning has several advantages, including its simplicity, interpretability, and ability to handle both discrete and continuous attributes. However, it also has some disadvantages, including its tendency to overfit, its sensitivity to small changes in the training data, and its inability to represent certain types of functions, such as XOR.