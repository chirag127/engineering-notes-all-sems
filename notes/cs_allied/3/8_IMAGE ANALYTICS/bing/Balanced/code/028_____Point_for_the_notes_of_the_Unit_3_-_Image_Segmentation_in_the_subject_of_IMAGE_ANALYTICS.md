### Point for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of dividing a digital image into subgroups called image segments, reducing the complexity of the image and enabling further processing or analysis of each image segment.
- Image segmentation is typically used to locate objects and boundaries (lines, curves, etc.) in images .
- Image segmentation is the assignment of labels to pixels to identify objects, people, or other important elements in the image.
- Image segmentation can be done based on different criteria, such as color, intensity, texture, shape, or semantic meaning.
- Image segmentation can be classified into two main types: supervised and unsupervised.
  - Supervised image segmentation uses a set of labeled images as training data to learn a model that can segment new images.
  - Unsupervised image segmentation does not use any labeled data, but relies on clustering or similarity measures to group pixels into segments.
- Image segmentation can also be classified into two main levels: semantic and instance.
  - Semantic image segmentation assigns the same label to all pixels that belong to the same object class, such as person, car, or tree.
  - Instance image segmentation assigns a different label to each individual object of the same class, such as person 1, person 2, or person 3.
- Image segmentation can be implemented using various techniques, such as thresholding, region growing, edge detection, watershed, graph-based methods, or deep learning.
  - Thresholding is a simple technique that divides the image into two or more segments based on a predefined intensity value.
  - Region growing is a technique that starts from a seed pixel and expands the segment by adding neighboring pixels that are similar to the seed pixel.
  - Edge detection is a technique that finds the boundaries of objects by detecting the changes in intensity or color across the image.
  - Watershed is a technique that treats the image as a topographic surface and segments it by finding the catchment basins and the ridges.
  - Graph-based methods are techniques that model the image as a graph, where the nodes are pixels and the edges are weighted by some similarity measure, and segment it by finding the minimum spanning tree or the normalized cuts.
  - Deep learning is a technique that uses neural networks to learn a mapping from the input image to the output segmentation mask.