The following diagram illustrates the basic architecture of a deep network and a shallow network:

```
Deep network:

Input layer:  x1  x2  x3  x4
              |   |   |   |
Hidden layer: o---o---o---o
              |   |   |   |
Hidden layer: o---o---o---o
              |   |   |   |
Output layer: y1  y2  y3  y4

Shallow network:

Input layer:  x1  x2  x3  x4
              |   |   |   |
Hidden layer: o---o---o---o
              |   |   |   |
Output layer: y1  y2  y3  y4
```

A deep network has more than one hidden layer, while a shallow network has only one hidden layer. Both networks can approximate any function, but a deep network can do so with fewer parameters and less computation than a shallow network. A deep network can also learn more abstract and complex features from the input data, while a shallow network can only learn simple and linear features. A deep network can generalize better to new data, while a shallow network can overfit to the training data.