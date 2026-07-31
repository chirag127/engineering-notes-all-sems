### Segmentation by morphological watersheds

- Segmentation is the process of dividing an image into meaningful regions or objects based on some criteria, such as brightness, color, texture, etc.  
- Morphological watersheds are a region-based segmentation technique that uses the concept of topographic surface and catchment basins to separate the regions.   
- The basic idea is to imagine the image as a landscape, where the pixel intensity represents the height. The local minima of the image are the sources of water, and the water flows from the lower regions to the higher regions. The boundaries of the regions where the water from different sources meet are the watersheds.   
- The morphological watersheds can be computed using the following steps:   
  - Find the local minima of the image and assign them unique labels. These are the initial markers or seeds for the regions.
  - Perform a flooding process, where the neighboring pixels of the markers are visited in increasing order of intensity and assigned the same label as the marker, unless they are already visited by another marker. This creates a gradient image, where the intensity represents the distance from the nearest marker.
  - Identify the pixels that have more than one nearest marker. These are the watershed pixels, and they form the boundaries of the regions.
  - Optionally, apply some post-processing techniques to reduce over-segmentation, such as merging small regions, smoothing the boundaries, or using edge information.