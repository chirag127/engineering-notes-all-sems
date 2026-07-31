## Unit 3 - Image Segmentation

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as color, texture, intensity, shape, etc.
- Image segmentation can be used for various applications, such as object detection, face recognition, medical imaging, scene understanding, etc.
- Image segmentation can be classified into two main types: supervised and unsupervised.
  - Supervised segmentation uses a set of labeled images as training data to learn a model that can segment new images based on the given labels.
  - Unsupervised segmentation does not use any labeled data, but instead relies on some intrinsic properties of the image, such as similarity, continuity, or compactness, to group pixels into regions.
- Some common methods for image segmentation are:
  - Thresholding: This method uses a global or local threshold value to separate the foreground and background pixels based on their intensity values.
  - Edge detection: This method uses filters or operators to detect the boundaries or edges of the objects in the image, and then segments the image based on the edge map.
  - Region growing: This method starts from a set of seed pixels and expands the regions by adding neighboring pixels that are similar to the seeds based on some criteria, such as intensity, color, or texture.
  - Clustering: This method groups pixels into clusters based on their feature vectors, such as intensity, color, or texture, using algorithms such as K-means, Fuzzy C-means, or Mean-shift.
  - Graph-based: This method models the image as a graph, where the nodes are the pixels and the edges are the similarities or distances between the pixels, and then partitions the graph into segments using algorithms such as Minimum Spanning Tree, Normalized Cuts, or Graph Cuts.
  - Deep learning: This method uses neural networks, such as Convolutional Neural Networks (CNNs), Fully Convolutional Networks (FCNs), or U-Nets, to learn a mapping from the input image to the output segmentation mask, using labeled or unlabeled data.