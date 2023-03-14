## Unit 3 - DIMENTIONALITY REDUCTION

Dimensionality reduction is the process of transforming data from a high-dimensional space into a low-dimensional space, while preserving some meaningful properties of the original data. Dimensionality reduction can be done in two different ways: feature selection and feature projection. Feature selection approaches try to find a subset of the input variables that are most relevant for the analysis. Feature projection approaches try to find a smaller set of new variables, each being a combination of the input variables, that contain basically the same information as the original data.

The following diagram illustrates the basic idea of dimensionality reduction:

```
+-------------------+       +-------------------+
| High-dimensional  |       | Low-dimensional   |
| data              |       | data              |
|                   |       |                   |
| x1 x2 x3 x4 x5 x6 |       | y1 y2             |
|                   |       |                   |
| 1  2  3  4  5  6  |       | 2  3              |
| 2  3  4  5  6  7  |       | 3  4              |
| 3  4  5  6  7  8  |       | 4  5              |
| 4  5  6  7  8  9  |       | 5  6              |
| 5  6  7  8  9  10 |       | 6  7              |
|                   |       |                   |
+-------------------+       +-------------------+
        |                          ^
        |                          |
        |                          |
        |                          |
        v                          |
+-------------------+              |
| Dimensionality    |              |
| reduction         |              |
| technique         |              |
|                   |              |
| e.g. PCA, SVD, LDA|              |
|                   |              |
+-------------------+              |
        |                          |
        |                          |
        |                          |
        |                          |
        v                          |
+-------------------+              |
| Transformation    |              |
| matrix            |              |
|                   |              |
| W                 |              |
|                   |              |
+-------------------+              |
        |                          |
        |                          |
        |                          |
        |                          |
        v                          |
+-------------------+              |
| Matrix            |              |
| multiplication    |              |
|                   |              |
| Y = XW            |              |
|                   |              |
+-------------------+              |
        |                          |
        |                          |
        |                          |
        |                          |
        v                          |
+-------------------+              |
| Error             |              |
| measurement       |              |
|                   |              |
| e.g. MSE, RMSE    |              |
|                   |              |
+-------------------+              |
        |                          |
        |                          |
        |                          |
        |                          |
        v                          |
+-------------------+              |
| Optimization      |              |
| algorithm         |              |
|                   |              |
| e.g. gradient     |              |
| descent, SVD      |              |
|                   |              |
+-------------------+              |
        |                          |
        |                          |
        |                          |
        |                          |
        v                          |
+-------------------+              |
| Optimal           |              |
| transformation    |              |
| matrix            |              |
|                   |              |
| W*                |              |
|                   |              |
+-------------------+              |
        |                          |
        |                          |
        |                          |
        |                          |
        v                          |
+-------------------+              |
| Final low-        |              |
| dimensional data  |              |
|                   |              |
| Y* = XW*          |              |
|                   |              |
+-------------------+              |
        |                          |
        |                          |
        |                          |
        |                          |
        v                          |
+-------------------+              |
| Data analysis     |              |
| or visualization  |              |
|                   |              |
| e.g. regression,  |              |
| clustering, PCA   |              |
| plot              |              |
|                   |              |
+-------------------+              |
        |                          |
        |                          |
        |                          |
        |                          |
        v                          |
+-------------------+              |
| Results or        |              |
| insights          |              |
|                   |              |
| e.g. coefficients,|              |
| clusters, patterns|              |
|                   |              |
+-------------------