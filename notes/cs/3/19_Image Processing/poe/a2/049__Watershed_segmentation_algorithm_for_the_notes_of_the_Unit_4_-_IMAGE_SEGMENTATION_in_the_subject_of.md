 Here is the formal notes on Watershed Segmentation Algorithm for Unit 4 - Image Segmentation in Markdown format:

### Watershed Segmentation Algorithm

1. Watershed algorithm treats the image as a topographic relief, where the brightness of each pixel is treated as its height.
2. Dark regions are like valleys and bright regions are like mountains.
3. The process of flooding this topographic relief filled with dams is equivalent to segmentation.
4. The dams are placed at the locations where the region boundaries exist to prevent the merging of adjacent regions.
5. The key steps involved in watershed segmentation are:

- Finding regional minima of the image. These correspond to the markers or seeds of the segmentation.
- Performing morphological dilation on the image. This results in oversegmentation.
- Finding watershed lines. This connects all regional minima and forms the boundaries between segments.
- Merging adjacent regions based on similarity to obtain the final segments.

6. The advantages of watershed algorithm are:
- It produces closed and continuous boundaries.
- It can segment images with intensity inhomogeneities.
- It is simple and intuitive.

7. The disadvantages are:
- It leads to oversegmentation.
- It is sensitive to noise.
- It has high computational complexity.

8. Various techniques are used to reduce oversegmentation such as preprocessing, hierarchical approaches and gradient-based methods.