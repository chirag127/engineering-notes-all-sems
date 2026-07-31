### Multiple Time – Alignment Paths for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Time alignment is the process of finding the best correspondence between the frames of two time series, such as speech signals or speech and biosignal data .
- Time alignment is useful for many applications of speech analysis, such as speech recognition, speech synthesis, voice conversion, speech enhancement, and speech to lips synchronization  .
- Time alignment can be challenging when the time series have different lengths, sampling rates, feature dimensions, or temporal variations .
- One common technique for time alignment is dynamic time warping (DTW), which finds the optimal alignment path between two time series by minimizing the cumulative distance between the frames.
- DTW can be implemented using a dynamic programming algorithm that searches for the optimal path in a matrix of distances between the frames of the two time series.
- However, DTW has some limitations, such as the assumption of monotonicity and continuity of the alignment path, the sensitivity to noise and outliers, and the high computational cost .
- Therefore, some alternative or improved techniques have been proposed, such as:

  - Multiview temporal alignment by dependence maximisation in the latent space (TRANSIENCE), which projects the feature vectors from the two time series into a common latent subspace where they are maximally similar, and then uses a graph search algorithm to find the optimal alignment path.
  - Adaptive, ordered, graph search technique, which uses a heuristic function to guide the search for the optimal alignment path in a graph of possible paths, and adapts the search order and the graph structure according to the characteristics of the time series.
  - Dynamic temporal alignment of speech to lips, which uses a convolutional neural network to extract visual features from the lips, and then uses a recurrent neural network to learn the temporal alignment between the audio and visual features.

- These techniques aim to overcome some of the limitations of DTW and achieve better performance and accuracy for time alignment of different types of time series  .