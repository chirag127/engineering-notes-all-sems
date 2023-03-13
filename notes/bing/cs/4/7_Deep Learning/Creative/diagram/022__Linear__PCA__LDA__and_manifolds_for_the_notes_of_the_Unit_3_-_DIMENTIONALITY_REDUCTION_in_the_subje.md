The following is a detailed ASCII diagram for Linear (PCA, LDA) and manifolds for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning.

### Linear (PCA, LDA) and manifolds

```
+-------------------+     +-------------------+     +-------------------+
|                   |     |                   |     |                   |
|  High-dimensional |     |  Low-dimensional  |     |  Low-dimensional  |
|      data         |     |      data         |     |      data         |
|                   |     |                   |     |                   |
+-------------------+     +-------------------+     +-------------------+
|                   |     |                   |     |                   |
|  X = [x1, x2, ...]|     |  Y = [y1, y2, ...]|     |  Z = [z1, z2, ...]|
|                   |     |                   |     |                   |
+-------------------+     +-------------------+     +-------------------+
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          |                       |                       |
          v                       v                       v
+-------------------+     +-------------------+     +-------------------+
|                   |     |                   |     |                   |
| Principal Component|     | Linear Discriminant|     | Manifold Learning |
|     Analysis      |     |     Analysis      |     |                   |
|                   |     |                   |     |                   |
+-------------------+     +-------------------+     +-------------------+
|                   |     |                   |     |                   |
|  PCA finds the    |     |  LDA finds the    |     |  Manifold learning|
|  linear combination|     |  linear combination|     |  finds the non-linear|
|  of features that |     |  of features that |     |  transformation of |
|  maximizes the    |     |  maximizes the    |     |  features that     |
|  variance of the  |     |  separation of the|     |  preserves the     |
|  projected data   |     |  projected classes|     |  local structure   |
|                   |     |                   |     |  of the data       |
|  PCA is an        |     |  LDA is a         |     |  Manifold learning |
|  unsupervised     |     |  supervised       |     |  is an unsupervised|
|  method           |     |  method           |     |  method           |
|                   |     |                   |     |                   |
+-------------------+     +-------------------+     +-------------------+
```