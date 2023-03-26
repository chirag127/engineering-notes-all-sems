 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Topological and Texture Descriptors

1. Topological Descriptors
- Neighbourhood Graph - Connectivity of pixels in an image. Extracts information about neighbouring pixels of a pixel.
- Adjacency Graph - Connectivity of adjacent pixels in an image. Extracts information about adjacent pixels of a pixel.
- Voronoi Diagram - Divides an image into regions based on distance to nearest neighbour. Can extract features based on Voronoi cells/regions.

2. Texture Descriptors
- Grey Level Co-occurrence Matrix (GLCM) - Calculates probability of occurrence of pairs of pixels with specific values/grey levels at a given offset. Gives information about texture of an image.
- Grey Level Run Length Matrix (GLRLM) - Calculates occurrences of consecutive pixels (runs) with same grey level. Gives information about texture of an image.
- Spatial Grey Level Dependence Matrix - Calculates probability of a pixel having a particular grey level based on grey levels of surrounding pixels. Gives information about texture of an image.

These topological and texture descriptors can be used to extract distinctive features from images which can be used for segmentation, classification, etc. The performance of these descriptors varies based on the type of image and application. Appropriate descriptors and parameters must be chosen for optimal results.