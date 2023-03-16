### Fourier Descriptors for Shape-Based Image Retrieval

- Fourier descriptors (FDs) are a method of representing and comparing the shapes of objects in images based on the Fourier analysis of their contours .
- FDs are computed by applying the discrete Fourier transform (DFT) to the complex coordinates of the boundary points of the object .
- FDs have the advantages of being invariant to translation, scale, rotation and starting point of the contour, as well as being able to retain essential information about the shape .
- FDs can be used for shape-based image retrieval, which is the task of finding images that contain objects with similar shapes to a given query image .
- The steps of using FDs for shape-based image retrieval are :
  - Preprocessing: convert the input image to a binary image, extract the boundary of the object of interest, and resample the boundary points to a fixed number.
  - Feature extraction: apply the DFT to the complex coordinates of the boundary points and obtain the FDs as the coefficients of the Fourier series.
  - Feature normalization: make the FDs invariant to translation, scale, rotation and starting point by applying appropriate transformations to the coefficients.
  - Feature selection: reduce the dimensionality of the FDs by discarding the high-frequency components that contain noise and insignificant details of the shape.
  - Feature matching: compare the FDs of the query image with the FDs of the images in the database using a similarity measure, such as the Euclidean distance or the normalized correlation coefficient, and rank the images according to their similarity scores.
- The following diagram illustrates the process of using FDs for shape-based image retrieval:

![Diagram of FDs for shape-based image retrieval](https://www.ijert.org/assets/images/ijertv2is4403/fig1.jpg)