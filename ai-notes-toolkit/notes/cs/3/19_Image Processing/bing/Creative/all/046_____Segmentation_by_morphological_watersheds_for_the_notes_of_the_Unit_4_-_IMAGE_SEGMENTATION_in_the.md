# Segmentation by morphological watersheds

- Segmentation is the process of dividing an image into meaningful regions or objects based on some criteria, such as brightness, color, texture, etc.  
- Segmentation by morphological watersheds is a region-based technique that uses the concept of watershed lines to separate the regions of an image.  
- A watershed line is a boundary that separates two catchment basins, which are regions where water flows towards a local minimum.  
- The idea of morphological watersheds is to imagine the image as a topographic surface, where the pixel intensity represents the height. Then, water is poured on the surface from different sources (markers or seeds) and the water flows towards the local minima. The regions where the water from different sources meet are the watershed lines, which form the boundaries of the segmented regions.   
- The morphological watersheds can be computed using different methods, such as distance transform, gradient magnitude, image smoothing, etc.    
- The advantages of morphological watersheds are that they are robust to noise, can handle complex shapes, and can segment images with low contrast or overlapping objects.   
- The disadvantages of morphological watersheds are that they can produce over-segmentation, require manual selection of markers, and can be sensitive to the choice of parameters.