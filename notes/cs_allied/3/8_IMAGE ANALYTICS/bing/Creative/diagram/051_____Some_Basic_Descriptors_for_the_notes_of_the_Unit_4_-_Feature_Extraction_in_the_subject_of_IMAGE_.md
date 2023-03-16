Hello, I am Sydney, your AI assistant. I can help you with your study material for IMAGE ANALYTICS. Here is some content on the topic of Some Basic Descriptors for the notes of the Unit 4 - Feature Extraction.

### Some Basic Descriptors

- A descriptor is a representation of a local feature that captures its distinctive characteristics.
- Descriptors are usually computed from the image patch around the detected feature point, such as a corner, edge, or blob.
- Descriptors can be classified into two types: global and local.
  - Global descriptors describe the whole image or a large region of it, such as color histograms, texture features, or shape features.
  - Local descriptors describe a small region around a feature point, such as SIFT, SURF, or ORB.
- The main properties of a good descriptor are:
  - Distinctiveness: it should be able to distinguish between different features and match similar ones.
  - Robustness: it should be invariant or tolerant to common image transformations, such as rotation, scaling, illumination, noise, or perspective distortion.
  - Efficiency: it should be computationally fast and compact in memory.
- Some examples of popular descriptors are:
  - SIFT (Scale-Invariant Feature Transform): it computes a 128-dimensional vector from the gradient orientation histogram of a 16x16 patch around the feature point, at multiple scales and orientations.
  - SURF (Speeded-Up Robust Features): it computes a 64-dimensional vector from the Haar wavelet responses of a 20x20 patch around the feature point, at multiple scales and orientations.
  - ORB (Oriented FAST and Rotated BRIEF): it computes a binary string of 256 bits from the intensity comparisons of a 31x31 patch around the feature point, at a single scale and orientation.