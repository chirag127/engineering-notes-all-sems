### Decision Tree Learning

- Decision tree learning is a **supervised machine learning** technique that can create both **classification** and **regression** models  .
- A decision tree is a graphical representation of a **sequence of decisions** and their possible **outcomes**  .
- A decision tree consists of three types of nodes  :
  - A **root node** that has no incoming edges and zero or more outgoing edges.
  - An **internal node** that has one incoming edge and two or more outgoing edges.
  - A **leaf node** that has one incoming edge and no outgoing edges.
- Each internal node represents a **test** or a **condition** on an **attribute** or a **feature** of the data  .
- Each outgoing edge from an internal node corresponds to a possible **value** or a **range** of values of the attribute tested at that node  .
- Each leaf node represents a **class label** (in classification) or a **numeric value** (in regression) of the target variable  .
- To classify or predict a new instance, the decision tree is traversed from the root node to a leaf node by following the edges that match the attribute values of the instance  .
- The class label or the numeric value at the leaf node is the **prediction** or the **output** of the decision tree for that instance  .

A simple example of a decision tree for predicting whether a person will play tennis based on the weather conditions is shown below:

```
        Outlook
    /     |      \
  Sunny Overcast Rainy
  /        |       \
 No      Yes      Windy
                /      \
              Strong   Weak
              /          \
             No          Yes
```

- The root node tests the attribute `Outlook`, which can have three possible values: `Sunny`, `Overcast`, or `Rainy`.
- The internal nodes test the attributes `Humidity` and `Windy`, which can have two possible values each: `High` or `Normal` for `Humidity`, and `Strong` or `Weak` for `Windy`.
- The leaf nodes represent the class labels `Yes` or `No`, indicating whether the person will play tennis or not.
- For example, if the outlook is `Sunny`, the humidity is `High`, and the wind is `Weak`, the decision tree predicts `No` as the output.