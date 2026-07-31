# Multiple Time – Alignment Paths for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Time alignment is the process of finding the best correspondence between the frames of two time series, such as speech signals or speech and biosignal data .
- Time alignment is useful for many applications, such as speech recognition, speech synthesis, voice conversion, speech to lips synchronization, and articulatory-to-acoustic mapping  .
- Time alignment can be challenging when the time series have different lengths, sampling rates, feature dimensions, or temporal variations .
- One common technique for time alignment is dynamic time warping (DTW), which finds the optimal alignment path between two time series by minimizing the cumulative distance between the frames.
- DTW can be implemented using dynamic programming, which computes a cost matrix that stores the distances between all pairs of frames from the two time series, and then traces back the optimal path from the matrix.
- However, DTW has some limitations, such as:
  - It assumes that the optimal alignment path is monotonic, i.e., it does not allow for backward or skipping movements.
  - It is sensitive to outliers and noise in the time series, which can affect the distance measure and the alignment quality.
  - It is computationally expensive, especially for long or high-dimensional time series, as it requires comparing all pairs of frames and storing the cost matrix.
- To overcome these limitations, some variations and extensions of DTW have been proposed, such as:
  - Ordered, graph search technique, which reduces the search space for the optimal alignment path by imposing some constraints on the possible movements and pruning the cost matrix.
  - Multiview temporal alignment by dependence maximisation in the latent space (TRANSIENCE), which projects the time series into a common, latent subspace where the frames are maximally similar, and then applies DTW on the projected embeddings.
  - Dynamic temporal alignment of speech to lips (DTAL), which uses a deep neural network to learn a mapping from speech features to lip features, and then applies DTW on the mapped features.
- These techniques aim to find multiple time-alignment paths that can capture the temporal variations and dependencies between the time series, and improve the alignment quality and efficiency  .