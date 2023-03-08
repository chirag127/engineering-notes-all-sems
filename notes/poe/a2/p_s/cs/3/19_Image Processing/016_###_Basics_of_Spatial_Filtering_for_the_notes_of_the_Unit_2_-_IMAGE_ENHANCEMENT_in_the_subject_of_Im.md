 Here is the content in markdown format for the topic ### Basics of Spatial Filtering for the notes of the Unit 2 - IMAGE ENHANCEMENT in the subject of Image Processing:

### Basics of Spatial Filtering

- Spatial filtering is a technique used to manipulate the spatial content of an image by modifying the pixels in an image based on some rule or algorithm.
- It is done by applying a convolution mask or kernel over the image. The kernel is slid over the image and the value of each pixel is replaced by a new value that depends on the kernel and the surrounding pixels.
- Types of Spatial Filters:
    - Smoothing Filters: Also called low-pass filters. Blur images and reduce noise. Eg. Average, Gaussian filter.
    - Sharpening Filters: Also called high-pass filters. Enhance edges and high-frequency components. Eg. Laplacian, Sobel filter.
    - Custom Filters: User defines kernel to get desired properties. Eg. Emboss filter.
- Working: At each pixel, the kernel is centered and the new pixel value is calculated by taking a weighted sum of the neighboring pixels under the kernel. The kernel decides the weights. Larger weights for pixels we want to amplify.
- Examples:
    - 3x3 Average Filter: All weights = 1/9. Blurs image, reduces noise.
    - 3x3 Gaussian Filter: Weights decrease with distance. Smooths while preserving edges.
    - 3x3 Laplacian Filter: [0 1 0; 1 -4 1; 0 1 0]. Enhances edges.
- Advantages: Simple to implement, can amplify/suppress specific frequencies, reduce noise, enhance edges.
- Disadvantages: Can introduce distortions/artifacts, choosing right kernel is challenging, smoothing can remove fine details.
- Applications: Noise removal, edge detection, blurring, sharpening, etc.