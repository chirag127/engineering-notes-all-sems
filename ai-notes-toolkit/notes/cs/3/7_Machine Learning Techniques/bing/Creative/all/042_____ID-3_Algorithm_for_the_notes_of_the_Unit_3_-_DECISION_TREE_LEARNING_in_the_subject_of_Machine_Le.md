# ID-3 Algorithm

- ID-3 stands for Iterative Dichotomiser 3 .
- It is a classification algorithm that follows a greedy approach of building a decision tree by selecting the best attribute that yields maximum information gain or minimum entropy .
- It is used to generate a decision tree from a dataset.
- It is a precursor to the C4.5 algorithm, and is typically used in the machine learning and natural language processing domains.

## Steps of ID-3 Algorithm

- The ID-3 algorithm begins with the original set as the root node.
- On each iteration of the algorithm, it iterates through every unused attribute of the set and calculates the entropy or the information gain of that attribute.
- It then selects the attribute which has the smallest entropy or the largest information gain value.
- The set is then split by the selected attribute to produce subsets of the data.
- The algorithm recursively repeats the above steps on each subset until one of the following conditions is met:
  - The subset is pure, i.e., all the instances belong to the same class.
  - There are no more unused attributes.
  - The subset is empty.
- The resulting decision tree is stored in memory and can be used to classify new test cases by traversing the tree using the features of the datum to arrive at a leaf node.

## Example of ID-3 Algorithm

- Suppose we have a dataset of weather conditions and whether to play tennis or not, as shown below:

| Outlook  | Temperature | Humidity | Wind   | Play Tennis |
| -------- | ----------- | -------- | ------ | ----------- |
| Sunny    | Hot         | High     | Weak   | No          |
| Sunny    | Hot         | High     | Strong | No          |
| Overcast | Hot         | High     | Weak   | Yes         |
| Rain     | Mild        | High     | Weak   | Yes         |
| Rain     | Cool        | Normal   | Weak   | Yes         |
| Rain     | Cool        | Normal   | Strong | No          |
| Overcast | Cool        | Normal   | Strong | Yes         |
| Sunny    | Mild        | High     | Weak   | No          |
| Sunny    | Cool        | Normal   | Weak   | Yes         |
| Rain     | Mild        | Normal   | Weak   | Yes         |
| Sunny    | Mild        | Normal   | Strong | Yes         |
| Overcast | Mild        | High     | Strong | Yes         |
| Overcast | Hot         | Normal   | Weak   | Yes         |
| Rain     | Mild        | High     | Strong | No          |

- The ID-3 algorithm will start with the original set as the root node and calculate the entropy of the target attribute (Play Tennis) as follows:

  - Entropy(Play Tennis) = -P(Yes) * log2(P(Yes)) - P(No) * log2(P(No))
  - P(Yes) = 9/14, P(No) = 5/14
  - Entropy(Play Tennis) = - (9/14) * log2(9/14) - (5/14) * log2(5/14) = 0.940

- The algorithm will then calculate the information gain of each attribute by subtracting the entropy of the attribute from the entropy of the target attribute:

  - Information Gain(Outlook) = Entropy(Play Tennis) - Entropy(Outlook)
  - Entropy(Outlook) = P(Sunny) * Entropy(Sunny) + P(Overcast) * Entropy(Overcast) + P(Rain) * Entropy(Rain)
  - P(Sunny) = 5/14, P(Overcast) = 4/14, P(Rain) = 5/14
  - Entropy(Sunny) = - (2/5) * log2(2/5) - (3/5) * log2(3/5) = 0.971
  - Entropy(Overcast) = - (4/4) * log2(4/4) - (0/4) * log2(0/4) = 0
  - Entropy(Rain)