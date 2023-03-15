### Watershed segmentation algorithm

Watershed segmentation is a classical algorithm used for separating different objects in an image. It is a region-based technique that utilizes image morphology. The algorithm treats pixel values as a local topography (elevation) and floods basins from user-defined markers until basins attributed to different markers meet on watershed lines.

The algorithm requires the selection of at least one marker, or "seed" point, interior to each object of the image, including the background as a separate object. It is used for segmentation in complex images where simple thresholding and contour detection may not give proper results. The algorithm is based on extracting sure background and foreground and then using markers to make the watershed run and detect the exact boundaries.

Watershed algorithms are primarily used for object segmentation purposes, allowing for counting the objects or for further analysis of the separated objects. Any grayscale image can be viewed as a topographic surface where high intensity denotes peaks and hills while low intensity denotes valleys.