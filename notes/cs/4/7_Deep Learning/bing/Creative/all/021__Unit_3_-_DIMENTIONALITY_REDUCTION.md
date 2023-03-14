## Unit 3 - DIMENTIONALITY REDUCTION

- Dimensionality reduction is the transformation of data from a high-dimensional space into a low-dimensional space so that the low-dimensional representation retains some meaningful properties of the original data, ideally close to its intrinsic dimension. 
- Working in high-dimensional spaces can be undesirable for many reasons; raw data are often sparse as a consequence of the curse of dimensionality, and analyzing the data is usually computationally intractable. 
- Dimensionality reduction is common in fields that deal with large numbers of observations and/or large numbers of variables, such as signal processing, speech recognition, neuroinformatics, and bioinformatics. 
- Methods are commonly divided into linear and nonlinear approaches.  Approaches can also be divided into feature selection and feature extraction. 
- Dimensionality reduction can be used for noise reduction, data visualization, cluster analysis, or as an intermediate step to facilitate other analyses. 

### Feature selection
- Feature selection approaches try to find a subset of the input variables (also called features or attributes). 
- The three strategies are: the filter strategy (e.g. information gain), the wrapper strategy (e.g. search guided by accuracy), and the embedded strategy (selected features are added or removed while building the model based on prediction errors). 
- Data analysis such as regression or classification can be done in the reduced space more accurately than in the original space. 

### Feature projection
- Feature projection (also called feature extraction) transforms the data from the high-dimensional space to a space of fewer dimensions. 
- The data transformation may be linear, as in principal component analysis (PCA), but many nonlinear dimensionality reduction techniques also exist.  
- For multidimensional data, tensor representation can be used in dimensionality reduction through multilinear subspace learning. 

#### Principal component analysis (PCA)
- The main linear technique for dimensionality reduction, principal component analysis, performs a linear mapping of the data to a lower-dimensional space in such a way that the variance of the data in the low-dimensional representation is maximized. 
- In practice, the covariance (and sometimes the correlation) matrix of the data is constructed and the eigenvectors on this matrix are computed. 
- The eigenvectors that correspond to the largest eigenvalues (the principal components) can now be used to reconstruct a large fraction of the variance of the original data. 
- Moreover, the first few eigenvectors can often be interpreted in terms of the large-scale physical behavior of the system, because they often contribute the vast majority of the system's energy, especially in low-dimensional systems. 

A visual depiction of the resulting PCA projection for a set of 2D points.

```
    ^
    |  x
    |    x
    |      x
    |        x
    |          x
    |            x
    |              x
    |                x
    |                  x
    |                    x
    |                      x
    |                        x
    |                          x
    |                            x
    |                              x
    |                                x
    |                                  x
    |                                    x
    |                                      x
    |                                        x
    |                                          x
    |                                            x
    |                                              x
    |                                                x
    |                                                  x
    |                                                    x
    |                                                      x
    |                                                        x
    |                                                          x
    |                                                            x
    |                                                              x
    |                                                                x
    |                                                                  x
    |                                                                    x
    |                                                                      x
    |                                                                        x
    |                                                                          x
    |                                                                            x
    |                                                                              x
    |                                                                                x
    |                                                                                  x
    |                                                                                    x
    |                                                                                      x
    |                                                                                        x
    |                                                                                          x
    |                                                                                            x
    |                                                                                              x
    |                                                                                                x
    |                                                                                                  x
    |                                                                                                    x
    |                                                                                                      x
    |                                                                                                        x
    |                                                                                                          x
    |                                                                                                            x
    |                                                                                                              x
    |                                                                                                                x
    |                                                                                                                  x
    |                                                                                                                    x
    |                                                                                                                      x
    |                                                                                                                        x
    |                                                                                                                          x
    |                                                                                                                            x
    |