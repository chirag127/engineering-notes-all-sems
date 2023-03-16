### Morphological Reconstruction

- Morphological reconstruction is a technique to extract or enhance marked objects from an image without changing their size or shape .
- It uses two images: a marker image and a mask image. The marker image specifies where the processing begins, and the mask image limits the processing region .
- The basic operations of morphological reconstruction are geodesic dilation and geodesic erosion .
- Geodesic dilation spreads the peaks of the marker image to fill in the valleys of the mask image, while geodesic erosion shrinks the valleys of the marker image to fit within the peaks of the mask image .
- Morphological reconstruction can be used for various applications, such as filling holes, extracting the largest connected component, removing small objects, smoothing boundaries, and separating touching objects .
- The following diagram illustrates the process of morphological reconstruction by geodesic dilation:

```
  Marker Image     Mask Image     Result Image

    0 0 0 0 0       0 0 0 0 0       0 0 0 0 0
    0 1 0 0 0       0 1 1 1 0       0 1 1 1 0
    0 0 0 0 0       0 1 1 1 0       0 1 1 1 0
    0 0 0 0 0       0 1 1 1 0       0 1 1 1 0
    0 0 0 0 0       0 0 0 0 0       0 0 0 0 0
```

- The marker image has a single peak at (2,2), and the mask image has a square region of ones. The result image shows the peak spreading out to fill the square region, while being constrained by the mask image. The process stops when no more changes occur in the result image.