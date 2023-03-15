### Segmentation by Morphological Watersheds

- Segmentation by morphological watersheds is a region-based technique that utilizes image morphology .
- The aim of segmentation is to separate regions with respect to brightness, color, reflectivity, texture, etc  .
- Segmentation is based on three principal concepts: detection of discontinuities, thresholding, and region processing  .
- Watershed segmentation requires the selection of at least one marker or seed point interior to each object of the image, including the background as a separate object .
- The general concept of watershed segmentation was introduced by Digabel and Lantuejoul in 1978 .
- A modified watershed algorithm for image segmentation using distance transform and image smoothing method has been proposed to reduce over-segmentation .
- OpenCV has implemented a marker-based watershed algorithm where the user can specify which valley points are to be merged and which are not .
