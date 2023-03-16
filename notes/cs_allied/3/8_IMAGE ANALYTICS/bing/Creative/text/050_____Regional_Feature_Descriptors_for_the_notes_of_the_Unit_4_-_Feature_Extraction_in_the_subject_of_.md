### Regional Feature Descriptors for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Regional feature descriptors are methods to extract and describe distinctive points or regions in an image that can be used for image analysis tasks such as matching, retrieval, and classification .
- Regional feature descriptors consist of two steps: feature detection and feature description .
- Feature detection is the process of finding and locating salient regions or points in an image that are invariant to changes in scale, rotation, illumination, and viewpoint  .
- Feature description is the process of computing a signature or a vector for each detected feature that captures its local appearance and neighborhood information  .
- Some examples of feature detection algorithms are Harris corner detector, SIFT, SURF, FAST, ORB, etc  .
- Some examples of feature description algorithms are SIFT, SURF, ORB, BRIEF, FREAK, LBP, etc  .
- Regional feature descriptors can be classified into two types: hand-crafted and learned .
- Hand-crafted feature descriptors are designed based on human knowledge and intuition, such as using gradients, histograms, or binary patterns to represent local patches .
- Learned feature descriptors are obtained by training deep neural networks on large-scale datasets to learn the optimal representation for each feature .
- Regional feature descriptors can be further encoded by methods such as Bag of Words (BoW), Vector of Locally Aggregated Descriptors (VLAD), or Fisher Vector (FV) to generate a global feature representation for the whole image .