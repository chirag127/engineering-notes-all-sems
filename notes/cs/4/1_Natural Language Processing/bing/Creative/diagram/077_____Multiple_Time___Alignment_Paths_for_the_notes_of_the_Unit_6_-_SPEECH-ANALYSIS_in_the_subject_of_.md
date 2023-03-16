### Multiple Time – Alignment Paths for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Time alignment is the process of finding the best correspondence between the frames of two time series, such as speech signals or speech and biosignal data .
- Time alignment is useful for many applications of speech analysis, such as speech recognition, speech synthesis, voice conversion, speech enhancement, and speech to lips synchronization  .
- Time alignment can be challenging when the time series have different lengths, sampling rates, feature dimensions, or temporal variations .
- One common technique for time alignment is dynamic time warping (DTW), which finds the optimal alignment path between two time series by minimizing the cumulative distance between the frames.
- DTW can be implemented using dynamic programming, which computes a cost matrix that stores the distances between all pairs of frames from the two time series, and then traces back the optimal path from the matrix.
- However, DTW has some limitations, such as:
  - It assumes that the time series have the same feature dimensionality, which may not be true for multimodal data.
  - It does not account for the underlying structure or dependencies of the time series, which may affect the alignment quality.
  - It can be computationally expensive and memory intensive, especially for long time series.
- Therefore, some alternative or improved techniques for time alignment have been proposed, such as:
  - Multiview temporal alignment by dependence maximisation in the latent space (TRANSIENCE), which projects the time series into a common latent space where the feature vectors are maximally similar, and then applies DTW on the latent embeddings.
  - Adaptive, ordered, graph search technique for DTW, which reduces the search space and the computational complexity of DTW by using a heuristic function and a priority queue.
  - Dynamic temporal alignment of speech to lips, which uses a convolutional neural network to extract visual features from the lips, and then applies DTW on the audio and visual features with a modified distance function that incorporates phonetic information.