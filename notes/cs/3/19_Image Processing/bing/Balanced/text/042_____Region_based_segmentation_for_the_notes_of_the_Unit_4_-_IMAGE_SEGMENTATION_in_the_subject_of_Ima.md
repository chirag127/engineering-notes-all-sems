### Region based segmentation

- Region based segmentation is a technique for determining the regions directly from the image pixels, without using edge detection.
- Region based segmentation methods look for similarities between adjacent pixels, such as intensity, color, texture, etc., and group them into unique regions .
- Region based segmentation methods can be classified into two types: region growing and region splitting and merging .
- Region growing is a method that starts with some initial seed points, and grows the regions by adding neighboring pixels that satisfy some similarity criteria.
- Region splitting and merging is a method that starts with the whole image as a single region, and recursively splits it into smaller regions if they are not homogeneous, or merges adjacent regions if they are similar.
- Region based segmentation methods can be applied to 3D images as well, by using 3D seed points and 3D similarity measures.
- Region based segmentation methods are simple and fast, but they may suffer from over-segmentation or under-segmentation, depending on the choice of seed points and similarity criteria.
- Region based segmentation methods may also be sensitive to noise and outliers, which can affect the region growing or splitting and merging process.