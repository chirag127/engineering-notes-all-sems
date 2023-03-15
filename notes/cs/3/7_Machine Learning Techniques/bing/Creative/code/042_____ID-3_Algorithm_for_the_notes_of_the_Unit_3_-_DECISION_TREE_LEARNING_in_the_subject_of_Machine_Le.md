### ID-3 Algorithm

- ID-3 stands for Iterative Dichotomiser 3 .
- It is an algorithm used to generate a decision tree from a dataset .
- It follows a greedy approach of selecting the best attribute that yields maximum information gain or minimum entropy at each node .
- It can handle categorical attributes, but not numerical attributes or missing values.
- It can overfit the training data, so pruning techniques may be needed to avoid overfitting .

#### Steps of ID-3 Algorithm

1. Start with the original set of data as the root node.
2. Calculate the entropy of the target attribute for the data.
3. For each attribute in the data, calculate the information gain or the entropy reduction with respect to the target attribute.
4. Choose the attribute with the highest information gain or the lowest entropy as the splitting attribute for the node.
5. If the entropy of the target attribute is zero (i.e., all examples have the same value of the target attribute), then stop and assign the value of the target attribute as the label of the node.
6. If the entropy of the target attribute is not zero, then for each value of the splitting attribute, create a new child node and repeat the process from step 2 with the subset of data corresponding to that value.
7. Return the decision tree.

#### Example of ID-3 Algorithm

Suppose we have the following dataset of weather conditions and whether to play tennis or not.

| Outlook  | Temperature | Humidity | Wind   | PlayTennis |
| -------- | ----------- | -------- | ------ | ---------- |
| Sunny    | Hot         | High     | Weak   | No         |
| Sunny    | Hot         | High     | Strong | No         |
| Overcast | Hot         | High     | Weak   | Yes        |
| Rain     | Mild        | High     | Weak   | Yes        |
| Rain     | Cool        | Normal   | Weak   | Yes        |
| Rain     | Cool        | Normal   | Strong | No         |
| Overcast | Cool        | Normal   | Strong | Yes        |
| Sunny    | Mild        | High     | Weak   | No         |
| Sunny    | Cool        | Normal   | Weak   | Yes        |
| Rain     | Mild        | Normal   | Weak   | Yes        |
| Sunny    | Mild        | Normal   | Strong | Yes        |
| Overcast | Mild        | High     | Strong | Yes        |
| Overcast | Hot         | Normal   | Weak   | Yes        |
| Rain     | Mild        | High     | Strong | No         |

We want to use the ID-3 algorithm to generate a decision tree that can predict the value of PlayTennis based on the other attributes.

The steps are as follows:

1. Start with the original set of data as the root node. The entropy of the target attribute PlayTennis is 0.940.
2. For each attribute in the data, calculate the information gain with respect to the target attribute PlayTennis. The results are:

| Attribute   | Information Gain |
| ----------- | ---------------- |
| Outlook     | 0.247            |
| Temperature | 0.029            |
| Humidity    | 0.152            |
| Wind        | 0.048            |

3. Choose the attribute with the highest information gain as the splitting attribute for the node. In this case, it is Outlook.
4. If the entropy of the target attribute is zero, then stop and assign the value of the target attribute as the label of the node. In this case, the entropy of the target attribute is not zero, so we continue.
5. For each value of the splitting attribute Outlook, create a new child node and repeat the process from step 2 with the subset of data corresponding to that value. The results are:

| Outlook  | Subset of Data                                                                 | Entropy | Information Gain |
| -------- | ------------------------------------------------------------------------------ | ------- | ---------------- |
| Sunny    | {No, No, No, Yes, Yes}                                                         | 0.971   | 0.570            |
| Overcast | {Yes, Yes, Yes, Yes, Yes}                                                     | 0.000   | 0.940            |
| Rain     | {Yes, Yes, No, Yes, No}                                                       | 0.971   | 0.570            |

6. Return the