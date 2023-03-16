# Fourier Descriptors for Shape-Based Image Retrieval

- Fourier descriptors are a method of representing the shape of an object in an image using the Fourier transform of its boundary.
- Fourier descriptors are invariant to translation, scale, rotation and starting point of the boundary, which makes them suitable for shape-based image retrieval.
- Fourier descriptors can capture the essential information about the contour of the object, while discarding the irrelevant details such as noise or minor variations.
- Fourier descriptors are computed as follows :
  - Extract the boundary of the object from the image using edge detection or segmentation techniques.
  - Represent the boundary as a complex-valued function of a parameter t, such as x(t) + iy(t), where x(t) and y(t) are the coordinates of the boundary points.
  - Apply the discrete Fourier transform (DFT) to the complex-valued function to obtain the Fourier coefficients, which are the Fourier descriptors of the shape.
  - Normalize the Fourier descriptors to make them invariant to translation, scale, rotation and starting point, by using the following rules :
    - Discard the first Fourier coefficient, which corresponds to the mean position of the boundary.
    - Divide all the Fourier coefficients by the absolute value of the second Fourier coefficient, which corresponds to the scale of the boundary.
    - Multiply all the Fourier coefficients by a complex number that cancels the phase of the second Fourier coefficient, which corresponds to the rotation of the boundary.
    - Discard the Fourier coefficients that correspond to high frequencies, which capture the noise or minor variations of the boundary.
- Fourier descriptors can be used to measure the similarity between two shapes by computing the Euclidean distance between their normalized Fourier coefficients .
- Fourier descriptors can also be used to reconstruct the shape of the object by applying the inverse DFT to the normalized Fourier coefficients .
- Fourier descriptors have some limitations, such as :
  - They are sensitive to the sampling rate of the boundary, which affects the number and accuracy of the Fourier coefficients.
  - They are not invariant to the topology of the shape, such as holes or branches, which may affect the similarity measure.
  - They are not invariant to the deformation of the shape, such as bending or stretching, which may change the frequency spectrum of the boundary.