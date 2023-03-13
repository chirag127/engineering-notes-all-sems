### Weighted Cepstral Distances And Filtering for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Cepstral distance is a measure of similarity between two speech signals based on their cepstral coefficients, which are obtained by applying a discrete cosine transform (DCT) to the log-magnitude spectrum of the signal.
- Cepstral distance is often used in speech recognition and speaker recognition systems to compare the input speech with the stored templates or models of words or speakers.
- However, cepstral distance is not a very robust measure, as it does not account for the different importance or variability of different cepstral coefficients. For example, the lower-order cepstral coefficients are more related to the vocal tract shape and the speaker identity, while the higher-order cepstral coefficients are more related to the pitch and the noise level of the speech.
- Therefore, some researchers have proposed weighted cepstral distance measures, which assign different weights to different cepstral coefficients according to their statistical properties or their relevance to the recognition task.
- One example of a weighted cepstral distance measure is the inverse variance weighted cepstral distance (IVWCD), which was proposed by Tohkura et al. . The IVWCD is defined as:

$$
IVWCD = \sqrt{\sum_{i=1}^N \frac{(c_i - d_i)^2}{\sigma_i^2}}
$$

where $c_i$ and $d_i$ are the cepstral coefficients of the two speech signals to be compared, $N$ is the number of cepstral coefficients, and $\sigma_i^2$ is the variance of the $i$-th cepstral coefficient estimated from a large speech database.

- The IVWCD assigns higher weights to the cepstral coefficients that have lower variance, which means they are more stable and discriminative across different speech signals. The IVWCD has been shown to improve the performance of speaker-independent isolated word recognition systems using dynamic time warping (DTW) techniques .
- Another example of a weighted cepstral distance measure is the log-index weighted cepstral distance (LIWCD), which was proposed by Zheng and Wu . The LIWCD is defined as:

$$
LIWCD = \sqrt{\sum_{i=1}^N \log(i) (c_i - d_i)^2}
$$

where $c_i$ and $d_i$ are the cepstral coefficients of the two speech signals to be compared, and $N$ is the number of cepstral coefficients.

- The LIWCD assigns higher weights to the higher-order cepstral coefficients, which means they are more sensitive to the fine details of the speech spectrum. The LIWCD has been shown to improve the performance of speaker-independent and speaker-dependent isolated word recognition systems using statistic techniques .

- A possible mnemonic to remember the difference between IVWCD and LIWCD is that IVWCD is **I**nverse **V**ariance **W**eighted, which means it gives more weight to the **low**-variance coefficients, while LIWCD is **L**og-**I**ndex **W**eighted, which means it gives more weight to the **high**-index coefficients.

- A possible application of weighted cepstral distance measures is to use them as a feature extraction method for speech emotion recognition, which is the task of identifying the emotional state of a speaker from their speech. Weighted cepstral distance measures can capture the spectral variations of speech signals that are related to different emotions, such as anger, sadness, happiness, etc. For example, one can compute the weighted cepstral distance between the input speech and a neutral speech template, and use it as a feature vector for emotion classification. Alternatively, one can compute the weighted cepstral distance between the input speech and different emotion-specific speech templates, and use them as a feature vector for emotion classification.