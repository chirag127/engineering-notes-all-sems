### Fourier Descriptors for Shape-Based Image Retrieval

- Fourier descriptors (FDs) are a method of representing and comparing the shapes of objects in images .
- FDs are derived from the Fourier transform of the boundary points of the object .
- FDs have the advantages of being invariant to translation, scale, rotation and starting point of the object  , which means that the shape description does not depend on the position, size, orientation or contour direction of the object.
- FDs can retain the essential information about the contour of the object while discarding the noise and irrelevant details  .
- FDs can be used for shape-based image retrieval, which is the task of finding images that contain objects with similar shapes to a given query object  .
- The steps for using FDs for shape-based image retrieval are  :
  - Extract the boundary points of the object from the image using edge detection or segmentation techniques.
  - Represent the boundary points as a complex vector, where the real and imaginary parts are the x and y coordinates of the points.
  - Apply the discrete Fourier transform (DFT) to the complex vector to obtain the FDs, which are the coefficients of the Fourier series.
  - Normalize the FDs to make them invariant to translation, scale, rotation and starting point by using the following formulas  :
    - Translation invariance: set the first FD to zero.
    - Scale invariance: divide all FDs by the absolute value of the second FD.
    - Rotation invariance: use only the magnitudes of the FDs and discard the phases.
    - Starting point invariance: rotate the complex vector by an angle that minimizes the difference between the first and last FDs.
  - Select a subset of FDs that capture the most important features of the shape, usually the low-frequency components, and discard the rest.
  - Compare the FDs of the query object with the FDs of the objects in the database using a similarity measure, such as the Euclidean distance or the cosine similarity.
  - Retrieve the images that have the most similar FDs to the query object.