# Multiple Time – Alignment Paths for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Time alignment is the process of finding the best correspondence between the frames of two time series, such as speech signals or speech and biosignal data .
- Time alignment is useful for many applications of speech analysis, such as speech recognition, speech synthesis, voice conversion, speech enhancement, and speech-to-lips synchronization  .
- Multiple time-alignment paths are the possible ways of aligning two time series, which may have different lengths and feature dimensions.
- Multiple time-alignment paths can be represented by a matrix, where each element corresponds to the distance or similarity between a pair of frames from the two time series.
- The optimal time-alignment path is the one that minimizes or maximizes a certain objective function, such as the total distance or the total similarity along the path.
- There are different methods for finding the optimal time-alignment path, such as dynamic time warping (DTW), hidden Markov models (HMMs), and multiview temporal alignment by dependence maximization in the latent space (TRANSIENCE) .
- DTW is a classical method that uses dynamic programming to find the optimal path that minimizes the total distance between the two time series.
- HMMs are probabilistic models that use a set of states and transition probabilities to find the optimal path that maximizes the likelihood of the two time series.
- TRANSIENCE is a novel method that uses a neural network to project the two time series into a common latent space, where the optimal path maximizes the similarity between the embeddings.
- Multiple time-alignment paths can be used to compare the performance of different methods, to evaluate the robustness of the alignment, and to explore the variability of the alignment.