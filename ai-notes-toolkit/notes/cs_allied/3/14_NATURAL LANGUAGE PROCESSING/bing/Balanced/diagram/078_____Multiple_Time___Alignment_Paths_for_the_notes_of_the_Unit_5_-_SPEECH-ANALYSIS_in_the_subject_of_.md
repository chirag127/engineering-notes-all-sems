### Multiple Time – Alignment Paths for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Time alignment is the process of finding the best correspondence between the frames of two time series, such as speech signals or speech and biosignal data .
- Time alignment is useful for many applications of speech analysis, such as speech recognition, speech synthesis, voice conversion, speech enhancement, and speech to lips synchronization  .
- Time alignment can be challenging when the time series have different lengths, sampling rates, feature dimensions, or temporal variations  .
- One common method for time alignment is dynamic time warping (DTW), which finds the optimal alignment path between two time series by minimizing the cumulative distance between the frames.
- DTW can be implemented using various algorithms, such as ordered graph search, fast DTW, or multiview temporal alignment .
- However, DTW has some limitations, such as being sensitive to noise, requiring a predefined distance metric, and producing a single alignment path that may not capture the diversity of the time series .
- Therefore, some alternative methods have been proposed to overcome these limitations, such as multiple time-alignment paths (MTAP), which can find multiple alignment paths between two time series by using a probabilistic model or a latent subspace .
- MTAP can be useful for applications that require multiple interpretations of the time series, such as voice conversion, speech enhancement, or speech to lips synchronization  .
- MTAP can also be more robust to noise, more flexible to different distance metrics, and more informative to the time series structure than DTW .
- Some examples of MTAP methods are multiview temporal alignment by dependence maximisation in the latent space (TRANSIENCE), which projects the time series into a common latent subspace where the alignment paths are maximally similar, and probabilistic time alignment, which models the alignment paths as hidden variables in a probabilistic graphical model.