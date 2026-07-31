### Variable Thresholding for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as pixel intensity, color, texture, etc.
- Image thresholding is a simple and widely used technique for image segmentation, where a grayscale or color image is converted into a binary image, i.e., one that has only two pixel values: 0 (black) or 1 (white).
- Image thresholding can be done in two ways: global or local.
  - Global thresholding applies a single threshold value to the whole image, such that any pixel with an intensity above the threshold is set to 1, and any pixel below the threshold is set to 0.
  - Local thresholding applies different threshold values to different regions of the image, depending on the local characteristics of the image, such as brightness, contrast, or noise level.
- Variable thresholding is a type of local thresholding, where the threshold value is not fixed, but varies according to some function of the pixel intensity or its neighborhood.
- Variable thresholding can be useful for images that have uneven illumination, varying background, or complex foreground objects.
- Some examples of variable thresholding methods are:
  - Adaptive thresholding: The threshold value is computed as a weighted mean of the pixel intensity and its neighborhood, with a constant offset. The weights can be uniform or Gaussian, depending on the desired smoothness of the result.
  - Otsu's method: The threshold value is determined by maximizing the between-class variance of the pixel intensities, i.e., the difference between the mean intensities of the foreground and background classes.
  - Niblack's method: The threshold value is computed as the mean of the pixel intensity and its neighborhood, plus or minus a factor times the standard deviation of the neighborhood.
  - Bernsen's method: The threshold value is computed as the midpoint of the minimum and maximum pixel intensities in the neighborhood. If the difference between the minimum and maximum is less than a contrast threshold, the pixel is set to 0 or 1 depending on a global threshold.