A Probabilistic Theory of Deep Learning is a framework for understanding, analyzing, and synthesizing deep learning architectures based on a Bayesian generative probabilistic model that explicitly captures variation due to nuisance variables . The model is called the Deep Rendering Model (DRM) and it consists of a hierarchy of latent variables that represent different levels of abstraction and nuisance variation in the data. The DRM can be used to derive two of the current leading deep learning systems, deep convolutional neural networks (DCNs) and random decision forests (RDFs), as well as to provide insights into their strengths and limitations.

The following diagram illustrates the basic architecture of a DRM:

```
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  Class labels   |  |  Class labels   |  |  Class labels   |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        v                 v                 v
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  High-level     |  |  High-level     |  |  High-level     |
|  features       |  |  features       |  |  features       |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        v                 v                 v
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  Mid-level      |  |  Mid-level      |  |  Mid-level      |
|  features       |  |  features       |  |  features       |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        v                 v                 v
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  Low-level      |  |  Low-level      |  |  Low-level      |
|  features       |  |  features       |  |  features       |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        |                 |                 |
        v                 v                 v
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  Data           |  |  Data           |  |  Data           |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
```

Each layer of latent variables corresponds to a level of abstraction and nuisance variation in the data. For example, the high-level features may represent the object category, the mid-level features may represent the object pose and shape, and the low-level features may represent the object texture and lighting. The data