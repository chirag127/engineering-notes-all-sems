### Regional Feature Descriptors for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Regional feature descriptors are methods that extract and describe distinctive points or regions in an image, such as corners, edges, blobs, etc.
- Regional feature descriptors are useful for image analysis tasks such as object detection, recognition, matching, retrieval, etc.
- Regional feature descriptors can be classified into two categories: local and global.
  - Local feature descriptors operate on small patches of the image around the detected points or regions, and compute a signature or a vector that represents the local appearance, shape, texture, or gradient of the patch.
  - Global feature descriptors operate on the whole image or large regions of the image, and compute a signature or a vector that represents the global characteristics, statistics, or distribution of the image or region.
- Some examples of local feature descriptors are:
  - Scale-Invariant Feature Transform (SIFT): SIFT detects keypoints that are invariant to scale and orientation changes, and describes them using histograms of gradient orientations in a 16x16 neighborhood around each keypoint.
  - Speeded-Up Robust Features (SURF): SURF is similar to SIFT, but uses integral images and Haar wavelets to speed up the detection and description of keypoints.
  - Histogram of Oriented Gradients (HOG): HOG divides the image into small cells, and computes histograms of gradient orientations for each cell. The histograms are then concatenated to form a feature vector for the image or region.
- Some examples of global feature descriptors are:
  - Color Histogram: Color histogram counts the number of pixels in each color bin for the image or region, and forms a feature vector that represents the color distribution.
  - Texture Features: Texture features measure the spatial variation of pixel intensities in the image or region, and can be computed using methods such as co-occurrence matrix, local binary patterns, Gabor filters, etc.
  - Bag of Visual Words (BoVW): BoVW is a method that quantizes the local feature descriptors of an image or region into a fixed number of clusters, and counts the frequency of each cluster in the image or region. The frequency vector is then used as a feature vector that represents the visual content.
- Some recent methods that improve the regional feature descriptors are:
  - Region-Wise Deep Feature Representation (RDFR): RDFR is a method that uses a convolutional neural network (CNN) to extract deep features from different regions of the image, and then encodes them using an improved Vector of Locally Aggregated Descriptors (VLAD) algorithm. The encoded features are then concatenated to form a feature vector for the image or region .
  - Fisher Vector (FV): FV is a method that encodes the local feature descriptors of an image or region using a Gaussian mixture model (GMM), and computes the gradient of the log-likelihood of the descriptors with respect to the GMM parameters. The gradient vector is then used as a feature vector that represents the visual content.