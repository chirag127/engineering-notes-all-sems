# Relationships between pixels

- A pixel is the smallest unit of a digital image that can be displayed or manipulated.
- Pixels have coordinates that indicate their position in the image, usually starting from the top-left corner as the origin.
- Pixels can have different values depending on the color space and bit depth of the image, such as grayscale, RGB, CMYK, etc.
- Pixels can have different relationships with each other based on their spatial proximity and connectivity.
- Spatial proximity refers to how close two pixels are in terms of their coordinates, such as horizontal, vertical, or diagonal distance.
- Connectivity refers to how two pixels are linked by a path of pixels that share the same value or property, such as intensity, color, or region.
- There are different types of connectivity that can be defined for pixels, such as 4-connectivity, 8-connectivity, and m-connectivity .
  - 4-connectivity: Two pixels are 4-connected if they are horizontal or vertical neighbors, that is, they share an edge. The 4-neighbors of a pixel p are denoted by N4(p) and have the coordinates (x+1,y), (x-1,y), (x,y+1), and (x,y-1), where (x,y) are the coordinates of p.
  - 8-connectivity: Two pixels are 8-connected if they are horizontal, vertical, or diagonal neighbors, that is, they share an edge or a corner. The 8-neighbors of a pixel p are denoted by N8(p) and have the coordinates (x+1,y), (x-1,y), (x,y+1), (x,y-1), (x+1,y+1), (x-1,y+1), (x+1,y-1), and (x-1,y-1), where (x,y) are the coordinates of p.
  - m-connectivity: Two pixels are m-connected if they satisfy a specific condition that depends on the image and the application. For example, two pixels can be m-connected if they have the same intensity value, or if they belong to the same region or object.
- The relationships between pixels can be used to define and analyze the properties and features of digital images, such as regions, boundaries, edges, shapes, textures, etc.
- The relationships between pixels can also be used to perform various operations and transformations on digital images, such as filtering, segmentation, morphological processing, etc.