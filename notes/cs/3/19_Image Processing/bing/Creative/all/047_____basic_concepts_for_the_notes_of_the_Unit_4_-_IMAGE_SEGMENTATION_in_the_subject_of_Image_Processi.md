# Unit 4 - Image Segmentation

## Basic Concepts

- Image segmentation is the process of partitioning an image into multiple segments, each of which consists of pixels that share some common characteristics .
- Image segmentation is typically used to locate objects and boundaries in images, such as edges, contours, regions, or regions of interest (ROI) .
- Image segmentation can reduce the complexity of the image and enable further processing or analysis of each image segment.
- Image segmentation can be performed based on different criteria, such as pixel intensity, color, texture, shape, or semantic meaning .
- Image segmentation can be classified into two main types: supervised and unsupervised .
  - Supervised image segmentation requires prior knowledge or training data to assign labels to pixels or segments .
  - Unsupervised image segmentation does not require any prior knowledge or training data, and relies on clustering or grouping pixels or segments based on their similarity or dissimilarity .
- Image segmentation can also be classified into two main levels: low-level and high-level .
  - Low-level image segmentation operates on the pixel level and focuses on the local features or properties of the image, such as intensity, color, or texture .
  - High-level image segmentation operates on the region level and focuses on the global features or properties of the image, such as shape, context, or semantic meaning .
- Image segmentation can be performed using various techniques, such as thresholding, edge detection, region growing, region splitting and merging, watershed, graph-based, or deep learning .
  - Thresholding is a simple and fast technique that divides the image into two or more segments based on a predefined or adaptive threshold value .
  - Edge detection is a technique that identifies the boundaries or contours of the objects or regions in the image by detecting the changes or discontinuities in the pixel intensity or color .
  - Region growing is a technique that starts from a seed pixel or region and expands it by adding neighboring pixels or regions that satisfy some similarity or homogeneity criteria .
  - Region splitting and merging is a technique that recursively divides the image into smaller regions until each region is homogeneous or satisfies some predefined condition, and then merges the adjacent regions that are similar or compatible .
  - Watershed is a technique that treats the image as a topographic surface and segments it by finding the catchment basins or valleys and the watershed lines or ridges .
  - Graph-based is a technique that represents the image as a graph, where the nodes are the pixels or regions and the edges are the connections or distances between them, and segments it by finding the optimal partition or cut of the graph .
  - Deep learning is a technique that uses neural networks or machine learning models to learn the features or representations of the image and segments it by predicting the labels or masks for each pixel or region .