### Point for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of assigning a label to every pixel in an image such that pixels with the same label share certain characteristics .
- Image segmentation is typically used to locate objects and boundaries (lines, curves, etc.) in images .
- Image segmentation can reduce the complexity of the image and enable further processing or analysis of each image segment.
- Image segmentation can be classified into two main types: semantic segmentation and instance segmentation.
- Semantic segmentation assigns a class label to each pixel, such as sky, road, car, person, etc. Semantic segmentation does not distinguish between different instances of the same class.
- Instance segmentation assigns a unique label to each pixel belonging to a specific object instance, such as car1, car2, person1, person2, etc. Instance segmentation can separate overlapping objects of the same class.
- Some of the common techniques for image segmentation are: thresholding, region-based methods, edge-based methods, clustering, and deep learning.
- Thresholding is a simple technique that divides the image into foreground and background based on a predefined intensity value.
- Region-based methods are techniques that group pixels based on their similarity or proximity, such as region growing, region splitting, and region merging.
- Edge-based methods are techniques that detect the boundaries of objects based on the discontinuities in the image intensity, such as gradient, Laplacian, Canny, and Sobel operators.
- Clustering is a technique that partitions the image into clusters based on the similarity of pixel features, such as color, texture, shape, etc. Some of the popular clustering algorithms are k-means, mean-shift, and hierarchical clustering.
- Deep learning is a technique that uses neural networks to learn the features and labels of the image segments from a large amount of annotated data. Some of the popular deep learning models for image segmentation are U-Net, SegNet, Mask R-CNN, and DeepLab.