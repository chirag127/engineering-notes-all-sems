### Information gain for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques

- Information gain is a measure of how much information a feature provides about the class label of a dataset .
- Information gain is based on the concept of entropy, which is the degree of uncertainty or randomness in a dataset .
- Entropy can be calculated as the negative sum of the probabilities of each class label multiplied by the logarithm of those probabilities .
- Information gain can be calculated as the difference between the entropy of the dataset before and after splitting it by a feature .
- Information gain can be used as a criterion to select the best feature to split a node in a decision tree .
- The feature with the highest information gain is the one that reduces the most entropy or uncertainty in the dataset .
- Information gain can help to build a decision tree that is accurate, simple, and interpretable .
- Information gain can be expressed as:

```
IG(S, A) = H(S) - H(S|A)
```

where:

  - IG(S, A) is the information gain of splitting dataset S by feature A
  - H(S) is the entropy of dataset S
  - H(S|A) is the conditional entropy of dataset S given feature A
  - H(S|A) can be calculated as the weighted average of the entropies of the subsets of S obtained by splitting by A .

- Information gain can be illustrated by an example:

  - Suppose we have a dataset of 14 instances of playing tennis, with two features (outlook and humidity) and one class label (play or not play).
  - The entropy of the dataset before splitting is:

  ```
  H(S) = - (9/14) * log2(9/14) - (5/14) * log2(5/14) = 0.94
  ```

  - The entropy of the dataset after splitting by outlook is:

  ```
  H(S|outlook) = (5/14) * H(Sunny) + (4/14) * H(Overcast) + (5/14) * H(Rainy)
  ```

  where:

    - H(Sunny) is the entropy of the subset of instances with outlook = Sunny
    - H(Overcast) is the entropy of the subset of instances with outlook = Overcast
    - H(Rainy) is the entropy of the subset of instances with outlook = Rainy
    - H(Sunny) can be calculated as:

    ```
    H(Sunny) = - (2/5) * log2(2/5) - (3/5) * log2(3/5) = 0.97
    ```

    - H(Overcast) can be calculated as:

    ```
    H(Overcast) = - (4/4) * log2(4/4) - (0/4) * log2(0/4) = 0
    ```

    - H(Rainy) can be calculated as:

    ```
    H(Rainy) = - (3/5) * log2(3/5) - (2/5) * log2(2/5) = 0.97
    ```

  - Therefore, the entropy of the dataset after splitting by outlook is:

  ```
  H(S|outlook) = (5/14) * 0.97 + (4/14) * 0 + (5/14) * 0.97 = 0.69
  ```

  - The information gain of splitting by outlook is:

  ```
  IG(S, outlook) = H(S) - H(S|outlook) = 0.94 - 0.69 = 0.25
  ```

  - Similarly, the information gain of splitting by humidity can be calculated as:

  ```
  IG(S, humidity) = H(S) - H(S|humidity) = 0.94 - 0.79 = 0.15
  ```

  - Since the information gain of splitting by outlook is higher than the information gain of splitting by humidity, outlook is the best feature to split the root node of