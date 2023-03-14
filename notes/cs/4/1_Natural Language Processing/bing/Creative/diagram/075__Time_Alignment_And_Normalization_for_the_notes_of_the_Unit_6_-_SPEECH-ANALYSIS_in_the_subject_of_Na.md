Time alignment and normalization are techniques for aligning and comparing speech signals from different speakers or sources. Time alignment is the process of finding the optimal correspondence between the frames of two speech signals, based on some measure of similarity or dissimilarity. Normalization is the process of adjusting the acoustic features of speech signals to reduce the effects of speaker variability or channel distortion.

One of the main applications of time alignment and normalization is voice conversion, which is the task of transforming the speech of a source speaker into the speech of a target speaker, while preserving the linguistic content and the prosody. Voice conversion can be done using parallel corpus-based methods, which require a set of utterances spoken by both the source and the target speakers, and aligned in time. The alignment can be done using methods such as dynamic time warping (DTW) or hidden Markov models (HMMs).

The following diagram illustrates the basic architecture of a parallel corpus-based voice conversion system, using DTW for time alignment and cepstral mean and variance normalization (CMVN) for feature normalization. The diagram is drawn using ASCII characters, as requested.

```
+----------------+     +----------------+     +----------------+
| Source speaker |     | Target speaker |     | Converted      |
| utterances     |     | utterances     |     | speech         |
+----------------+     +----------------+     +----------------+
       |                      |                      ^
       |                      |                      |
       |                      |                      |
       v                      v                      |
+----------------+     +----------------+     +----------------+
| Feature        |     | Feature        |     | Feature        |
| extraction     |     | extraction     |     | transformation |
+----------------+     +----------------+     +----------------+
       |                      |                      ^
       |                      |                      |
       |                      |                      |
       v                      v                      |
+----------------+     +----------------+     +----------------+
| Feature        |     | Feature        |     | Feature        |
| normalization  |     | normalization  |     | normalization  |
+----------------+     +----------------+     +----------------+
       |                      |                      ^
       |                      |                      |
       |                      |                      |
       v                      v                      |
+----------------+     +----------------+     +----------------+
| Time alignment |---->| Parallel       |---->| Speech         |
| using DTW      |     | feature pairs  |     | synthesis      |
+----------------+     +----------------+     +----------------+
```