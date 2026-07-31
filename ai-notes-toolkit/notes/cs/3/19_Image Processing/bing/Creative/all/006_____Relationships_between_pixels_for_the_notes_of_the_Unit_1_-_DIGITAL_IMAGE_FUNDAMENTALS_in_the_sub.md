# Relationships between pixels

- A pixel is the smallest unit of a digital image that can be displayed or manipulated.
- Pixels are arranged in a two-dimensional grid, where each pixel has a row and column index.
- The relationship between pixels can be described by their spatial and intensity properties.
- Spatial properties refer to the location, size, shape, and orientation of pixels and their neighborhoods.
- Intensity properties refer to the brightness, contrast, color, and texture of pixels and their regions.
- Some common spatial relationships between pixels are:

  - Adjacency: Two pixels are adjacent if they share a common edge or corner. There are four types of adjacency: 4-adjacency, 8-adjacency, m-adjacency, and n-adjacency.
  - Connectivity: Two pixels are connected if there is a path of adjacent pixels between them. There are two types of connectivity: 4-connectivity and 8-connectivity.
  - Distance: The distance between two pixels is a measure of their separation. There are different ways to define distance, such as Euclidean, city-block, chessboard, and weighted distance.
  - Region: A region is a set of connected pixels that have similar intensity properties. Regions can be classified as binary, gray-level, or color regions.
  - Boundary: A boundary is a set of pixels that separates a region from its background or from other regions. Boundaries can be classified as internal, external, or mixed boundaries.

- Some common intensity relationships between pixels are:

  - Histogram: A histogram is a graphical representation of the frequency distribution of pixel intensities in an image. Histograms can be used to analyze the contrast, brightness, and dynamic range of an image.
  - Thresholding: Thresholding is a process of converting a gray-level or color image into a binary image by assigning a pixel to either 0 or 1 based on whether its intensity is above or below a certain threshold value. Thresholding can be used to segment an image into foreground and background regions.
  - Enhancement: Enhancement is a process of modifying the intensity properties of an image to improve its appearance or suitability for a specific task. Enhancement can be done by using techniques such as contrast stretching, histogram equalization, filtering, sharpening, and smoothing.
  - Quantization: Quantization is a process of reducing the number of distinct intensity levels in an image to a smaller set of values. Quantization can be used to compress an image or to simplify its analysis. Quantization can be done by using techniques such as uniform, nonuniform, or adaptive quantization.