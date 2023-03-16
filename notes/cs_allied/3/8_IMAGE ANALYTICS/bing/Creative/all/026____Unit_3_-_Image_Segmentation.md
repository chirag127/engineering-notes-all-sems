## Unit 3 - Image Segmentation

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as color, texture, shape, or intensity.
- Image segmentation can be used for various applications, such as object detection, face recognition, medical imaging, scene understanding, and image editing.
- Image segmentation can be classified into two types: supervised and unsupervised.
  - Supervised segmentation uses a set of labeled images to train a model that can segment new images based on the learned features and classes.
  - Unsupervised segmentation does not use any labels, but instead relies on clustering or grouping pixels based on their similarity or dissimilarity.
- Some common methods for image segmentation are:
  - Thresholding: This method uses a global or local threshold value to separate the foreground and background pixels based on their intensity values.
  - Edge detection: This method uses filters or operators to detect the boundaries or edges of objects or regions in an image.
  - Region growing: This method starts from a seed pixel or region and expands it by adding neighboring pixels that satisfy some homogeneity criterion.
  - Region splitting and merging: This method recursively divides an image into smaller regions until they are homogeneous or satisfy some stopping criterion, and then merges adjacent regions that are similar or belong to the same class.
  - Watershed: This method treats an image as a topographic surface, where the intensity values represent the height, and finds the catchment basins or regions that are separated by the watershed lines or ridges.
  - K-means clustering: This method partitions the pixels into k clusters based on their feature vectors, such as color, texture, or location, and assigns each pixel to the cluster with the nearest centroid or mean.
  - Mean shift clustering: This method iteratively shifts each pixel to the mode or peak of the feature space density, and forms clusters around the modes.
  - Graph cut: This method models an image as a weighted graph, where the nodes represent pixels and the edges represent the similarity or dissimilarity between pixels, and finds the minimum cut or partition that separates the foreground and background regions.
  - Markov random field: This method models an image as a probabilistic graphical model, where the nodes represent pixels and the edges represent the spatial dependencies or constraints between pixels, and finds the maximum a posteriori or most likely segmentation that satisfies the prior and likelihood terms.
  - Neural networks: This method uses a deep learning model, such as a convolutional neural network or a recurrent neural network, to learn the features and classes of the image segments from a large amount of labeled data, and outputs a pixel-wise or region-wise segmentation map.