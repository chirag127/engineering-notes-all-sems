### Segmentation by morphological watersheds

- Segmentation is the process of dividing an image into meaningful regions or objects based on some criteria, such as brightness, color, texture, etc.  
- Morphological watersheds are a segmentation technique that uses the concept of topographic relief to partition an image into catchment basins and watershed lines.  
- A catchment basin is a region where all the water flows to a single minimum point, and a watershed line is a boundary that separates adjacent catchment basins.  
- The idea is to imagine the image as a landscape, where the pixel intensity represents the height, and to flood the landscape from its minima with water of different colors.  
- The regions where the water of different colors meet are the watershed lines, and the regions filled with the same color are the catchment basins.  
- The catchment basins correspond to the objects of interest in the image, and the watershed lines correspond to the edges or boundaries of the objects.  
- The morphological watershed algorithm can be summarized as follows   :

  - Step 1: Compute the gradient magnitude of the image to enhance the edges and reduce the noise.
  - Step 2: Find the regional minima of the gradient image, and assign a unique label to each minimum and its neighboring pixels of the same value.
  - Step 3: Perform a flooding process, where the labeled pixels are considered as water sources, and the unlabeled pixels are considered as the landscape to be flooded.
  - Step 4: At each iteration, increase the water level by one unit, and expand the catchment basins by adding the unlabeled pixels that are adjacent to the labeled pixels and have the same or lower value than the current water level.
  - Step 5: If two or more catchment basins meet at a pixel, assign that pixel to the watershed line, and do not expand the basins through that pixel.
  - Step 6: Repeat steps 4 and 5 until all the pixels are labeled, either as catchment basins or watershed lines.

- The morphological watershed algorithm can produce over-segmentation, where the objects are divided into too many small regions, due to the presence of noise or local minima in the image.   
- To overcome this problem, some preprocessing steps can be applied, such as smoothing the image, filtering the regional minima, or using markers to guide the segmentation.    
- Markers are pixels that belong to the objects or the background, and can be manually or automatically selected.  
- The markers are used to modify the gradient image, such that the catchment basins are forced to pass through the markers, and the watershed lines are forced to avoid the markers.  
- This way, the segmentation is more accurate and robust, and the over-segmentation is reduced.