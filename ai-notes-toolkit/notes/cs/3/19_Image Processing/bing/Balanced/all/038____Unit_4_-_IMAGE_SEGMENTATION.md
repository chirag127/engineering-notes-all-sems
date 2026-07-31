## Unit 4 - IMAGE SEGMENTATION

- Image segmentation is the process of partitioning an image into multiple segments, each of which has a label or a class  .
- Image segmentation is typically used to locate objects and boundaries in images, such as people, animals, buildings, roads, etc .
- Image segmentation can reduce the complexity of the image and enable further processing or analysis of each image segment.
- Image segmentation can be based on various heuristics or high-level image features, such as color, intensity, texture, shape, edge, region, etc.
- Image segmentation can be classified into two main types: supervised and unsupervised.
  - Supervised image segmentation uses a set of labeled images as training data to learn a model that can segment new images.
  - Unsupervised image segmentation does not use any labeled images, but relies on clustering or grouping algorithms to find the natural segments in the image.
- Image segmentation can be further divided into several subtypes, such as semantic segmentation, instance segmentation, panoptic segmentation, etc.
  - Semantic segmentation assigns a class label to each pixel in the image, such as person, car, sky, etc.
  - Instance segmentation assigns a class label and an instance identifier to each pixel in the image, such as person 1, person 2, car 1, car 2, etc.
  - Panoptic segmentation combines semantic and instance segmentation, and also assigns a class label to the background pixels, such as road, grass, wall, etc.
- Image segmentation can be implemented using various techniques, such as thresholding, region growing, edge detection, watershed, graph-based methods, neural networks, etc.
  - Thresholding is a simple technique that divides the image into two or more segments based on a predefined or adaptive threshold value.
  - Region growing is a technique that starts from a seed pixel and expands the segment by adding neighboring pixels that have similar properties.
  - Edge detection is a technique that finds the boundaries of the segments by detecting the discontinuities in the image.
  - Watershed is a technique that treats the image as a topographic surface and finds the segments by flooding the surface from the local minima.
  - Graph-based methods are techniques that model the image as a graph and find the segments by partitioning the graph into subgraphs.
  - Neural networks are techniques that use deep learning models, such as convolutional neural networks (CNNs), to learn the features and the labels of the segments from the data.