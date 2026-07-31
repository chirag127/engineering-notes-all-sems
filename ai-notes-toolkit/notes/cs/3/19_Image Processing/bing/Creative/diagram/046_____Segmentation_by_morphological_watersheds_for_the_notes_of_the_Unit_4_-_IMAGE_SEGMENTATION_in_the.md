### Segmentation by morphological watersheds

- Segmentation is the process of dividing an image into meaningful regions or objects based on some criteria, such as brightness, color, texture, etc.  
- Morphological watersheds are a segmentation technique that uses the concept of topographic relief to partition an image into catchment basins and watershed lines.  
- A catchment basin is a region where all the water flows to a single minimum point, and a watershed line is a boundary that separates adjacent catchment basins.  
- The idea is to imagine the image as a landscape, where the pixel intensity represents the height, and to flood the landscape from its local minima. The regions that are filled with water are the catchment basins, and the regions where the water from different basins meet are the watershed lines.  
- The morphological watershed algorithm can be summarized as follows   :
  - Convert the image to grayscale and apply a gradient operator to enhance the edges.
  - Find the local minima of the gradient image and assign them unique labels. These are the initial markers for the catchment basins.
  - Perform a geodesic dilation of the markers, which means to dilate them with respect to the gradient image, such that the dilation does not cross the edges or the existing markers.
  - Repeat the geodesic dilation until all the pixels are labeled. The pixels that are not labeled by any marker are the watershed lines.
- The morphological watershed algorithm can segment complex images with irregular shapes and touching objects, but it is sensitive to noise and may produce over-segmentation.   
- To reduce over-segmentation, some preprocessing steps can be applied, such as smoothing the image, removing small regions, or using markers that are more meaningful than local minima.