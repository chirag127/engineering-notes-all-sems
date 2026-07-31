# Watershed segmentation algorithm

- Watershed segmentation is a classical algorithm used for separating different objects in an image .
- The algorithm treats pixel values as a local topography (elevation), where high intensity denotes peaks and hills, and low intensity denotes valleys .
- The algorithm starts from user-defined markers, which are pixels that belong to different objects or the background .
- The algorithm floods basins from the markers until basins attributed to different markers meet on watershed lines, which are the boundaries of the objects .
- The algorithm can be applied to any grayscale image, such as the gradient magnitude of the original image .
- The algorithm can be implemented using the `cv.watershed()` function in OpenCV or the `skimage.segmentation.watershed()` function in scikit-image.
- The algorithm can be used for counting the objects or for further analysis of the separated objects .

## Example of watershed segmentation

- The following image shows an example of applying watershed segmentation to an image of coins .

![Original image of coins](https://scikit-image.org/docs/stable/_images/sphx_glr_plot_watershed_001.png)

- The first step is to find the markers, which can be done by applying thresholding, distance transform, and peak detection .

![Markers of coins](https://scikit-image.org/docs/stable/_images/sphx_glr_plot_watershed_002.png)

- The second step is to apply the watershed algorithm to the gradient magnitude of the original image, using the markers as seeds .

![Watershed segmentation of coins](https://scikit-image.org/docs/stable/_images/sphx_glr_plot_watershed_003.png)

- The result is a labeled image, where each pixel has a value corresponding to the object it belongs to .

![Labeled image of coins](https://scikit-image.org/docs/stable/_images/sphx_glr_plot_watershed_004.png)

- The final step is to overlay the segmentation boundaries on the original image .

![Segmentation boundaries of coins](https://scikit-image.org/docs/stable/_images/sphx_glr_plot_watershed_005.png)