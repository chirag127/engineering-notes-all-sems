# Basic Concepts for the Notes of the Unit 4 - Image Segmentation in the Subject of Image Processing

- Image segmentation is the process of partitioning an image into multiple segments, such as regions, objects, or boundaries .
- Image segmentation is typically used to locate objects and boundaries in images, such as faces, cars, roads, tumors, etc .
- Image segmentation can reduce the complexity of the image and enable further processing or analysis of each image segment.
- Image segmentation can be performed by assigning a label to every pixel in an image such that pixels with the same label share certain characteristics, such as color, intensity, texture, or shape .
- Image segmentation can be based on several relevant heuristics, or high-level image features, such as edges, regions, contours, or saliency.
- Image segmentation can be classified into two main types: supervised and unsupervised.
  - Supervised image segmentation uses prior knowledge or training data to guide the segmentation process, such as ground truth labels, annotations, or models.
  - Unsupervised image segmentation does not use any prior knowledge or training data, but relies on the inherent properties or similarities of the image pixels to group them into segments.
- Image segmentation can be further categorized into different techniques, such as thresholding, clustering, region growing, region splitting and merging, watershed, active contours, graph-based, or deep learning-based methods .
  - Thresholding is a simple and fast technique that divides the image pixels into two or more segments based on a predefined threshold value or range of values .
  - Clustering is a technique that groups the image pixels into segments based on their similarity or proximity in a feature space, such as color, intensity, or texture .
  - Region growing is a technique that starts from a seed pixel or region and expands it to neighboring pixels or regions that satisfy some homogeneity criteria, such as color, intensity, or texture .
  - Region splitting and merging is a technique that recursively divides the image into smaller regions until each region is homogeneous or meets some stopping criteria, and then merges adjacent regions that are similar or meet some merging criteria .
  - Watershed is a technique that treats the image as a topographic surface and segments it into regions that correspond to the catchment basins of the surface, using the image gradient as the height function .
  - Active contours is a technique that uses a deformable curve or surface to fit the boundaries of the image segments, based on some energy minimization or optimization criteria .
  - Graph-based is a technique that represents the image as a graph, where the nodes are the pixels or regions and the edges are the similarities or distances between them, and segments the image by finding the optimal cuts or partitions of the graph .
  - Deep learning-based is a technique that uses neural networks or other machine learning models to learn the features or representations of the image segments, and outputs the pixel labels or masks for the image .